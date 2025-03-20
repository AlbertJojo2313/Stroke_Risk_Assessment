#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:58:22 2025
@author: aj
"""
import sys
import os
preprocess_module = os.path.expanduser('~/DataScience_Projects/Stroke_Risk_Assessment/code/preprocessing')
sys.path.append(preprocess_module)
analysis_module = os.path.expanduser('~/DataScience_Projects/Stroke_Risk_Assessment/code/data_analysis')
sys.path.append(analysis_module)

import preprocess
import feature_engineering
from new_updated_csv import convert_df_to_csv
import analysis 

def main():
    brfss_df = preprocess.preprocess_dataframe()

    brfss_file_path = os.path.expanduser(
        "~/DataScience_Projects/Stroke_Risk_Assessment/data/Processed/brfss.csv"
    )
    encoded_file_path = os.path.expanduser(
        "~/DataScience_Projects/Stroke_Risk_Assessment/data/Encoded/encoded.csv"
    )
    final_data_path = os.path.expanduser(
        "~/DataScience_Projects/Stroke_Risk_Assessment/data/Final_Data/final_dataset.csv"
    )

    # File does not exist, then create the csv file
    if not os.path.exists(brfss_file_path):
        convert_df_to_csv(brfss_df)

    # Encoded csv for data analysis
    encoded_df = preprocess.impute_val(brfss_df)
    encoded_df = feature_engineering.feature_engineering(encoded_df)

    # Final data set
    final_df = analysis.reduce_colinearity(encoded_df)
    final_df = preprocess.to_lowercase(final_df)

 

    if not os.path.exists(encoded_file_path):
        convert_df_to_csv(encoded_df)

    if not os.path.exists(final_data_path):
        convert_df_to_csv(final_df)

    print('Process Complete ...')

    # Checking the stats
    preprocess.view_dataframe(final_df)


if __name__ == "__main__":
    main()
