# https://github.com/mostafaalishahi/eICU_Benchmark

```

# common network
def build_network(config, input_size, output_dim=1, activation='sigmoid'):
    if config.num and config.cat:
        input1 = Input(shape=(input_size, 13))
        
        if config.ohe:
            input2 = Input(shape=(input_size, config.n_cat_class))
            inp = Concatenate(axis=-1)([input1, input2])
        
        else:
            input2 = Input(shape=(input_size, 7))
            x2 = Embedding(config.n_cat_class, config.embedding_dim)(input2)
            x2 = Reshape((int(x2.shape[1]),int(x2.shape[2]*x2.shape[3])))(x2)
            inp = Concatenate(axis=-1)([input1, x2]) #keras.layers.Concatenate(axis=-1)([input1, x2])
    
    elif config.num:
        input1 = Input(shape=(input_size, 13))
        inp = input1 
    
    elif config.cat:
        if config.ohe:
            input1 = Input(shape=(input_size, config.n_cat_class))
            inp = input1       
        else:
            input1 = Input(shape=(input_size, 7))
            x1 = Embedding(config.n_cat_class, config.embedding_dim)(input1)
            inp = Reshape((int(x1.shape[1]),int(x1.shape[2]*x1.shape[3])))(x1)

    mask = Masking(mask_value=0., name="maski")(inp)

    lstm = mask
    for i in range(config.rnn_layers-1):
        lstm = Bidirectional(LSTM(units=config.rnn_units[i],kernel_regularizer=regularizers.l2(0.01),kernel_initializer='glorot_normal' ,name="lstm_{}".format(i+1), return_sequences=True))(lstm)
        lstm = BatchNormalization()(lstm)
        lstm = Dropout(config.dropout)(lstm)

    if config.task in ['rlos', 'dec', 'surv']:  # regression like
        
        lstm = Bidirectional(LSTM(units=config.rnn_units[-1],kernel_regularizer=regularizers.l2(0.01),kernel_initializer='glorot_normal' ,name="lstm_{}".format(config.rnn_layers),return_sequences=True))(lstm)
        
    elif config.task in ['mort', 'phen']:
        lstm = Bidirectional(LSTM(units=config.rnn_units[-1],kernel_regularizer=regularizers.l2(0.01),kernel_initializer='glorot_normal' ,name="lstm_{}".format(config.rnn_layers),return_sequences=False))(lstm)
    

    lstm = BatchNormalization()(lstm)
    lstm = Dropout(config.dropout)(lstm)

    if config.task in ['rlos', 'dec']:
        out = TimeDistributed(Dense(output_dim, activation=activation))(lstm)
    
    elif config.task in ['mort', 'phen']:
        out = Dense(output_dim, activation=activation)(lstm)
    

    if config.num and config.cat:
        model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)
    else:
        model = tf.keras.models.Model(inputs=input1, outputs=out)

    optim = get_optimizer(lr=config.lr)

    if config.task == 'mort':
        
        if config.metric =='sparse_weighted':
            model.compile( tf.losses.sparse_softmax_cross_entropy(labels=label, logits=logits, weights=weights), optimizer=optim, metrics=[metrics.f1, metrics.sensitivity, metrics.specificity, 'accuracy'] )
        else:
            model.compile( loss="binary_crossentropy", optimizer=optim ,metrics=[metrics.f1,metrics.sensitivity, metrics.specificity, 'accuracy'])
        
    elif config.task == 'rlos':
        model.compile(loss='mean_squared_error', optimizer=optim, metrics=['mse'])
    
    elif config.task in ['phen', 'dec']:
        model.compile(loss="binary_crossentropy" ,optimizer=optim, metrics=[metrics.f1,'accuracy'])
    
    else:
        print('Invalid task name')

    # print(model.summary())
    return model
 
    
# from eicu_benchmark
def baseline_network(config, input_size, output_dim=1, activation='sigmoid'):

    if config.num and config.cat:
        input1 = Input(shape=(input_size, 13))
        if config.ohe:
            input2 = Input(shape=(input_size, config.n_cat_class))
            inp = keras.layers.Concatenate(axis=-1)([input1, input2])
            if config.task in ['mort','phen']: #added
                inp = Reshape((int(input2.shape[1])*int(input2.shape[2]+input1.shape[2]),))(inp) #added            
        
        else:
            input2 = Input(shape=(input_size, 7))
            x2 = Embedding(config.n_cat_class, config.embedding_dim)(input2)
            x2 = Reshape((int(x2.shape[1]),int(x2.shape[2]*x2.shape[3])))(x2)
            inp = keras.layers.Concatenate(axis=-1)([input1, x2])
            if config.task in ['mort','phen']: #added
                inp = Reshape((int(x2.shape[1])*int(x2.shape[2]+input1.shape[2]),))(inp)#added


    elif config.num and not config.cat:
        input1 = Input(shape=(input_size, 13))
        inp = input1

        #added
        if config.task in ['mort','phen']: #added
            inp = Reshape((int(input1.shape[1])*int(input1.shape[2]),))(input1)
        #added

    elif config.cat and not config.num:
        if config.ohe:
            input1 = Input(shape=(input_size, config.n_cat_class))
            # inp = Reshape((int(input1.shape[1]),int(input1.shape[2]*input1.shape[3])))(input1)
            # inp = Reshape((int(input1.shape[1])*int(input1.shape[2]),))(input1)
            inp = input1

            #added
            if config.task in ['mort','phen']: #added
                inp = Reshape((int(input1.shape[1])*int(input1.shape[2]),))(input1)
            #added


        else:
            input1 = Input(shape=(input_size, 7))
            x1 = Embedding(config.n_cat_class, config.embedding_dim)(input1)
            inp = Reshape((int(x1.shape[1]),int(x1.shape[2]*x1.shape[3]),))(x1)
            # inp = Reshape((int(input1.shape[1])*int(input1.shape[2]),))(input1)
            #added
            if config.task in ['mort','phen']: #added
                # inp = Reshape((int(x1.shape[1])*int(x1.shape[2]),))(x1)
                inp = Reshape((int(inp.shape[1])*int(inp.shape[2]),))(inp)

    mask = Masking(mask_value=0., name="maski")(inp)

    if config.ann:
        hidden = keras.layers.Dense(64,activation='relu')(mask)
    elif not config.ann:
        hidden = mask
    if config.task in ['rlos', 'dec']:
        out = TimeDistributed(Dense(output_dim, activation=activation))(hidden)

    elif config.task in ['mort', 'phen']:
        out = Dense(output_dim, activation=activation)(hidden)
    
    else:
        print('Invalid task type.')
        exit() 
    optim = metrics.get_optimizer(lr=config.lr)

    if config.num and config.cat:
        model = keras.models.Model(inputs=[input1, input2], outputs=out)
    else:
        model = keras.models.Model(inputs=input1, outputs=out)


    if config.task == 'mort':
        model.compile(loss="binary_crossentropy", optimizer=optim ,metrics=[metrics.f1,metrics.sensitivity, metrics.specificity, 'accuracy'])
    elif config.task == 'rlos':
        model.compile(loss='mean_squared_error', optimizer=optim, metrics=['mse'])
    
    elif config.task in ['phen', 'dec']:
        model.compile(loss="binary_crossentropy" ,optimizer=optim, metrics=[metrics.f1,'accuracy'])
    
    else:
        print('Invalid task name')
        exit()
    # print(model.summary())
    return model
```





