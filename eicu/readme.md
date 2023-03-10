### Installation 

```
pip install --no-index tensorflow==2.8 torch==1.13.1 keras==2.8.0
```

### Extracted time-series

```

```

| Varname | Description |
|--|--|
| ```conf.dec_cat```| n=6 | 
| 'apacheadmissiondx'| string of admission diagnosis for patients unit stay e.g.: Pulmonary valve surgery, Chest pain, unknown origin, Restrictive lung disease (i.e., Sarcoidosis, pulmonary fibrosis), etc." |
'gender' | 397 vs 398|
'GCS Total', 
'Eyes', 
'Motor', 
'Verbal' |
| ```conf.dec_num``` | n=13 |
| 'admissionheight',
 'admissionweight',
 'age',
 'Heart Rate',
 'MAP (mmHg)',
 'Invasive BP Diastolic',
 'Invasive BP Systolic',
 'O2 Saturation',
 'Respiratory Rate',
 'Temperature (C)',
 'glucose',
 'FiO2',
 'pH'  |
|'patientunitstayid' | similar to SID |
|'hospitaldischargestatus' | outcome |

### Labnames

```
                                   0
0                             -bands
1                             -basos
2                               -eos
3                            -lymphs
4                             -monos
5                             -polys
6                 24 h urine protein
7           24 h urine urea nitrogen
8                         ALT (SGPT)
9                            ANF/ANA
10                        AST (SGOT)
11                     Acetaminophen
12                   Amikacin - peak
13                 Amikacin - random
14                 Amikacin - trough
15                               BNP
16                               BUN
17                      Base Deficit
18                       Base Excess
19                               CPK
20                            CPK-MB
21                      CPK-MB INDEX
22                               CRP
23                            CRP-hs
24                     Carbamazepine
25                 Carboxyhemoglobin
26   Clostridium difficile toxin A+B
27                       Cyclosporin
28                            Device
29                           Digoxin
30                               ESR
31                                Fe
32                     Fe/TIBC Ratio
33                          Ferritin
34                              FiO2
35                 Gentamicin - peak
36               Gentamicin - random
37               Gentamicin - trough
38                              HCO3
39                               HDL
40                        HIV 1&2 AB
41                    HSV 1&2 IgG AB
42              HSV 1&2 IgG AB titer
43                               Hct
44                               Hgb
45                               LDH
46                               LDL
47                            LPM O2
48         Legionella pneumophila Ab
49                         Lidocaine
50                           Lithium
51                               MCH
52                              MCHC
53                               MCV
54                               MPV
55                     Methemoglobin
56                              Mode
57                              NAPA
58                        O2 Content
59                        O2 Sat (%)
60                     Oxyhemoglobin
61                              PEEP
62                                PT
63                          PT - INR
64                               PTT
65                         PTT ratio
66              Peak Airway/Pressure
67                     Phenobarbital
68                         Phenytoin
69                  Pressure Control
70                  Pressure Support
71                      Procainamide
72                               RBC
73                               RDW
74                         RPR titer
75                  Respiratory Rate
76                              Site
77                  Spontaneous Rate
78                                T3
79                              T3RU
80                                T4
81                              TIBC
82                               TSH
83                                TV
84                  Tacrolimus-FK506
85                       Temperature
86                      Theophylline
87                 Tobramycin - peak
88               Tobramycin - random
89               Tobramycin - trough
90                         Total CO2
91                 Vancomycin - peak
92               Vancomycin - random
93               Vancomycin - trough
94                        Vent Other
95                         Vent Rate
96                       Vitamin B12
97                        WBC x 1000
98               WBC's in body fluid
99      WBC's in cerebrospinal fluid
100       WBC's in pericardial fluid
101        WBC's in peritoneal fluid
102           WBC's in pleural fluid
103          WBC's in synovial fluid
104                   WBC's in urine
105                          albumin
106                   alkaline phos.
107                          ammonia
108                          amylase
109                        anion gap
110                  bedside glucose
111                      bicarbonate
112                          calcium
113                             cd 4
114                         chloride
115                         cortisol
116                       creatinine
117                 direct bilirubin
118                          ethanol
119                       fibrinogen
120                           folate
121                          free T4
122                          glucose
123                    glucose - CSF
124                      haptoglobin
125                  ionized calcium
126                          lactate
127                           lipase
128                        magnesium
129                        myoglobin
130                               pH
131                            paCO2
132                             paO2
133                        phosphate
134                 platelets x 1000
135                        potassium
136                       prealbumin
137                        prolactin
138                    protein - CSF
139                        protein C
140                        protein S
141               reticulocyte count
142                       salicylate
143                    serum ketones
144                 serum osmolality
145                           sodium
146                  total bilirubin
147                total cholesterol
148                    total protein
149                      transferrin
150                    triglycerides
151                     troponin - I
152                     troponin - T
153                        uric acid
154               urinary creatinine
155               urinary osmolality
156                   urinary sodium
157         urinary specific gravity
```


