# survival

[site under construction]

<details>
<summary>e-ICU</summary>

## ```NursingCharts```
|Field name | Size | Notes |
|--|--|--|
|```nursingchartid```|151,604,232 | unique data entry ID |


## ```diedinhospital``` vs ```actualicumortality```
```
sum( joined.diedinhospital.isnull()  )
10798
sum( joined.actualicumortality.isnull()  )
30126
sum( joined.diedinhospital.isnull() |  joined.actualicumortality.isnull() )
30126
```

## pastHistory of AF 
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
  
## Dx
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

</details>

<details>
<summary>SEER</summary>

## Installation
- You'll need to complete 2 identical weboforms to obtain separate links for installation files (EXE that can only executed on Windows):
  1. ```ss8_4_0_1.exe``` (SEER*Stat 8.40.1, downloaded on Dec 24, 2022) 
  2. ```sp301.exe``` (SEER*Prep 3.0)

## Extract data 

### To obtain patient-level (individualized) data

1. First, define selection criteria:

  - Click on "table" icon ![image](https://user-images.githubusercontent.com/38703113/209453078-33345bb2-2911-44aa-bc7c-922960cc3b8c.png)
    - ```Selection Tab** is used to define cohort 
    - ```Table Tab** is used to add fields to the dataframe you are about to create

  - Click on "execute" icon ![image](https://user-images.githubusercontent.com/38703113/209453082-81d650f2-c248-450c-8281-d6b732693edc.png) 

2. To save the extracted data: Matrix > Export > ```CSV```

### To obtain histories of individual patients

1. ```Matrix``` > ```Retrieve session```
2. ```Session``` > ```Person selection```

<details>
<summary>SEER: meta data</summary>


</details>


<details>
<summary>SEER: meta data</summary>

| Field name | Meta info |
| -- | -- |
| Patient ID | 8-digit, starting from 00000001 | 
| Race recode | White, Black, Other |
| Age recode with <1 year olds | Unknown, 25-29, ..., 40-44,...,55-59, ..., 70-74, .., 85+ years  |
| PRCDA or not | purchased/referred care delivery area? |
| Histologic Type ICD-O-3 | 8140; 8070 |
| Hist/ behav (ICD-O-3) | Adeocarcinoma; Squamous cell carcionma  |
| AJCC Stage 3rd ed (1988-2003) | Blank; 10, 32, ... |
| Laterality | Left - origin of primary, Right, bilateral, paired site, ... |
                     
## Other fields:
- Median household adjusted to 2019
- Rural-Urban Continuum code
                     
</details>


  
</details>


<details>
<summary>Literature review</summary>
## Guha et al. EHJ 2022   
- Objectives: To measure the ```incidence, prevalence, risk factors and mortality outcomes of atrial fibrillation (AF) in a multi-ethnic representative United States cohort of breast cancer patients```
- Model: KM
- 
  
  
## Lee et al. LDH 2021
- Model:  Survival Quilts
- Variables: ```age, PSA, primary and secondary Gleason grades or grade groups, T stage, total number of biopsy cores examined, and core positivity (number of cores positive for cancer divided by number of cores taken). MRI, comorbidity, and treatment data were not available```  
  
</details>


<details>
<summary>Colab demos</summary>

| Dataset | Colab demo |
|--|--|
| SUPPORT | [CPH, GBS, RSF, SVM](SDA_SUPPORT_demo.ipynb) |

</details>
