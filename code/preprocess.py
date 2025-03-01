import os
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.impute import KNNImputer

# Importing the value tables
from value_table_dict import VALUE_TABLES, invert_mapping

# Set the data folder path (can be changed easily)
FILE_PATH = os.path.expanduser(
    "~/DataScience_Projects/Stroke_Risk_Assessment/data/Raw")


def open_files(file_path):
    """Loads CSV files into DataFrames with optimized dtypes."""
    dataset = "brfss_2023.csv"
    full_path = os.path.join(file_path, dataset)

    if not os.path.exists(full_path):
        print(f"⚠️ Warning: File {dataset} not found!")
        return None

    try:
        # Load as string for memory efficiency
        df = pd.read_csv(full_path, dtype=str)
        return df
    except Exception as e:
        print(f"❌ Error loading {dataset}: {e}")
        return None


def create_dataframe():
    """Preprocesses data by dropping unnecessary columns and optimizing dtypes."""
    brfss_df = open_files(FILE_PATH)

    if brfss_df is None:
        return None

    # Columns to keep
    columns_to_keep = [
        'HTM4', '_BMI5CAT', 'CVDSTRK3', 'BPHIGH6', 'BPMEDS1', 'TOLDHI3', 'CHOLMED3',
        'CVDINFR4', 'CVDCRHD4', 'PREDIAB2', 'DIABETE4', '_RFHYPE6', '_RFCHOL3',
        '_MICHD', '_SMOKER3', 'SMOKDAY2', 'ECIGNOW2', '_CURECI2', 'AVEDRNK3',
        '_RFBING6', '_RFDRHV8', '_PACAT3', 'MARITAL', 'EMPLOY1', 'INCOME3',
        'RENTHOM1', 'VETERAN3', 'LSATISFY', 'EMTSUPPRT', 'SDLONELY', 'SDHSTRE1',
        'COVIDPO1', 'MARIJAN1', '_IMPRACE', '_METSTAT', '_URBSTAT', '_HLTHPL1',
        'ASPIRIN'
    ]

    # Keep only selected columns if they exist in the dataset
    brfss_df = brfss_df.filter(
        items=[col for col in columns_to_keep if col in brfss_df.columns])

    return brfss_df


def preprocess_dataframe():
    df = create_dataframe()

    if df is None:
        return None

    df1 = df.copy()

    # Convert string values to numeric
    df1 = df1.apply(pd.to_numeric, errors='coerce')  # Converts string to float

    # Replace with value table mappings
    df1 = df1.replace(VALUE_TABLES)

    # Impute NULL Values
    df1 = imputation_null_values(df1)

    return df1


# Returns an encoded dataframe
def encoded_values(df):
    inverted_value_tables = invert_mapping(VALUE_TABLES)
    df_encoded = df.replace(inverted_value_tables)

    return df_encoded


def imputation_null_values(df):
    """Handles missing values using KNN imputation & Drop small counts of null values."""

    # Drop rows that have small null values
    drop_small = ['CVDSTRK3', 'BPHIGH6', 'CVDINFR4', 'CVDCRHD4', 'DIABETE4']

    df = df.dropna(subset=drop_small)

    # Drop columns with excessive missing values
    cols_to_drop = ['ASPIRIN']
    df.drop(columns=cols_to_drop, inplace=True)

    return df


# Returns the final dataframe
def impute_val(df):
    # Make a new category "Missing" for NA values
    cols_avoid = ['HTM4']  # Avoid these cols
    cols_impute = [col for col in df.columns if col not in cols_avoid]
    df[cols_impute] = df[cols_impute].fillna(
        'Missing')  # Makes a new category Missing

    # Impute numerical cols

    ncols_impute = ['HTM4']

    df[ncols_impute] = df[ncols_impute].apply(pd.to_numeric,errors='coerce')

    knn__imputer = KNNImputer(n_neighbors=5)
    df[ncols_impute] = knn__imputer.fit_transform(df[ncols_impute])

    df[ncols_impute] = df[ncols_impute].round(0).astype(int)
    df = encoded_values(df)
    return df

# ------Helper Functions------- #


def view_dataframe(brfss_df):
    """Displays null value counts and basic dataset info."""
    count_null_values = brfss_df.isna().sum()
    print(f"Total Null Value Count: {count_null_values} \n")
    print(brfss_df.info())


def dataframe_info():
    """Prints information about the dataset."""
    brfss_df = create_dataframe()

    if brfss_df is not None:
        print(f"\n✅ BRFSS Dataset Loaded:")
        print(f"Shape: {brfss_df.shape}")
        print(f"Columns: {list(brfss_df.columns)}\n")
    else:
        print("\n❌ BRFSS Dataset is missing or could not be processed.\n")