### PatRes
  
```
PatRes[['actualiculos','actualhospitallos','actualhospitalmortality']].head(20)
  
    actualiculos  actualhospitallos actualhospitalmortality
0         2.4972             2.4972                 EXPIRED
1         2.4972             2.4972                 EXPIRED
2         3.3423             9.2167                   ALIVE
3         3.3423             9.2167                   ALIVE
4         1.2979             3.7493                   ALIVE
5         1.2979             3.7493                   ALIVE
6         0.5000             0.4215                   ALIVE
7         0.5000             0.4215                   ALIVE
8         1.1472             1.8861                   ALIVE
9         1.1472             1.8861                   ALIVE
10       10.8923            15.9313                   ALIVE
11       10.8923            15.9313                   ALIVE
12        2.6631            13.7771                   ALIVE
13        2.6631            13.7771                   ALIVE
14        0.7451             1.3174                   ALIVE
15        0.7451             1.3174                   ALIVE
16        4.2138            11.1931                   ALIVE
17        4.2138            11.1931                   ALIVE
18        1.0423             7.7542                   ALIVE
19        1.0423             7.7542                   ALIVE
```
  
```
PatRes.physicianspeciality.unique()

array(['critical care medicine (CCM)', 'hospitalist', 'internal medicine',
       'surgery-cardiac', 'Specialty Not Specified', 'family practice',
       'cardiology', 'other', 'pulmonary/CCM', 'surgery-general',
       'pulmonary', 'surgery-trauma', 'unknown', 'surgery-neuro',
       'orthopedics', 'infectious disease', 'rheumatology', 'nurse',
       'neurology', 'surgery-vascular', 'hematology/oncology',
       'gastroenterology', 'otolaryngology', 'obstetrics/gynecology',
       'emergency medicine', 'surgery-transplant', 'surgery-plastic',
       'urology', 'surgery-critical care', 'nephrology', 'oncology',
       'ethics', 'surgery-orthopedic', 'radiology', 'surgery-oral',
       'anesthesiology/CCM', 'ophthalmology', 'hematology', 'dermatology',
       'psychiatry', 'surgery-otolaryngology head & neck',
       'allergy/immunology', 'endocrinology', 'anesthesiology',
       'physical medicine/rehab', 'surgery-pediatric',
       'nurse practitioner', 'respiratory therapist'], dtype=object) 
```  
  
  
### ```NursingCharts```

|Field name | Size | Notes |
|--|--|--|
|```nursingchartid```|151,604,232 | unique data entry ID |

  
  
<details>
<summary>Labels & example values</summary>  

