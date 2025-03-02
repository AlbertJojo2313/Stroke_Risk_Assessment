# Central BASE_MAPPING for missing and undefined values
BASE_MAPPING = {
    7: "Don't know/Not sure",
    9: "Refused",
    None: 'NA',
    'Missing': 'Missing'
}

# Function to apply BASE_MAPPING for any column


def apply_base_mapping(mapping):
    return {**mapping, **BASE_MAPPING}


# Updated VALUE_TABLES
VALUE_TABLES = {
    # --- Health Indicators ---
    'HTM4': {None: 'NA'},
    'WEIGHT2': {None: 'NA'},
    '_BMI5CAT': apply_base_mapping({1: "Underweight", 2: "Normal Weight", 3: "Overweight", 4: "Obese"}),

    # --- Cardiovascular ---
    'CVDSTRK3': apply_base_mapping({
        1: 'Yes',
        2: 'No',
    }),
    'BPHIGH6': apply_base_mapping({
        1: 'Yes',
        2: 'Yes (gestational)',
        3: 'No',
        4: 'Told borderline',
    }),
    'BPMEDS1': apply_base_mapping({
        1: 'Yes',
        2: 'No',
    }),

    # --- Cholesterol ---
    'TOLDHI3': apply_base_mapping({
        1: 'Yes',
        2: 'No',
    }),
    'CHOLMED3': apply_base_mapping({
        1: 'Yes',
        2: 'No',
    }),
    'CVDCRHD4': apply_base_mapping({
        1: 'Yes',
        2: 'No',
    }),

    # --- Diabetes ---
    'PREDIAB2': apply_base_mapping({
        1: 'Yes',
        2: 'Yes (gestational)',
        3: 'No',
    }),
    'DIABETE4': apply_base_mapping({
        1: 'Yes',
        2: 'Yes (gestational)',
        3: 'No',
        4: 'Prediabetes',
    }),

    # --- Risk Factors ---
    '_RFHYPE6': apply_base_mapping({
        1: 'No',
        2: 'Yes',
    }),
    '_RFCHOL3': apply_base_mapping({
        1: 'No',
        2: 'Yes',
    }),

    # --- Tobacco/Substances ---
    '_SMOKER3': apply_base_mapping({
        1: 'Current everyday',
        2: 'Current some-day',
        3: 'Former',
        4: 'Never',
    }),
    'SMOKDAY2': apply_base_mapping({
        1: 'Every day',
        2: 'Some days',
        3: 'Not at all',
    }),

    # --- Alcohol ---
    '_RFBING6': apply_base_mapping({
        1: 'No',
        2: 'Yes',
    }),

    # --- Physical Activity ---
    '_PACAT3': apply_base_mapping({
        1: 'Highly active',
        2: 'Active',
        3: 'Insufficiently active',
        4: 'Inactive',
    }),

    # --- Demographics ---
    'MARITAL': apply_base_mapping({
        1: 'Married',
        2: 'Divorced',
        3: 'Widowed',
        4: 'Separated',
        5: 'Never married',
        6: 'Unmarried couple',
    }),
    'EMPLOY1': apply_base_mapping({
        1: 'Employed',
        2: 'Self-employed',
        3: 'Unemployed (1+ years)',
        4: 'Unemployed (<1 year)',
        5: 'Homemaker',
        6: 'Student',
        7: 'Retired',
        8: 'Unable to work',
    }),
    'INCOME3': apply_base_mapping({
        1: '<$10k',
        2: '$10k-$15k',
        3: '$15k-$20k',
        4: '$20k-$25k',
        5: '$25k-$35k',
        6: '$35k-$50k',
        7: '$50k-$75k',
        8: '$75k-$100k',
        9: '$100k-$150k',
        10: '$150k-$200k',
        11: '>$200k',
        77: "Don't know/Not sure",
        99: 'Refused',
    }),
    'RENTHOM1': apply_base_mapping({
        1: 'Own',
        2: 'Rent',
        3: 'Other',
    }),
    'VETERAN3': apply_base_mapping({
        1: 'Yes',
        2: 'No',
    }),

    # --- Mental Health ---
    'LSATISFY': apply_base_mapping({
        1: 'Very satisfied',
        2: 'Satisfied',
        3: 'Dissatisfied',
        4: 'Very dissatisfied',
    }),

    # --- COVID ---
    'COVIDPO1': apply_base_mapping({
        1: 'Yes',
        2: 'No',
    }),

    # --- Race/Ethnicity ---
    '_IMPRACE': {
        1: 'White',
        2: 'Black',
        3: 'Asian',
        4: 'Native American',
        5: 'Hispanic',
        6: 'Other'
    },

    # --- Healthcare ---
    '_HLTHPL1': apply_base_mapping({
        1: 'Yes',
        2: 'No',
    }),

    # --- Medications ---
    'ASPIRIN': apply_base_mapping({
        1: 'Daily',
        2: 'Some days',
        3: 'Former user',
        4: 'Non-user',
    })
}

"""
# Convert all keys to strings in the VALUE_TABLES dictionary
VALUE_TABLES = {col: {str(key): value for key, value in mapping.items()}
                for col, mTpping in VALUE_TABLES.items()}
"""

# Inverts the mapping


def invert_mapping(value_tables):
    inverted_tables = {}
    for column, mapping in value_tables.items():
        inverted_mapping = {v: k for k, v in mapping.items()}
        inverted_tables[column] = inverted_mapping
    return inverted_tables
