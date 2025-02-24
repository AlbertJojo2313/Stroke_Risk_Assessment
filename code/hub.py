#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:58:22 2025

@author: aj
"""
import os
import preprocess
from new_updated_csv import convert_df_to_csv


def main():
    brfss_df = preprocess.preprocess_dataframe()

    brfss_file_path = os.path.expanduser(
        "~/DataScience_Projects/Stroke_Risk_Assessment/data/Processed/brfss.csv"
    )
    # Viewing the dataframe
    preprocess.view_dataframe(brfss_df)

    if not os.path.exists(brfss_file_path):
        convert_df_to_csv(brfss_df)



    print('Process Complete ...')


if __name__ == "__main__":
    main()
