# eicu's latest results


## 2023-03-14

- Corrected on ```NCAT=6```

### Summary
```
================
 FD5_BS16_VAL10_MXL400_OHE0_bilstm_NL2_NU128_BN1_DO0.1_bce_LR0.0010
0
F1=0.697 | SEN=0.595 | SPEC=0.880 | PPV=0.409 | NPV=0.940 | AUC=0.830 | 
F1=0.670 | SEN=0.490 | SPEC=0.897 | PPV=0.375 | NPV=0.933 | AUC=0.808 | 

================
 FD5_BS16_VAL10_MXL400_OHE0_bilstm_NL3_NU64_BN1_DO0.3_bce_LR0.0010
0
F1=0.707 | SEN=0.514 | SPEC=0.920 | PPV=0.471 | NPV=0.932 | AUC=0.821 | 
F1=0.670 | SEN=0.400 | SPEC=0.933 | PPV=0.428 | NPV=0.925 | AUC=0.789 | 
1
F1=0.688 | SEN=0.578 | SPEC=0.889 | PPV=0.393 | NPV=0.944 | AUC=0.821 | 
F1=0.664 | SEN=0.563 | SPEC=0.863 | PPV=0.350 | NPV=0.938 | AUC=0.813 | 

================
 FD5_BS16_VAL3_MXL256_OHE0_bilstm_NL3_NU64_BN0_bce_DO0.3_LR0.0100
0
F1=0.455 | SEN=0.756 | SPEC=0.556 | PPV=0.191 | NPV=0.943 | AUC=0.727 | 
F1=0.445 | SEN=0.652 | SPEC=0.597 | PPV=0.166 | NPV=0.933 | AUC=0.678 | 

================
 FD5_BS64_VAL5_MXL400_OHE0_bilstm_NL2_NU64_BN1_DO0.3_bce_LR0.0010
0
F1=0.654 | SEN=0.776 | SPEC=0.771 | PPV=0.320 | NPV=0.961 | AUC=0.847 | 
F1=0.644 | SEN=0.703 | SPEC=0.797 | PPV=0.298 | NPV=0.956 | AUC=0.824 | 

================
 FD2_BS16_VAL5_MXL400_OHE0_bilstm_NL3_NU128_BN1_DO0.3_bce_LR0.0010
1
F1=0.641 | SEN=0.580 | SPEC=0.833 | PPV=0.305 | NPV=0.940 | AUC=0.788 | 
F1=0.666 | SEN=0.677 | SPEC=0.832 | PPV=0.331 | NPV=0.954 | AUC=0.824 | 

================
 FD5_BS16_VAL10_MXL400_OHE0_bilstm_NL2_NU64_BN1_DO0.3_bce_LR0.0010
1
F1=0.694 | SEN=0.612 | SPEC=0.879 | PPV=0.387 | NPV=0.948 | AUC=0.837 | 
F1=0.678 | SEN=0.626 | SPEC=0.858 | PPV=0.366 | NPV=0.946 | AUC=0.830 | 
3
F1=0.619 | SEN=0.565 | SPEC=0.817 | PPV=0.272 | NPV=0.939 | AUC=0.773 | 
F1=0.656 | SEN=0.671 | SPEC=0.827 | PPV=0.316 | NPV=0.955 | AUC=0.824 | 
4
F1=0.656 | SEN=0.644 | SPEC=0.814 | PPV=0.336 | NPV=0.940 | AUC=0.811 | 
F1=0.644 | SEN=0.730 | SPEC=0.792 | PPV=0.298 | NPV=0.960 | AUC=0.837 | 

================
 FD5_BS16_VAL10_MXL400_OHE1_bilstm_NL3_NU64_BN0_DO0.3_bce_LR0.0100
1
F1=0.652 | SEN=0.659 | SPEC=0.838 | PPV=0.315 | NPV=0.956 | AUC=0.848 | 
F1=0.640 | SEN=0.680 | SPEC=0.819 | PPV=0.326 | NPV=0.952 | AUC=0.835 | 
2
F1=0.629 | SEN=0.596 | SPEC=0.835 | PPV=0.289 | NPV=0.948 | AUC=0.811 | 
F1=0.622 | SEN=0.692 | SPEC=0.771 | PPV=0.294 | NPV=0.948 | AUC=0.843 | 
3
F1=0.612 | SEN=0.636 | SPEC=0.787 | PPV=0.266 | NPV=0.947 | AUC=0.797 | 
F1=0.638 | SEN=0.726 | SPEC=0.796 | PPV=0.298 | NPV=0.961 | AUC=0.843 | 

================
 FD5_BS16_VAL10_MXL400_OHE0_bilstm_NL2_NU64_BN1_DO0.3_bce_LR0.0080
4
F1=0.650 | SEN=0.648 | SPEC=0.805 | PPV=0.326 | NPV=0.940 | AUC=0.808 | 
F1=0.647 | SEN=0.738 | SPEC=0.793 | PPV=0.302 | NPV=0.962 | AUC=0.837 | 




```


