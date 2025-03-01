import os
import pandas as pd
OUTPUT_DIR = os.path.expanduser(
    "~/DataScience_Projects/Stroke_Risk_Assessment/data/Processed")
OUTPUT_ENC_DIR = os.path.expanduser(
    "~/DataScience_Projects/Stroke_Risk_Assessment/data/Encoded")


def convert_df_to_csv(brfss_df: pd.DataFrame):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    brfss_file_path = os.path.join(OUTPUT_DIR, "brfss.csv")

    brfss_df.to_csv(brfss_file_path, index=False)  # Overwrites/creates file

    os.makedirs(OUTPUT_ENC_DIR, exist_ok=True)
    encoded_file_path = os.path.join(OUTPUT_ENC_DIR, "encoded.csv")
    brfss_df.to_csv(encoded_file_path, index=False)

    print("\n Process Complete ...")
