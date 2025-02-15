import os
import pandas as pd

# Set the data folder path (can be changed easily)
FILE_PATH = os.path.expanduser("~/DataScience_Projects/Stroke_Risk_Assessment/data")

def open_files(file_path):


    """Loads CSV files into DataFrames with optimized dtypes."""
    datasets = ["kaggle_stroke.csv", "brfss_2023.csv"]
    dfs = []

    for dataset in datasets:
        full_path = os.path.join(file_path, dataset)
        if not os.path.exists(full_path):
            print(f"⚠️ Warning: File {dataset} not found!")
            dfs.append(None)
            continue
        
        try:
            df = pd.read_csv(full_path, dtype=str)  # Load as string for memory efficiency
            dfs.append(df)
        except Exception as e:
            print(f"❌ Error loading {dataset}: {e}")
            dfs.append(None)

    return dfs  # Returns [kaggle_df, heart_disease_df, brfss_df]

def preprocess_data():
    """Preprocesses data by dropping unnecessary columns and optimizing dtypes."""
    kaggle_df, brfss_df = open_files(FILE_PATH)

    # Drop unwanted columns safely (only if DataFrame is loaded)
    if kaggle_df is not None:
        kaggle_df.drop(columns=['id', 'Residence_type'], inplace=True, errors='ignore')
        kaggle_df = kaggle_df.astype({'age': 'int32', 'bmi': 'float32'}, errors='ignore')  # Optimize types

    ##Brfss_cols
    columns_to_keep = [
        'HTM4', 'BMI', 'CVDSTRK3', 'BPHIGH6', 'BPMEDS1', 'TOLDHI3', 'CHOLMED3', 'CVDINFR4', 
        'CVDCRHD4', 'DIABETE4', 'PREDIAB2', 'DIABTYPE', 'INSULIN1', '_RFHYPE6', '_RFCHOL3', '_MICHD',
        '_SMOKER', 'SMOKE100', 'SMOKEDAY2', 'USENOW3', 'ECIGNOW2', '_CURECI2', 'STOPSMK2', 'MENTCIGS', 
        'MENTECIG', 'ALCDAY4', 'AVEDRNK3', 'DRNK3GE5', 'MAXDRNKS', 'DRNKANY6', '_RFBING6', '_RFDRHV8',
        '_TOTINDA', 'PA3MIN', 'PA3VIGM_', '_PACAT3', 'MARITAL', 'EMPLOY1', 'INCOME3', 'RENTHOM1',
        'VETERAN3', 'LSATISFY', 'EMTSUPPRT', 'SDLONELY', 'SDHSTRE1', 'GENHLTH', 'PHYSHLTH', 'POORHLTH',
        'COVIDPO1', 'COVIDVA1', 'COVIDNU2', 'MARIJANI', 'RRCLASS3', 'RRHCARE4', '_IMPRACE', '_RACEGR3',
        '_RACEPRV', '_METSTAT', '_URBSTAT', 'MSCODE', '_HLTHPL1', '_HCVU653', 'LCSNUMCG', 'LCSCTSC1',
        'LCSSCNCR', 'CRGVPRB3', 'ASPIRIN', '_LLCPWT'
    ]
    if brfss_df is not None:
        brfss_df = brfss_df.filter(items=columns_to_keep)
    return kaggle_df, brfss_df

def main():
    """Runs the preprocessing pipeline and prints dataset info."""
    kaggle_df, brfss_df = preprocess_data()

    datasets = {
        "Kaggle Stroke Dataset": kaggle_df,
        "BRFSS Dataset": brfss_df
    }

    for name, df in datasets.items():
        if df is not None:
            print(f"\n✅ {name}:")
            print(f"Shape: {df.shape}")
            print(f"Columns: {list(df.columns)}\n")
        else:
            print(f"\n❌ {name} is missing or could not be processed.\n")

if __name__ == "__main__":
    main()