# w/ joint loss

```
===============
Evaluation set: 0
F1 0.458, SEN 0.397, SPEC 0.761, PPV 0.172, NPV 0.910, AUCPR 0.189, AUC 0.616, MCC 0.113, SPECAT90 0.170, ===============
Evaluation set: 1
F1 0.440, SEN 0.318, SPEC 0.758, PPV 0.142, NPV 0.898, AUCPR 0.157, AUC 0.586, MCC 0.055, SPECAT90 0.219, ===============
Evaluation set: 2
F1 0.469, SEN 0.528, SPEC 0.714, PPV 0.204, NPV 0.916, AUCPR 0.247, AUC 0.670, MCC 0.170, SPECAT90 0.222, 

/home/lisat/scratch/opensource/eicu/mdls_val/mort_0FD5_BS16_VAL10_MXL256_OHE0_bilstm_NL3_NU64_BN0_DO0.3_LR0.0100
 
===============
Evaluation set: 0
F1 0.101, SEN 0.951, SPEC 0.024, PPV 0.109, NPV 0.796, AUCPR 0.104, AUC 0.476, MCC -0.049, SPECAT90 0.057, ===============
Evaluation set: 1
F1 0.098, SEN 0.962, SPEC 0.025, PPV 0.108, NPV 0.842, AUCPR 0.106, AUC 0.496, MCC -0.026, SPECAT90 0.057, ===============
Evaluation set: 2
F1 0.109, SEN 0.949, SPEC 0.021, PPV 0.119, NPV 0.750, AUCPR 0.113, AUC 0.473, MCC -0.062, SPECAT90 0.045, 

/home/lisat/scratch/opensource/eicu/mdls_val/mort_0FD5_BS64_VAL5_MXL256_OHE0_bilstm_NL3_NU64_BN1_DO0.0_LR0.0010

```

### w/o joint loss

```
===============

loss: 1.8870 - f1: 0.7984 - sensitivity: 0.8100 - specificity: 0.7800 - accuracy: 0.7950 - val_loss: 2.0390 - val_f1: 0.7499 - val_sensitivity: 0.8451 - val_specificity: 0.5861 - val_accuracy: 0.7156

Model-fitting done; saving the final model wts...

Evaluation set: 0
F1 0.635, SEN 0.841, SPEC 0.741, PPV 0.289, NPV 0.974, AUCPR 0.519, AUC 0.871, MCC 0.391, SPECAT90 0.641, ===============
Evaluation set: 1
F1 0.592, SEN 0.743, SPEC 0.714, PPV 0.246, NPV 0.957, AUCPR 0.423, AUC 0.804, MCC 0.305, SPECAT90 0.443, ===============
Evaluation set: 2
F1 0.602, SEN 0.816, SPEC 0.688, PPV 0.266, NPV 0.964, AUCPR 0.472, AUC 0.835, MCC 0.341, SPECAT90 0.521, 

/home/lisat/scratch/opensource/eicu/mdls_val/mort_0FD5_BS16_VAL10_MXL256_OHE0_bilstm_NL3_NU64_BN1_DO0.0_LR0.0010

```

## 2023-03-10 

```
OHE=1; exec( open('mlsurv_bench.py').read()  ) 
```

