###Takes in the pre-processed dataframe and converts to a new csv file
import os
import pandas as pd
import numpy as np
from preprocess import create_dataframe

OUTPUT_DIR = os.path.expanduser("~/DataScience_Projects/Stroke_Risk_Assessment/data/Processed")
def convert_df_to_csv():
    brfss_df = create_dataframe()

    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    brfss_file_path = os.path.join(OUTPUT_DIR,"brfss.csv")

    brfss_df.to_csv(brfss_file_path)


def main():
    convert_df_to_csv()

if __name__ == "__main__":
    main()