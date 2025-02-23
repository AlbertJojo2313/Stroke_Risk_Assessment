BASE_MAPPING = {
    7: "Don't know/Not sure",
    9: "Refused",
    None: "NA"
}

VALUE_TABLES = {
    # --- Cardiovascular ---
    'CVDSTRK3': {
        1: 'Yes',
        2: 'No',
        **BASE_MAPPING
    },
    'BPHIGH6': {
        1: 'Yes',
        2: 'Yes (gestational)',
        3: 'No',
        4: 'Told borderline',
        **BASE_MAPPING
    },
    'BPMEDS1': {
        1: 'Yes',
        2: 'No',
        **BASE_MAPPING
    },

    # --- Cholesterol ---
    'TOLDHI3': {
        1: 'Yes',
        2: 'No',
        **BASE_MAPPING
    },
    'CHOLMED3': {
        1: 'Yes',
        2: 'No',
        **BASE_MAPPING
    },

    # --- Diabetes ---
    'PREDIAB2': {
        1: 'Yes',
        2: 'Yes (gestational)',
        3: 'No',
        **BASE_MAPPING
    },
    'DIABETE4': {
        1: 'Yes',
        2: 'Yes (gestational)',
        3: 'No',
        4: 'Prediabetes',
        **BASE_MAPPING
    },

    # --- Risk Factors ---
    '_RFHYPE6': {
        1: 'No',
        2: 'Yes',
        **BASE_MAPPING
    },
    '_RFCHOL3': {
        1: 'No',
        2: 'Yes',
        **BASE_MAPPING  # Fixed missing comma
    },

    # --- Tobacco/Substances ---
    '_SMOKER3': {
        1: 'Current everyday',
        2: 'Current some-day',
        3: 'Former',
        4: 'Never',
        **BASE_MAPPING  # Fixed missing comma
    },
    'SMOKDAY2': {
        1: 'Every day',
        2: 'Some days',
        3: 'Not at all',
        **BASE_MAPPING
    },

    # --- Alcohol ---
    '_RFBING6': {
        1: 'No',
        2: 'Yes',
        **BASE_MAPPING
    },

    # --- Physical Activity ---
    '_PACAT3': {
        1: 'Highly active',
        2: 'Active',
        3: 'Insufficiently active',
        4: 'Inactive',
        **BASE_MAPPING
    },

    # --- Demographics ---
    'MARITAL': {
        1: 'Married',
        2: 'Divorced',
        3: 'Widowed',
        4: 'Separated',
        5: 'Never married',
        6: 'Unmarried couple',
        **BASE_MAPPING
    },
    'EMPLOY1': {
        1: 'Employed',
        2: 'Self-employed',
        3: 'Unemployed (1+ years)',
        4: 'Unemployed (<1 year)',
        5: 'Homemaker',
        6: 'Student',
        7: 'Retired',
        8: 'Unable to work',
        **BASE_MAPPING
    },
    'INCOME3': {
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
        None: 'NA',
    },
    'RENTHOM1': {
        1: 'Own',
        2: 'Rent',
        3: 'Other',
        **BASE_MAPPING
    },
    'VETERAN3': {
        1: 'Yes',
        2: 'No',
        **BASE_MAPPING
    },

    # --- Mental Health ---
    'LSATISFY': {
        1: 'Very satisfied',
        2: 'Satisfied',
        3: 'Dissatisfied',
        4: 'Very dissatisfied',
        **BASE_MAPPING
    },

    # --- COVID ---
    'COVIDPO1': {
        1: 'Yes',
        2: 'No',
        **BASE_MAPPING
    },

    # --- Demographics ---
    '_IMPRACE': {
        1: 'White',
        2: 'Black',
        3: 'Asian',
        4: 'Native American',
        5: 'Hispanic',
        6: 'Other'
    },

    # --- Healthcare ---
    '_HLTHPL1': {
        1: 'Yes',
        2: 'No',
        **BASE_MAPPING
    },

    # --- Medications ---
    'ASPIRIN': {
        1: 'Daily',
        2: 'Some days',
        3: 'Former user',
        4: 'Non-user',
        **BASE_MAPPING
    }
}
# Convert all keys to strings in the VALUE_TABLES dictionary
VALUE_TABLES = {col: {str(key): value for key, value in mapping.items()} 
                for col, mapping in VALUE_TABLES.items()}