```
ArtMAP                      88.000000   48.000000
BedsideGlucose                    NaN         NaN
Best_eye                          NaN         NaN
Best_motor                        NaN         NaN
Best_verbal                       NaN         NaN
CI                                NaN         NaN
CO                                NaN         NaN
CPP                               NaN         NaN
CV/PV                             NaN         NaN
CVP                               NaN         NaN
CVP(mmHg)                   32.000000         NaN
Delirium                          NaN         NaN
ECG                               NaN         NaN
ECMO                              NaN         NaN
ElectrolyteReplace                NaN         NaN
EndTidalCO2                       NaN         NaN
EyeOpen                           NaN    4.000000
EENTAsess                         NaN         NaN
FallRisk                          NaN         NaN
Gastro                            NaN         NaN
Geni                              NaN         NaN
GlasgowComa                       NaN   15.000000
HR                         140.000000  104.000000
IAP                               NaN         NaN
ICP                               NaN         NaN
Impella                           NaN         NaN
Int                               NaN         NaN
InvasiveBP                  62.000000   84.000000
LVAD                              NaN         NaN
LevelAssist                       NaN         NaN
MAP(mmHg)                   67.000000         NaN
MSA                               NaN         NaN
Motor                             NaN    6.000000
Musculo                           NaN         NaN
Neuro                             NaN         NaN
NoninvasiveBP               59.000000  131.000000
O2Admin                           NaN         NaN
O2(L/%)                      2.000000         NaN
O2                          94.000000  100.000000
PO                                NaN         NaN
PA                                NaN         NaN
PAOP                              NaN         NaN
PVR                               NaN         NaN
PVRI                              NaN         NaN
Pain                              NaN         NaN
PainPresent                       NaN         NaN
PainScore                    0.000000    0.000000
PatientRest                  2.000000    0.000000
Pulse                             NaN         NaN
PulseOxMode                       NaN         NaN
RASS                              NaN         NaN
Resp                              NaN         NaN
RespRate                    22.000000   18.000000
SedationScore                     NaN         NaN
SV                                NaN         NaN
SVO2                              NaN         NaN
SVR                               NaN         NaN
SVRI                              NaN         NaN
ScoreGlasgowComaScale             NaN         NaN
SedationScale                     NaN         NaN
SpO2                              NaN         NaN
SympDelirium                      NaN         NaN
Temp                        97.000000         NaN
Verbal                            NaN    5.000000
ArtMAP_hrs                  35.100000   10.950000
BedsideGlucose_hrs                NaN         NaN
Best_eye_hrs                      NaN         NaN
Best_motor_hrs                    NaN         NaN
Best_verbal_hrs                   NaN         NaN
CI_hrs                            NaN         NaN
CO_hrs                            NaN         NaN
CPP_hrs                           NaN         NaN
CV/PV_hrs                    0.350000  -12.416667
CVP_hrs                           NaN         NaN
CVP(mmHg)_hrs               34.100000         NaN
Delirium_hrs                      NaN         NaN
ECG_hrs                           NaN         NaN
ECMO_hrs                          NaN         NaN
ElectrolyteReplace_hrs            NaN         NaN
EndTidalCO2_hrs                   NaN         NaN
EyeOpen_hrs                       NaN   14.700000
EENTAsess_hrs                0.350000  -12.416667
FallRisk_hrs                      NaN         NaN
Gastro_hrs                   0.350000  -15.700000
Geni_hrs                     0.350000  -15.683333
GlasgowComa_hrs                   NaN   14.700000
HR_hrs                       0.100000  -15.983333
IAP_hrs                           NaN         NaN
ICP_hrs                           NaN         NaN
Impella_hrs                       NaN         NaN
Int_hrs                      0.350000  -12.416667
InvasiveBP_hrs              35.100000   10.950000
LVAD_hrs                          NaN         NaN
LevelAssist_hrs              0.533333  -12.300000
MAP(mmHg)_hrs                0.100000         NaN
MSA_hrs                      0.350000  -12.416667
Motor_hrs                         NaN   14.700000
Musculo_hrs                  0.350000  -12.416667
Neuro_hrs                    0.350000  -12.416667
NoninvasiveBP_hrs            0.100000  -15.983333
O2Admin_hrs                  8.550000         NaN
O2(L/%)_hrs                  8.550000         NaN
O2_hrs                       0.350000  -15.983333
PO_hrs                            NaN         NaN
PA_hrs                            NaN         NaN
PAOP_hrs                          NaN         NaN
PVR_hrs                           NaN         NaN
PVRI_hrs                          NaN         NaN
Pain_hrs                     0.350000  -15.966667
PainPresent_hrs                   NaN         NaN
PainScore_hrs                0.350000  -12.416667
PatientRest_hrs              0.350000  -12.416667
Pulse_hrs                         NaN         NaN
PulseOxMode_hrs              0.100000  -12.950000
RASS_hrs                          NaN         NaN
Resp_hrs                     0.350000  -15.716667
RespRate_hrs                 8.550000  -15.983333
SedationScore_hrs                 NaN         NaN
SV_hrs                            NaN         NaN
SVO2_hrs                          NaN         NaN
SVR_hrs                           NaN         NaN
SVRI_hrs                          NaN         NaN
ScoreGlasgowComaScale_hrs         NaN         NaN
SedationScale_hrs                 NaN         NaN
SpO2_hrs                          NaN         NaN
SympDelirium_hrs            28.966667  -12.416667
Temp_hrs                     5.850000  -15.983333
Verbal_hrs                        NaN   14.700000
```
  
  
</details>
  
  
  

