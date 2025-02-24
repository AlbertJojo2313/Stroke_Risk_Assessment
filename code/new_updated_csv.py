import os
import pandas as pd
OUTPUT_DIR = os.path.expanduser(
    "~/DataScience_Projects/Stroke_Risk_Assessment/data/Processed")


def convert_df_to_csv(brfss_df: pd.DataFrame):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    brfss_file_path = os.path.join(OUTPUT_DIR, "brfss.csv")

    brfss_df.to_csv(brfss_file_path, index=False)  # Overwrites/creates file

    print("\n Process Complete ...")
