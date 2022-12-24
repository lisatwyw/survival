# survival

[site under construction]

<details>
<summary>SEER</summary>

  ## Installation
  - You'll need to complete 2 identical weboforms to obtain separate links for installation files (EXE that can only executed on Windows):
    1. ```ss8_4_0_1.exe``` (SEER*Stat 8.40.1, downloaded on Dec 24, 2022) 
    2. ```sp301.exe``` (SEER*Prep 3.0)

  ## Extract data 

  To obtain patient-level (individualized) data

  1. First, define selection criteria:

    - Click on "table" icon ![image](https://user-images.githubusercontent.com/38703113/209453078-33345bb2-2911-44aa-bc7c-922960cc3b8c.png)
      - ```Selection Tab** is used to define cohort 
      - ```Table Tab** is used to add fields to the dataframe you are about to create

    - Click on "execute" icon ![image](https://user-images.githubusercontent.com/38703113/209453082-81d650f2-c248-450c-8281-d6b732693edc.png) 

  2. To save the extracted data: Matrix > Export > 


<details>
<summary>SEER: meta data</summary>

| Field name | Meta info |
| -- | -- |
| Patient ID | 8-digit, starting from 00000001 | 
| Race recode | White, Black, Other |
| Age recode with <1 year olds | Unknown, 25-29, ..., 40-44,...,55-59, ..., 70-74, .., 85+ years  |
| PRCDA or not | purchased/referred care delivery area? |
| Histologic Type ICD-O-3 | |
| Hist/ behav (ICD-O-3) ||
                     
## Other fields:
- median household adjusted to 2019
- Rural-Urban Continuum code
                     
</details>

  
  
  
</details>


<details>
<summary>Literature review</summary>
</details>


<details>
<summary>Colab demos</summary>

| Dataset | Colab demo |
|--|--|
| SUPPORT | [CPH, GBS, RSF, SVM](SDA_SUPPORT_demo.ipynb) |

</details>