```
13                        Arterial Line MAP (mmHg)
31                                 Bedside Glucose
60                               Best Eye Response
56                             Best Motor Response
57                            Best Verbal Response
30                                              CI
40                                              CO
42                                             CPP
20                               CV/ PV Assessment
35                                             CVP
14                                      CVP (mmHg)
36                            Delirium Scale/Score
52                                      ECG (secs)
64                                            ECMO
51                         Electrolyte Replacement
33                                   End Tidal CO2
29                                     Eye Opening
22               Eye, Ear, Nose, Throat Assessment
54                                       Fall Risk
10                     Gastrointestinal Assessment
2                         Genitourinary Assessment
26                              Glasgow coma score
1                                       Heart Rate
53                                             IAP
43                                             ICP
49                                         Impella
3                         Integumentary Assessment
11                                     Invasive BP
50                                            LVAD
6                              Level of Assistance
8                                       MAP (mmHg)
0                         Mental Status Assessment
28                                  Motor Response
9                       Musculoskeletal Assessment
16                         Neurological Assessment
17                                 Non-Invasive BP
23                                 O2 Admin Device
25                                          O2 L/%
5                                    O2 Saturation
48                                            P.O.
41                                              PA
44                                            PAOP
32                                             PVR
47                                            PVRI
24                                 Pain Assessment
62                                    Pain Present
21                                 Pain Score/Goal
18  Patient s Comfort/Function (Pain) GOAL At Rest
58                                           Pulse
4                                   Pulse Ox  Mode
59                                            RASS
15                          Respiratory Assessment
12                                Respiratory Rate
63                                  SEDATION SCORE
38                                              SV
45                                            SVO2
39                                             SVR
46                                            SVRI
61                      Score (Glasgow Coma Scale)
37                       Sedation Scale/Score/Goal
55                                            SpO2
7                     Symptoms of Delirium Present
19                                     Temperature
27                                 Verbal Response
34                                             NaN
```

  
### ```diedinhospital``` vs ```actualicumortality```
```
sum( joined.diedinhospital.isnull()  )
10798
sum( joined.actualicumortality.isnull()  )
30126
sum( joined.diedinhospital.isnull() |  joined.actualicumortality.isnull() )
30126
```


  
### pastHistory of AF 
```
  {'Hx_AS': 229,
 'Hx_renal failure- not currently dialyzed': 16,
 'Hx_CHF - class II': 26,
 'Hx_Performed': 480,
 'Hx_hypertension requiring treatment': 342,
 'Hx_atrial fibrillation - chronic': 363,
 'Hx_CHF - severity unknown': 14,
 'Hx_AICD': 27,
 'Hx_COPD  - no limitations': 40,
 'Hx_rheumatoid arthritis': 11,
 "Hx_Cushing's syndrome": 1,
 'Hx_CHF': 188,
 'Hx_DVT - date unknown': 27,
 'Hx_atrial fibrillation - intermittent': 94,
 'Hx_renal insufficiency - baseline creatinine unknown': 27,
 'Hx_MR': 34,
 'Hx_unknown pacer': 44,
 'Hx_s/p MVR': 15,
 'Hx_hypothyroidism': 79,
 'Hx_COPD  - moderate': 52,
 'Hx_CABG - date unknown': 49,
 'Hx_s/p AVR': 22,
 'Hx_home oxygen': 27,
 'Hx_COPD  - severe': 29,
 'Hx_procedural coronary intervention - date unknown': 32,
 'Hx_renal insufficiency - creatinine 1-2': 32,
 'Hx_non-medication dependent': 31,
 'Hx_MI - date unknown': 33,
 'Hx_CHF - class III': 9,
 'Hx_MS': 3,
 'Hx_stroke - within 2 years': 3,
 'Hx_procedural coronary intervention - remote': 10,
 'Hx_medication dependent': 102,
 'Hx_SVT- other': 9,
 'Hx_TR': 883,
 'Hx_AR': 170,
 'Hx_colon': 16,
 'Hx_stroke - date unknown': 39,
 'Hx_renal failure - hemodialysis': 31,
 'Hx_peripheral vascular disease': 38,
 'Hx_asthma': 38,
 'Hx_insulin dependent diabetes': 78,
 'Hx_renal insufficiency - creatinine 2-3': 7,
 'Hx_ovary': 3,
 'Hx_V paced': 7,
 'Hx_other': 37,
 'Hx_stroke - remote': 10,
 'Hx_multiple': 24,
 'Hx_other seizures': 8,
 'Hx_generalized seizures': 7,
 'Hx_dementia': 21,
 'Hx_nodes': 1,
 'Hx_procedural coronary intervention - within 2 years': 5,
 'Hx_peptic ulcer disease with h/o GI bleeding': 9,
 'Hx_procedural coronary intervention - within 5 years': 4,
 'Hx_restrictive pulmonary disease': 2,
 'Hx_breast': 16,
 'Hx_angina': 27,
 'Hx_pulmonary embolism - date unknown': 8,
 'Hx_CHF - class I': 33,
 'Hx_pulmonary embolism - remote': 1,
 'Hx_prostate': 9,
 'Hx_peptic ulcer disease': 31,
 'Hx_ventricular tachycardia': 3,
 'Hx_MI - remote': 14,
 'Hx_CABG - remote': 20,
 'Hx_procedural coronary intervention - within 6 months': 5,
 'Hx_lung': 21,
 'Hx_s/p TVR': 4,
 'Hx_non-Hodgkins lymphoma': 4,
 'Hx_CABG - within 2 years': 2,
 'Hx_UGI bleeding': 1,
 'Hx_MI - within 6 months': 4,
 'Hx_A/V paced': 2,
 'Hx_bladder': 9,
 'Hx_CHF - class IV': 3,
 'Hx_recent steroid use for > 10 days': 1,
 'Hx_respiratory failure - date unknown': 9,
 'Hx_head and neck': 2,
 'Hx_chronic kidney stones': 3,
 'Hx_respiratory failure - within 6 months': 5,
 'Hx_s/p renal transplant': 1,
 'Hx_respiratory failure - within 2 years': 1,
 'Hx_renal failure - peritoneal dialysis': 2,
 'Hx_stroke - within 5 years': 6,
 'Hx_MI - within 2 years': 5,
 'Hx_hyperthyroidism': 1,
 'Hx_other immunosuppressive medications': 1,
 'Hx_chemotherapy within past mo.': 7,
 'Hx_stroke - within 6 months': 5,
 'Hx_CML': 1,
 'Hx_kidney': 7,
 'Hx_respiratory failure - within 5 years': 2,
 'Hx_CABG - within 6 months': 2,
 'Hx_focal seizures': 3,
 'Hx_primary site': 1,
 'Hx_CABG - within 5 years': 5,
 'Hx_esophagus': 2,
 'Hx_DVT - within 6 months': 1,
 'Hx_clotting disorder': 3,
 'Hx_DVT - remote': 4,
 'Hx_hypercoagulable condition': 1,
 'Hx_uterus': 4,
 'Hx_ITP': 1,
 'Hx_Not Obtainable': 3,
 'Hx_ventricular fibrillation': 1,
 'Hx_CLL': 1,
 'Hx_hemolytic anemia': 2,
 'Hx_sick sinus syndrome': 3,
 'Hx_MI - within 5 years': 2,
 'Hx_AML': 1,
 'Hx_DVT - within 5 years': 3,
 'Hx_intracranial mass': 1,
 'Hx_neurogenic bladder': 3,
 'Hx_unknown': 307,
 'Hx_brain': 5,
 'Hx_neuromuscular disease': 3,
 'Hx_clinical diagnosis': 2,
 'Hx_Hodgkins disease': 1,
 'Hx_renal insufficiency - creatinine > 5': 2,
 'Hx_angina - class II': 5,
 'Hx_melanoma': 7,
 'Hx_multiple myeloma': 2,
 'Hx_pulmonary embolism - within 5 years': 2,
 'Hx_leukemia - other': 1,
 'Hx_ventricular ectopy': 1,
 'Hx_FEV1/FVC ratio 51-60': 1,
 'Hx_FEV1 41-50': 1,
 'Hx_DLCO 41-50': 1,
 'Hx_MAT': 11,
 'Hx_HIV positive': 2,
 'Hx_Not Performed': 1,
 'Hx_angina - class I': 6,
 'Hx_angina - class IV': 1,
 'Hx_sickle cell disease': 1}
 ``` 
  
