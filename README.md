# survival

[site under construction]

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
