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
import preprocess
import feature_engineering
from new_updated_csv import convert_df_to_csv


def main():
    brfss_df = preprocess.preprocess_dataframe()

    brfss_file_path = os.path.expanduser(
        "~/DataScience_Projects/Stroke_Risk_Assessment/data/Processed/brfss.csv"
    )
    encoded_file_path = os.path.expanduser(
        "~/DataScience_Projects/Stroke_Risk_Assessment/data/Encoded/encoded.csv"
    )

    # File does not exist, then create the csv file
    if not os.path.exists(brfss_file_path):
        convert_df_to_csv(brfss_df)

    # Encoded csv for model training
    encoded_df = preprocess.impute_val(brfss_df)
    encoded_df = feature_engineering.feature_engineering(encoded_df)

    if not os.path.exists(encoded_file_path):
        convert_df_to_csv(encoded_df)

    print('Process Complete ...')

    # Checking the stats
    preprocess.view_dataframe(encoded_df)


if __name__ == "__main__":
    main()
