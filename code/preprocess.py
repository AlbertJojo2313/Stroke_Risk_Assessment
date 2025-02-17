import os
import pandas as pd

# Set the data folder path (can be changed easily)
FILE_PATH = os.path.expanduser("~/DataScience_Projects/Stroke_Risk_Assessment/data/Raw")

def open_files(file_path):
    """Loads CSV files into DataFrames with optimized dtypes."""
    dataset = "brfss_2023.csv"
    full_path = os.path.join(file_path, dataset)
    
    if not os.path.exists(full_path):
        print(f"⚠️ Warning: File {dataset} not found!")
        return None
    
    try:
        df = pd.read_csv(full_path, dtype=str)  # Load as string for memory efficiency
        return df
    except Exception as e:
        print(f"❌ Error loading {dataset}: {e}")
        return None

def preprocess_data():
    """Preprocesses data by dropping unnecessary columns and optimizing dtypes."""
    brfss_df = open_files(FILE_PATH)
    
    if brfss_df is None:
        return None

    # Columns to keep
    columns_to_keep = [
        'HTM4', 'BMI', 'CVDSTRK3', 'BPHIGH6', 'BPMEDS1', 'TOLDHI3', 'CHOLMED3', 'CVDINFR4', 
        'CVDCRHD4', 'DIABETE4', 'PREDIAB2', 'DIABTYPE', 'INSULIN1', '_RFHYPE6', '_RFCHOL3', '_MICHD',
        '_SMOKER',  'SMOKEDAY2', 'USENOW3', 'ECIGNOW2', '_CURECI2', 'MENTCIGS', 
        'MENTECIG', 'AVEDRNK3', '_RFBING6', '_RFDRHV8',
        '_PACAT3', 'MARITAL', 'EMPLOY1', 'INCOME3', 'RENTHOM1',
        'VETERAN3', 'LSATISFY', 'EMTSUPPRT', 'SDLONELY', 'SDHSTRE1',
        'COVIDPO1', 'COVIDVA1', 'COVIDNU2', 'MARIJANI', '_IMPRACE',
        '_METSTAT', '_URBSTAT', '_HLTHPL1', 'LCSNUMCG', 'LCSCTSC1',
        'ASPIRIN'
    ]
    
    # Keep only selected columns if they exist in the dataset
    brfss_df = brfss_df.filter(items=[col for col in columns_to_keep if col in brfss_df.columns])
    
    return brfss_df

def main():
    """Runs the preprocessing pipeline and prints dataset info."""
    brfss_df = preprocess_data()
    
    if brfss_df is not None:
        print(f"\n✅ BRFSS Dataset Loaded:")
        print(f"Shape: {brfss_df.shape}")
        print(f"Columns: {list(brfss_df.columns)}\n")
    else:
        print("\n❌ BRFSS Dataset is missing or could not be processed.\n")

if __name__ == "__main__":
    main()