### bi-LSTM
```
Evaluation set: 1
f1 0.6002918636583375, sen 1.4887892376681615, spec 1.4177740863787376, ppv 0.2545361615129057, npv 0.967687074829932, aucpr 0.4657964824440407, auc 0.8375865619037081, mcc 0.3380975685510748, specat90 0.5452026680348897, ===============
Evaluation set: 2
f1 0.6235308902786831, sen 0.8445440956651719, spec 0.708264119601329, ppv 0.2868020304568528, npv 0.9704125177809388, aucpr 0.5384004364745718, auc 0.8581810631229236, mcc 0.3770813113267653, specat90 0.6119186046511628, 

/home/lisat/scratch/opensource/eicu/mdls_val/set3_fd0_BS32_VAL2_MXL200_OHE1_bilstm_NL2_NU128_BN0_DO0

===============
Evaluation set: 0
f1 0.6836887361543171, sen 1.3871449925261585, spec 1.665905315614618, ppv 0.3495291902071563, npv 0.9649987972095261, aucpr 0.5450063458547288, auc 0.8751265644391156, mcc 0.4286397156354581, specat90 0.6283076923076922, ===============
Evaluation set: 1
f1 0.6346750952032226, sen 1.2002989536621824, spec 1.6154485049833887, ppv 0.29010115606936415, npv 0.9486647969759785, aucpr 0.41794374910896515, auc 0.8063345707703297, mcc 0.32938757783657985, specat90 0.4396100564391996, ===============
Evaluation set: 2
f1 0.6571826041127431, sen 0.7593423019431988, spec 0.7799003322259136, ppv 0.3239795918367347, npv 0.9588971151391371, aucpr 0.5029235705681877, auc 0.8461031117004109, mcc 0.3905626462102504, specat90 0.5550249169435215, 
 /home/lisat/scratch/opensource/eicu/mdls_val/set3_fd0_BS32_VAL2_MXL100_OHE0_bilstm_NL2_NU128_BN1_DO0.3
  
===============

Evaluation set: 0
f1 0.7186771109808923, sen 1.4962630792227205, spec 1.7063953488372092, ppv 0.39518357678641924, npv 0.974158368895211, aucpr 0.6437524017776215, auc 0.9137520876716939, mcc 0.4952338850672574, specat90 0.7431794871794872, ===============
Evaluation set: 1
f1 0.6541701180308503, sen 1.203288490284006, spec 1.6621677740863787, ppv 0.3163064833005894, npv 0.9502611585944919, aucpr 0.4462991137377479, auc 0.8174314295583122, mcc 0.35737887053205114, specat90 0.4635197537198563, ===============
Evaluation set: 2
f1 0.6744435994454036, sen 0.750373692077728, spec 0.8037790697674418, ppv 0.3469246717346234, npv 0.9586428925210501, aucpr 0.48489948328072324, auc 0.8446272762937691, mcc 0.4114986144114981, specat90 0.5882475083056478, 
 /home/lisat/scratch/opensource/eicu/mdls_val/set3_fd0_BS32_VAL2_MXL300_OHE0_bilstm_NL2_NU128_BN1_DO0.0



```

### LSTM 

