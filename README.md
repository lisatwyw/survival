# survival

[site under construction]

## Databases

- [e-ICU](eicu/readme.md)


<details>
<summary>MIMIC IV</summary>
 
  
### ```Procedural codes```

```  
DxCodes.loc[DxCodes.long_title.str.contains('atrial fib',case=False ) ]
  
[empty]  
```  
  
```
DxCodes.loc[DxCodes.long_title.str.contains('cathe',case=False ) ]

      icd_code  icd_version                                         long_title
2080      0102            9  Ventriculopuncture through previously implante...
2099      0126            9  Insertion of catheter(s) into cranial cavity o...
2100      0127            9  Removal of catheter(s) from cranial cavity or ...
2101      0128            9  Placement of intracerebral catheter(s) via bur...
8818      0390            9  Insertion of catheter into spinal canal for in...
73102     3404            9     Insertion of intercostal catheter for drainage
73224     3721            9                Right heart cardiac catheterization
73225     3722            9                 Left heart cardiac catheterization
73226     3723            9  Combined right and left heart cardiac catheter...
73229     3726            9  Catheter based invasive electrophysiologic tes...
73357     3891            9                           Arterial catheterization
73358     3892            9                     Umbilical vein catheterization
73359     3893            9   Venous catheterization, not elsewhere classified
73361     3895            9          Venous catheterization for renal dialysis
73362     3897            9    Central venous catheter placement with guidance
74708     4444            9  Transcatheter embolization for gastric or duod...
75418     5201            9            Drainage of pancreatic cyst by catheter
75629     5794            9           Insertion of indwelling urinary catheter
75630     5795            9         Replacement of indwelling urinary catheter
75674      598            9                           Ureteral catheterization
77149     8855            9     Coronary arteriography using a single catheter
77150     8856            9         Coronary arteriography using two catheters
77707     9646            9   Irrigation of ureterostomy and ureteral catheter
77709     9648            9    Irrigation of other indwelling urinary catheter
77717     9657            9                    Irrigation of vascular catheter
77718     9658            9                       Irrigation of wound catheter
77733     9715            9                      Replacement of wound catheter
77764     9762            9  Removal of ureterostomy tube and ureteral cath...
```
  
```  
DxCodes.loc[DxCodes.long_title.str.contains('atrial',case=False ) ]
  
      icd_code  icd_version                                         long_title
4144   02550ZZ           10        Destruction of Atrial Septum, Open Approach
4145   02553ZZ           10  Destruction of Atrial Septum, Percutaneous App...
4146   02554ZZ           10  Destruction of Atrial Septum, Percutaneous End...
4150   02570ZK           10  Destruction of Left Atrial Appendage, Open App...
4152   02573ZK           10  Destruction of Left Atrial Appendage, Percutan...
4154   02574ZK           10  Destruction of Left Atrial Appendage, Percutan...
4613   02B50ZX           10  Excision of Atrial Septum, Open Approach, Diag...
4614   02B50ZZ           10           Excision of Atrial Septum, Open Approach
4615   02B53ZX           10  Excision of Atrial Septum, Percutaneous Approa...
4616   02B53ZZ           10   Excision of Atrial Septum, Percutaneous Approach
4617   02B54ZX           10  Excision of Atrial Septum, Percutaneous Endosc...
4618   02B54ZZ           10  Excision of Atrial Septum, Percutaneous Endosc...
4625   02B70ZK           10   Excision of Left Atrial Appendage, Open Approach
4628   02B73ZK           10  Excision of Left Atrial Appendage, Percutaneou...
4631   02B74ZK           10  Excision of Left Atrial Appendage, Percutaneou...
4776   02C50ZZ           10  Extirpation of Matter from Atrial Septum, Open...
4777   02C53ZZ           10  Extirpation of Matter from Atrial Septum, Perc...
4778   02C54ZZ           10  Extirpation of Matter from Atrial Septum, Perc...
5169   02L70CK           10  Occlusion of Left Atrial Appendage with Extral...
5170   02L70DK           10  Occlusion of Left Atrial Appendage with Intral...
5171   02L70ZK           10  Occlusion of Left Atrial Appendage, Open Approach
5172   02L73CK           10  Occlusion of Left Atrial Appendage with Extral...
5173   02L73DK           10  Occlusion of Left Atrial Appendage with Intral...
5174   02L73ZK           10  Occlusion of Left Atrial Appendage, Percutaneo...
5175   02L74CK           10  Occlusion of Left Atrial Appendage with Extral...
5176   02L74DK           10  Occlusion of Left Atrial Appendage with Intral...
5177   02L74ZK           10  Occlusion of Left Atrial Appendage, Percutaneo...
5267   02N50ZZ           10               Release Atrial Septum, Open Approach
5268   02N53ZZ           10       Release Atrial Septum, Percutaneous Approach
5269   02N54ZZ           10  Release Atrial Septum, Percutaneous Endoscopic...
5426   02Q50ZZ           10                Repair Atrial Septum, Open Approach
5427   02Q53ZZ           10        Repair Atrial Septum, Percutaneous Approach
5428   02Q54ZZ           10  Repair Atrial Septum, Percutaneous Endoscopic ...
5511   02R507Z           10  Replacement of Atrial Septum with Autologous T...
5512   02R508Z           10  Replacement of Atrial Septum with Zooplastic T...
5513   02R50JZ           10  Replacement of Atrial Septum with Synthetic Su...
5514   02R50KZ           10  Replacement of Atrial Septum with Nonautologou...
5515   02R547Z           10  Replacement of Atrial Septum with Autologous T...
5516   02R548Z           10  Replacement of Atrial Septum with Zooplastic T...
5517   02R54JZ           10  Replacement of Atrial Septum with Synthetic Su...
5518   02R54KZ           10  Replacement of Atrial Septum with Nonautologou...
5723   02T50ZZ           10          Resection of Atrial Septum, Open Approach
5724   02T53ZZ           10  Resection of Atrial Septum, Percutaneous Approach
5725   02T54ZZ           10  Resection of Atrial Septum, Percutaneous Endos...
5793   02U507Z           10  Supplement Atrial Septum with Autologous Tissu...
5794   02U508Z           10  Supplement Atrial Septum with Zooplastic Tissu...
5795   02U50JZ           10  Supplement Atrial Septum with Synthetic Substi...
5796   02U50KZ           10  Supplement Atrial Septum with Nonautologous Ti...
5797   02U537Z           10  Supplement Atrial Septum with Autologous Tissu...
5798   02U538Z           10  Supplement Atrial Septum with Zooplastic Tissu...
5799   02U53JZ           10  Supplement Atrial Septum with Synthetic Substi...
5800   02U53KZ           10  Supplement Atrial Septum with Nonautologous Ti...
5801   02U547Z           10  Supplement Atrial Septum with Autologous Tissu...
5802   02U548Z           10  Supplement Atrial Septum with Zooplastic Tissu...
5803   02U54JZ           10  Supplement Atrial Septum with Synthetic Substi...
5804   02U54KZ           10  Supplement Atrial Septum with Nonautologous Ti...
6197   02W50JZ           10  Revision of Synthetic Substitute in Atrial Sep...
6198   02W54JZ           10  Revision of Synthetic Substitute in Atrial Sep...
73168     3541            9       Enlargement of existing atrial septal defect
73171     3551            9  Repair of atrial septal defect with prosthesis...
73172     3552            9  Repair of atrial septal defect with prosthesis...
73177     3561            9   Repair of atrial septal defect with tissue graft
73181     3571            9  Other and unspecified repair of atrial septal ...
73188     3591            9         Interatrial transposition of venous return
73238     3736            9  Excision, destruction, or exclusion of left at...
73262     3776            9  Replacement of transvenous atrial and/or ventr...
73274     3790            9          Insertion of left atrial appendage device
77868     9961            9                               Atrial cardioversion

```

  
### ```POE```
  