### Dx
```
0	>= 20 mg prednisone per day or equivalent
1	A paced
2	A/V paced
3	AICD
4	AIDS
5	ALL
6	AML
7	AR
8	AS
9	Alkylating agents (bleomycin, cytoxan, cycloph...
10	Anthracyclines (adriamycin, daunorubicin)
11	BMT within past 12 mos.
12	CABG - date unknown
13	CABG - remote
14	CABG - within 2 years
15	CABG - within 5 years
16	CABG - within 6 months
17	CHF
18	CHF - class I
19	CHF - class II
20	CHF - class III
21	CHF - class IV
22	CHF - severity unknown
23	CLL
24	CML
25	COPD - moderate
26	COPD - no limitations
27	COPD - severe
28	Cis-platinum
29	Cushing's syndrome
30	DLCO 31-40
31	DLCO 41-50
32	DLCO 51-60
33	DLCO 61-70
34	DLCO 71-80
35	DLCO <30
36	DLCO >80
37	DVT - date unknown
38	DVT - remote
39	DVT - within 2 years
40	DVT - within 5 years
41	DVT - within 6 months
42	FEV1 31-40
43	FEV1 41-50
44	FEV1 51-60
45	FEV1 61-70
46	FEV1 71-80
47	FEV1 <30
48	FEV1 >80
49	FEV1/FVC ratio 31-40
50	FEV1/FVC ratio 41-50
51	FEV1/FVC ratio 51-60
52	FEV1/FVC ratio 61-70
53	FEV1/FVC ratio 71-80
54	FEV1/FVC ratio <30
55	FEV1/FVC ratio >80
56	FVC 31-40
57	FVC 41-50
58	FVC 51-60
59	FVC 61-70
60	FVC 71-80
61	FVC <30
62	FVC >80
63	HIV positive
64	Hodgkins disease
65	ITP
66	MAT
67	MI - date unknown
68	MI - remote
69	MI - within 2 years
70	MI - within 5 years
71	MI - within 6 months
72	MR
73	MS
74	No Health Problems
75	Not Obtainable
76	Not Performed
77	PS
78	Performed
79	SLE
80	SVT- other
81	TIA(s) - date unknown
82	TIA(s) - remote
83	TIA(s) - within 2 years
84	TIA(s) - within 5 years
85	TIA(s) - within 6 months
86	TR
87	UGI bleeding
88	V paced
89	Vincristine
90	angina
91	angina - class I
92	angina - class II
93	angina - class III
94	angina - class IV
95	angina - severity unknown
96	aplastic anemia
97	ascites
98	asthma
99	atrial fibrillation - chronic
100	atrial fibrillation - intermittent
101	bile duct
102	biopsy proven
103	bladder
104	bone
105	both prednisone and other immunosuppressive me...
106	brain
107	breast
108	carcinomatosis
109	chemotherapy within past 6 mos.
110	chemotherapy within past mo.
111	chronic kidney stones
112	clinical diagnosis
113	clotting disorder
114	colon
115	coma
116	dementia
117	dermatomyositis
118	encephalopathy
119	esophagus
120	essential thrombocytosis
121	excellent - strenuous exercise (>10 mets)
122	focal seizures
123	generalized seizures
124	head and neck
125	hemolytic anemia
126	home oxygen
127	hypercalcemia
128	hypercoagulable condition
129	hypertension requiring treatment
130	hyperthyroidism
131	hypothyroidism
132	insulin dependent diabetes
133	intra-abdominal
134	intracranial mass
135	jaundice
136	kidney
137	leukemia - other
138	limited - household activities (1-4 mets)
139	liver
140	lung
141	medication dependent
142	melanoma
143	moderate - stairs/brisk walking (5-10 mets)
144	multiple
145	multiple myeloma
146	myelofibrosis
147	neurogenic bladder
148	neuromuscular disease
149	nodes
150	non-Hodgkins lymphoma
151	non-medication dependent
152	none
153	none - bed-ridden
154	other
155	other hematologic malignancy
156	other immunosuppressive medications
157	other seizures
158	ovary
159	pancreas - adenocarcinoma
160	pancreas - islet cell
161	peptic ulcer disease
162	peptic ulcer disease with h/o GI bleeding
163	peripheral vascular disease
164	petite mal seizures
165	polycythemia vera
166	primary site
167	procedural coronary intervention - date unknown
168	procedural coronary intervention - remote
169	procedural coronary intervention - within 2 years
170	procedural coronary intervention - within 5 years
171	procedural coronary intervention - within 6 mo...
172	prostate
173	pulmonary embolism - date unknown
174	pulmonary embolism - remote
175	pulmonary embolism - within 2 years
176	pulmonary embolism - within 5 years
177	pulmonary embolism - within 6 months
178	recent steroid use for > 10 days
179	renal failure - hemodialysis
180	renal failure - peritoneal dialysis
181	renal failure- not currently dialyzed
182	renal insufficiency - baseline creatinine unknown
183	renal insufficiency - creatinine 1-2
184	renal insufficiency - creatinine 2-3
185	renal insufficiency - creatinine 3-4
186	renal insufficiency - creatinine 4-5
187	renal insufficiency - creatinine > 5
188	renal tubular acidosis
189	respiratory failure - date unknown
190	respiratory failure - remote
191	respiratory failure - within 2 years
192	respiratory failure - within 5 years
193	respiratory failure - within 6 months
194	restrictive pulmonary disease
195	rheumatoid arthritis
196	s/p AVR
197	s/p MVR
198	s/p TVR
199	s/p heart transplant
200	s/p liver transplant
201	s/p lung transplant
202	s/p renal transplant
203	sarcoidosis
204	sarcoma
205	scleroderma
206	sick sinus syndrome
207	sickle cell disease
208	splenomegaly
209	stomach
210	stroke - date unknown
211	stroke - remote
212	stroke - within 2 years
213	stroke - within 5 years
214	stroke - within 6 months
215	testes
216	unknown
217	unknown pacer
218	uterus
219	varices
220	vasculitis
221	ventricular ectopy
222	ventricular fibrillation
223	ventricular tachycardia
```