```
Evaluation set: 0
<string>:598: RuntimeWarning: invalid value encountered in long_scalars
f1 0.47058255707321783, sen 0.0, spec 2.0245016611295683, ppv nan, npv 0.88886862977482, aucpr 0.10772436515088997, auc 0.4865317515407753, mcc 0.0, specat90 0.08820512820512816, ===============
Evaluation set: 1
<string>:598: RuntimeWarning: invalid value encountered in long_scalars
f1 0.4704547648933089, sen 0.0, spec 2.0234634551495017, ppv nan, npv 0.8884127997082688, aucpr 0.10899167283456303, auc 0.495600727036154, mcc 0.0, specat90 0.10138532580810677, ===============
Evaluation set: 2
f1 0.46752742452189106, sen 0.0, spec 1.0, ppv nan, npv 0.8780309936189608, aucpr 0.11914685439539396, auc 0.4958211045394276, mcc 0.0, specat90 0.09115448504983392, 
 /home/lisat/scratch/opensource/eicu/mdls_val/set3_fd0_BS32_VAL2_MXL200_OHE1_lstm_NL2_NU128_BN1_DO0.3
 
===============
Evaluation set: 0
<string>:598: RuntimeWarning: invalid value encountered in long_scalars
f1 0.47058255707321783, sen 0.0, spec 2.0245016611295683, ppv nan, npv 0.88886862977482, aucpr 0.11757455153477597, auc 0.5226236301297827, mcc 0.0, specat90 0.12, ===============
Evaluation set: 1
<string>:598: RuntimeWarning: invalid value encountered in long_scalars
f1 0.4704547648933089, sen 0.0, spec 2.0234634551495017, ppv nan, npv 0.8884127997082688, aucpr 0.12039525313549654, auc 0.5293476292518033, mcc 0.0, specat90 0.12396100564391999, ===============
Evaluation set: 2
f1 0.46752742452189106, sen 0.0, spec 1.0, ppv nan, npv 0.8780309936189608, aucpr 0.12650056614099858, auc 0.5126141250639373, mcc 0.0, specat90 0.07578903654485047, 
 /home/lisat/scratch/opensource/eicu/mdls_val/set3_fd0_BS32_VAL2_MXL200_OHE1_lstm_NL2_NU128_BN1_DO0.0
```




### GRU

```

Evaluation set: 0
<string>:539: RuntimeWarning: invalid value encountered in long_scalars
f1 0.47058255707321783, sen 0.0, spec 2.0245016611295683, ppv nan, npv 0.88886862977482, aucpr 0.10610183025794205, auc 0.47903662102185485, mcc 0.0, specat90 0.07189743589743591, ===============
Evaluation set: 1
<string>:539: RuntimeWarning: invalid value encountered in long_scalars
f1 0.4704547648933089, sen 0.0, spec 2.0234634551495017, ppv nan, npv 0.8884127997082688, aucpr 0.10772383892937355, auc 0.4756227846021254, mcc 0.0, specat90 0.07080554130323247, ===============
Evaluation set: 2
f1 0.46752742452189106, sen 0.0, spec 1.0, ppv nan, npv 0.8780309936189608, aucpr 0.1202017991908337, auc 0.47539141451762684, mcc 0.0, specat90 0.07059800664451832, 
/home/lisat/scratch/opensource/eicu/mdls_val/set3_fd0_BS32_VAL2_MXL200_OHE1_gru_NL2_NU128_BN1_DO0.3
 
===============
Evaluation set: 0
<string>:537: RuntimeWarning: invalid value encountered in long_scalars
f1 0.10001640958319657, sen 1.8221225710014948, spec 0.0, ppv 0.11113137022518005, npv nan, aucpr 0.11183079662179618, auc 0.500616941166572, mcc 0.0, specat90 0.10461538461538467,  

Evaluation set: 1
<string>:537: RuntimeWarning: invalid value encountered in long_scalars
f1 0.1003854670712704, sen 1.8295964125560538, spec 0.0, ppv 0.11158720029173125, npv nan, aucpr 0.11522300681586062, auc 0.5154381164129753, mcc 0.0, specat90 0.08660851718830165,  

Evaluation set: 2
f1 0.1087097822554436, sen 1.0, spec 0.0, ppv 0.12196900638103919, npv nan, aucpr 0.12231280930669887, auc 0.4951821966141759, mcc 0.0, specat90 0.08990863787375414, 
/home/lisat/scratch/opensource/eicu/mdls_val/set3_fd0_BS32_VAL2_MXL200_OHE1_gru_NL2_NU128_BN1_DO0.0
```

```


loss: 0.6244 - f1: 0.7770 - sensitivity: 0.7750 - specificity: 0.7800 - accuracy: 0.7775 - val_loss: 0.6410 - val_f1: 0.7730 - val_sensitivity: 0.7790 - val_specificity: 0.7681 - val_accuracy: 0.7736

```



## 2023-01-11


