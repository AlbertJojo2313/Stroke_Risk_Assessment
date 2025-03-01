# Top Priority (Essential for Stroke Risk Assessment)

## Demographics & Anthropometrics:
- HTM4 (Height in meters)
- BMI
- _SEX (Calculated Sex variable)
- Age (if available in dataset)

## Pre-existing Conditions (Heart, Stroke, & Diabetes):
- CVDSTRK3 (Ever told had a stroke)
- BPHIGH6 (Ever told had high blood pressure)
- BPMEDS1 (Currently taking prescription medicine for high blood pressure)
- TOLDHI3 (Ever told cholesterol is high)
- CHOLMED3 (Currently taking cholesterol medicine)
- CVDINFR4 (Ever told had heart attack)
- CVDCRHD4 (Ever told had coronary heart disease/angina)
- DIABETE4 (Ever told had diabetes)
- PREDIAB2 (Ever told had prediabetes)
- DIABTYPE (Type of diabetes)
- INSULIN1 (Currently taking insulin)
- _RFHYPE6 (High blood pressure diagnosis)
- _RFCHOL3 (High cholesterol diagnosis)
- _MICHD (Coronary heart disease or myocardial infarction history)

## Lifestyle & Behavioral Risk Factors:
- _SMOKER3 (Four-level smoking status)
- SMOKDAY2 (Current smoking frequency)
- ECIGNOW2 (E-cigarette use)
- _CURECI2 (Current e-cigarette users)
- MENTCIGS (Menthol cigarette use)
- MENTECIG (Menthol e-cigarette use)
- AVEDRNK3 (Average drinks per drinking day)
- _RFBING6 (Binge drinking status)
- _RFDRHV8 (Heavy drinking status)

## Physical Activity & Exercise:
- _PACAT3 (Physical activity categories)

## Social & Economic Factors:
- MARITAL (Marital status)
- EMPLOY1 (Employment status)
- INCOME3 (Annual household income) (Maybe)
- RENTHOM1 (Own or rent home)
- VETERAN3 (Military service history)


# Secondary Priority (Mental Health, COVID, Additional Factors)

## Mental Health & Stress:
- LSATISFY (Life satisfaction)
- EMTSUPPRT (Social/emotional support frequency)
- SDLONELY (Frequency of loneliness)
- SDHSTRE1 (Stress frequency in past 30 days)

## General & Physical Health:

### COVID-19 Factors:
- COVIDPO1 (Ever tested positive for COVID-19)
- COVIDVA1 (Received at least one COVID-19 vaccine)
- COVIDNU2 (Total COVID-19 vaccinations received)

### Marijuana Use (Consolidated into one feature):
- MARIJAN1 (Days used in past 30 days)
- MARJSMOK, MARJEAT, MARJVAPE, MARJDAB, MARJOTHR (Modes of use)


# Lower Priority (Race, Metropolitan, Calculated Values, Health Insurance, Other Tests)

## Race & Discrimination in Healthcare:
- _IMPRACE (Imputed race/ethnicity value)


## Geographical & Socioeconomic Context:
- _METSTAT (Metropolitan status)
- _URBSTAT (Urban/Rural status)

## Health Insurance Coverage:
- _HLTHPL1 (Has any health insurance)

## Additional Medical & Screening Factors:
- LCSNUMCG (Cigarettes per day when smoking)
- ASPIRIN (Frequency of aspirin use for heart disease prevention)