```Poe.field_name.unique()

array(['Admit category', 'Discharge Planning', 'Discharge When',
       'Admit to', 'Code status', 'Consult Status', 'Consult Status Time',
       'Level of Urgency', 'Tubes & Drains type', 'Transfer to',
       'Indication'], dtype=object)
```


### ```admissions.csv.gz.race```
  
      'WHITE', 'OTHER', 'BLACK/AFRICAN AMERICAN', 'UNABLE TO OBTAIN',
       'UNKNOWN', 'WHITE - RUSSIAN', 'PORTUGUESE',
       'WHITE - OTHER EUROPEAN', 'BLACK/CAPE VERDEAN', 'ASIAN',
       'ASIAN - CHINESE', 'HISPANIC/LATINO - DOMINICAN',
       'HISPANIC/LATINO - SALVADORAN', 'HISPANIC/LATINO - PUERTO RICAN',
       'HISPANIC/LATINO - GUATEMALAN', 'ASIAN - SOUTH EAST ASIAN',
       'WHITE - BRAZILIAN', 'HISPANIC OR LATINO',
       'HISPANIC/LATINO - CENTRAL AMERICAN', 'BLACK/AFRICAN',
       'NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER',
       'BLACK/CARIBBEAN ISLAND', 'HISPANIC/LATINO - MEXICAN',
       'PATIENT DECLINED TO ANSWER', 'HISPANIC/LATINO - CUBAN',
       'AMERICAN INDIAN/ALASKA NATIVE', 'MULTIPLE RACE/ETHNICITY',
       'WHITE - EASTERN EUROPEAN', 'ASIAN - KOREAN',
       'HISPANIC/LATINO - HONDURAN', 'ASIAN - ASIAN INDIAN',
       'HISPANIC/LATINO - COLUMBIAN', 'SOUTH AMERICAN'
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
                     
### Other fields:
- Median household adjusted to 2019
- Rural-Urban Continuum code
                     
</details>


  
</details>


## Literature review
### Guha et al. EHJ 2022   
- Objectives: To measure the ```incidence, prevalence, risk factors and mortality outcomes of atrial fibrillation (AF) in a multi-ethnic representative United States cohort of breast cancer patients```
- Model: KM
- ...
  
  
### Lee et al. LDH 2021
- Model:  Survival Quilts
- Variables: ```age, PSA, primary and secondary Gleason grades or grade groups, T stage, total number of biopsy cores examined, and core positivity (number of cores positive for cancer divided by number of cores taken). MRI, comorbidity, and treatment data were not available```  
  

## Colab demos 

| Dataset | Colab demo |
|--|--|
| SUPPORT | [CPH, GBS, RSF, SVM](SDA_SUPPORT_demo.ipynb) |