```
set3_fd0_BS32_VAL10_MXL100_OHE0

Evaluation set: 1
f1 0.6421872872300375, sen 0.28699551569506726, spec 0.31000830564784054, ppv 0.2962962962962963, npv 0.9657179818887451, aucpr 0.5083551622148068, auc 0.8551931393388551, mcc 0.37951438713807045, specat90 0.5659312467932274, ===============
Evaluation set: 2
f1 0.6385373144865749, sen 0.8011958146487295, spec 0.7423172757475083, ppv 0.3016319639842431, npv 0.9641316073354909, aucpr 0.5050289914702604, auc 0.85361543981447, mcc 0.3800604951356159, specat90 0.5627076411960132,


set3_fd0_BS32_VAL10_MXL200_OHE0
===============
Evaluation set: 1
f1 0.6432113288560326, sen 0.2765321375186846, spec 0.3141611295681063, ppv 0.29790660225442833, npv 0.9618563254926892, aucpr 0.5177844267808492, auc 0.864767908189443, mcc 0.3715338347934342, specat90 0.6228835300153925, ===============
Evaluation set: 2
f1 0.6620574372489926, sen 0.8011958146487295, spec 0.7724252491694352, ppv 0.3284313725490196, npv 0.9654814430314042, aucpr 0.5233796886054106, auc 0.8655670684166876, mcc 0.41060270571811225, specat90 0.5899086378737541,
```

```
set3_fd0_BS32_VAL10_MXL300_OHE0_bilstm 

Evaluation set: 1
f1 0.6833296406140636, sen 0.2571001494768311, spec 0.33990863787375414, ppv 0.35537190082644626, npv 0.9573099415204679, aucpr 0.5375760548694353, auc 0.8642422592433587, mcc 0.41165598740516357, specat90 0.6151872755259107, ===============
Evaluation set: 2
f1 0.6822602966374745, sen 0.7653213751868461, spec 0.8081395348837209, ppv 0.3565459610027855, npv 0.961224993825636, aucpr 0.5358478671665712, auc 0.8678694337261444, mcc 0.42688314671570204, specat90 0.6029900332225914, Input arguments
/home/lisat/sksurv/bin/ipython


```

```
set3_fd0_BS32_VAL10_MXL400_OHE0_bilstm 

Evaluation set: 1
f1 0.6329810849352431, sen 0.28101644245142005, spec 0.3073089700996678, ppv 0.2861491628614916, npv 0.962914769030579, aucpr 0.5480923002636858, auc 0.8634736809038648, mcc 0.36219420435075844, specat90 0.6110826064648538, ===============
Evaluation set: 2
f1 0.6552031990845846, sen 0.8251121076233184, spec 0.7562292358803987, ppv 0.31981460023174973, npv 0.9688747007182761, aucpr 0.5461370992291393, auc 0.869810211601587, mcc 0.4096669697076357, specat90 0.5963455149501662, 



eval checkpoint

Evaluation set: 1
f1 0.5859086507689025, sen 0.31988041853512705, spec 0.26785714285714285, ppv 0.24513172966781213, npv 0.9765329295987888, aucpr 0.5243594370949513, auc 0.8646548203683732, mcc 0.3444815975453299, specat90 0.629040533606978, ===============
Evaluation set: 2
f1 0.6001366089261955, sen 0.8714499252615845, spec 0.6671511627906976, ppv 0.2666971637694419, npv 0.97393149439224, aucpr 0.5337439989123475, auc 0.8676049938173205, mcc 0.36000396817596686, specat90 0.5917774086378738, 

```


```
checkpoint_fd4_BS64_VAL9 
===============
Evaluation set: 1
f1 0.5742910438378949, sen 0.28898426323319026, spec 0.31055381400208987, ppv 0.22469410456062291, npv 0.9655620532813515, aucpr 0.3661901555777072, auc 0.8086856547474693, mcc 0.2999445117229623, specat90 0.4562528630325241, ===============
Evaluation set: 2
f1 0.5988899687896228, sen 0.7410586552217453, spec 0.7011494252873564, ppv 0.26591375770020537, npv 0.9488122171945701, aucpr 0.4021213893092761, auc 0.7957410422113692, mcc 0.30814535724827047, specat90 0.47732497387669803, 

```

