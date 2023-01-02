# eicu

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

