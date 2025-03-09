import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

FILE_PATH = os.path.expanduser("~/DataScience_Projects/Stroke_Risk_Assessment/data/Encoded")

def open_csv(file_path):
    dataset = 'encoded.csv'
    file_path = os.path.join(file_path,dataset)

    if not os.path.exists(file_path):
        raise FileNotFoundError
    
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise e
        return None

def pearson_coeff(df):
    data = df

    corr_matrix  = data.corr(method='pearson')

    # Set up the figure
    plt.figure(figsize=(16, 12))

    # Create a heatmap
    sns.heatmap(corr_matrix, cmap='coolwarm', annot=False, fmt=".2f", linewidths=0.5, vmin=-1, vmax=1)

    # Add title
    plt.title("Pearson Correlation Matrix", fontsize=16)

    # Show plot
    plt.show()
    # plt.savefig('heatmap.jpg')


df  = open_csv(FILE_PATH)
pearson_coeff(df)