```
MXL=250; EP=120; fd=4; TK= [2]; VAL=8; BS=16; exec( open('run_val2.py').read() )

checkpoint_fd4_BS64_VAL10 

Running Fold 4...
ntrn 21939 ntst 5484
>> 21939 (5484, 200, 21)
size of class1: 2176 size of class2: 17569
Model wts loaded from checkpoint. Proceed with evaluation...
===============
Evaluation set: 1
f1 0.5814021750297196, sen 0.2675250357653791, spec 0.2808777429467085, ppv 0.23375, npv 0.9641319942611191, aucpr 0.42457436276373683, auc 0.821385527232115, mcc 0.3068407764841609, specat90 0.48083801737353093, ===============
Evaluation set: 2
f1 0.5974686847367547, sen 0.7753934191702432, spec 0.6871473354231975, ppv 0.26581657675331044, npv 0.9544267053701015, aucpr 0.41297427348503696, auc 0.8053487367384068, mcc 0.319173140955656, specat90 0.46562173458725187, 
```


2023-01-01

## AF 

```
trn: ACC=50.0 | PR=43.7 | RC=50.0 | F1=46.6     tst: ACC=50.0 | PR=42.5 | RC=50.0 | F1=45.9
xgb300-mx3-ff0.1
trn: ACC=50.2 | PR=78.7 | RC=50.2 | F1=47.0     tst: ACC=50.1 | PR=59.1 | RC=50.1 | F1=46.1
xgb100-mx3-ff0.3
trn: ACC=50.1 | PR=85.3 | RC=50.1 | F1=46.9     tst: ACC=50.1 | PR=67.5 | RC=50.1 | F1=46.1
xgb300-mx3-ff0.3
trn: ACC=50.8 | PR=89.6 | RC=50.8 | F1=48.2     tst: ACC=50.2 | PR=62.5 | RC=50.2 | F1=46.5
xgb100-mx3-ff0.5
trn: ACC=50.4 | PR=90.9 | RC=50.4 | F1=47.5     tst: ACC=50.1 | PR=67.5 | RC=50.1 | F1=46.2
xgb300-mx3-ff0.5
trn: ACC=51.4 | PR=92.2 | RC=51.4 | F1=49.5     tst: ACC=50.2 | PR=59.2 | RC=50.2 | F1=46.5
xgb100-mx3-ff0.7
trn: ACC=50.5 | PR=91.5 | RC=50.5 | F1=47.7     tst: ACC=50.1 | PR=67.5 | RC=50.1 | F1=46.1
xgb300-mx3-ff0.7
trn: ACC=51.9 | PR=91.4 | RC=51.9 | F1=50.3     tst: ACC=50.3 | PR=59.2 | RC=50.3 | F1=46.7
xgb100-mx3-ff0.9
trn: ACC=50.5 | PR=93.7 | RC=50.5 | F1=47.6     tst: ACC=50.0 | PR=42.5 | RC=50.0 | F1=45.9
xgb300-mx3-ff0.9
trn: ACC=52.1 | PR=90.7 | RC=52.1 | F1=50.7     tst: ACC=50.1 | PR=53.6 | RC=50.1 | F1=46.5
xgb100-mx12-ff0.1
trn: ACC=50.2 | PR=87.4 | RC=50.2 | F1=47.0     tst: ACC=50.1 | PR=67.5 | RC=50.1 | F1=46.1
xgb300-mx12-ff0.1
trn: ACC=51.0 | PR=83.8 | RC=51.0 | F1=48.7     tst: ACC=50.4 | PR=63.1 | RC=50.4 | F1=47.0
xgb100-mx12-ff0.3
trn: ACC=53.8 | PR=92.0 | RC=53.8 | F1=53.9     tst: ACC=50.2 | PR=54.5 | RC=50.2 | F1=46.8
xgb300-mx12-ff0.3
trn: ACC=59.1 | PR=92.9 | RC=59.1 | F1=62.5     tst: ACC=50.2 | PR=52.0 | RC=50.2 | F1=47.3
xgb100-mx12-ff0.5
trn: ACC=58.9 | PR=92.5 | RC=58.9 | F1=62.2     tst: ACC=50.0 | PR=49.4 | RC=50.0 | F1=46.5
xgb300-mx12-ff0.5
trn: ACC=68.5 | PR=94.4 | RC=68.5 | F1=74.7     tst: ACC=49.9 | PR=49.4 | RC=49.9 | F1=47.2
xgb100-mx12-ff0.7
trn: ACC=64.1 | PR=94.3 | RC=64.1 | F1=69.5     tst: ACC=50.1 | PR=50.7 | RC=50.1 | F1=47.1
xgb300-mx12-ff0.7
trn: ACC=75.7 | PR=95.4 | RC=75.7 | F1=82.0     tst: ACC=50.3 | PR=51.1 | RC=50.3 | F1=48.3
xgb100-mx12-ff0.9
trn: ACC=67.3 | PR=94.1 | RC=67.3 | F1=73.3     tst: ACC=50.2 | PR=51.4 | RC=50.2 | F1=47.6
xgb300-mx12-ff0.9
trn: ACC=80.5 | PR=96.1 | RC=80.5 | F1=86.2     tst: ACC=50.5 | PR=51.7 | RC=50.5 | F1=48.8
af_100_mice_brf

trn: ACC=56.0 | PR=52.6 | RC=56.0 | F1=45.4     tst: ACC=53.7 | PR=51.9 | RC=53.7 | F1=46.0
af_100_mice_brf
```


## All

```
POP='all'
metid='brf'
To train and evaluate brf...
trn: ACC=81.3 | PR=57.9 | RC=81.3 | F1=52.5     tst: ACC=54.9 | PR=51.6 | RC=54.9 | F1=44.1

metid='rusbooster'
To train and evaluate rusbooster...
trn: ACC=61.0 | PR=53.2 | RC=61.0 | F1=49.8     tst: ACC=53.1 | PR=51.1 | RC=53.1 | F1=46.8

xgb300-mx3-ff0.1
trn: ACC=0.50 | PR=0.91 | RC=0.50 | F1=0.48     tst: ACC=0.50         | PR=0.72 | RC=0.50 | F1=0.46
xgb100-mx3-ff0.3
trn: ACC=0.50 | PR=0.94 | RC=0.50 | F1=0.47     tst: ACC=0.50         | PR=0.42 | RC=0.50 | F1=0.46
xgb300-mx3-ff0.3
trn: ACC=0.51 | PR=0.92 | RC=0.51 | F1=0.49     tst: ACC=0.50         | PR=0.52 | RC=0.50 | F1=0.46
xgb100-mx3-ff0.5
trn: ACC=0.50 | PR=0.94 | RC=0.50 | F1=0.47     tst: ACC=0.50         | PR=0.67 | RC=0.50 | F1=0.46
xgb300-mx3-ff0.5
trn: ACC=0.52 | PR=0.92 | RC=0.52 | F1=0.50     tst: ACC=0.50         | PR=0.61 | RC=0.50 | F1=0.46
xgb100-mx3-ff0.7
trn: ACC=0.50 | PR=0.94 | RC=0.50 | F1=0.47     tst: ACC=0.50         | PR=0.42 | RC=0.50 | F1=0.46
xgb300-mx3-ff0.7
trn: ACC=0.52 | PR=0.92 | RC=0.52 | F1=0.51     tst: ACC=0.50         | PR=0.63 | RC=0.50 | F1=0.47
xgb100-mx3-ff0.9
trn: ACC=0.50 | PR=0.94 | RC=0.50 | F1=0.48     tst: ACC=0.50         | PR=0.76 | RC=0.50 | F1=0.46
xgb300-mx3-ff0.9
trn: ACC=0.52 | PR=0.93 | RC=0.52 | F1=0.51     tst: ACC=0.50         | PR=0.52 | RC=0.50 | F1=0.46
xgb100-mx12-ff0.1
trn: ACC=0.51 | PR=0.90 | RC=0.51 | F1=0.48     tst: ACC=0.50         | PR=0.47 | RC=0.50 | F1=0.46
xgb300-mx12-ff0.1
trn: ACC=0.53 | PR=0.91 | RC=0.53 | F1=0.53     tst: ACC=0.50         | PR=0.52 | RC=0.50 | F1=0.47
xgb100-mx12-ff0.3
trn: ACC=0.55 | PR=0.92 | RC=0.55 | F1=0.56     tst: ACC=0.50         | PR=0.53 | RC=0.50 | F1=0.47
```

