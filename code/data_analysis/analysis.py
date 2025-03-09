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
    
    if not os.path.exists(os.path.expanduser("~/DataScience_Projects/Stroke_Risk_Assessment/heatmap.png")):
        # Set up the figure
        plt.figure(figsize=(16, 12))

        # Create a heatmap
        sns.heatmap(corr_matrix, cmap='coolwarm', annot=False, fmt=".2f", linewidths=0.5, vmin=-1, vmax=1)

        # Add title
        plt.title("Pearson Correlation Matrix", fontsize=16)

        # Show plot
        plt.show()
        # plt.savefig('heatmap.jpg')
    
    threshold = 0.85
    high_corr_pairs = []

    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i,j]) > threshold:
                col1 = corr_matrix.columns[i]
                col2  =corr_matrix.columns[j]
                high_corr_pairs.append((col1,col2,corr_matrix.iloc[i,j]))
    
    high_corr_df = pd.DataFrame(high_corr_pairs, columns=["Feature_1", "Feature_2", "Correlation"])

    # Display highly correlated pairs
    print("Highly correlated feature pairs (correlation > 0.85):")
    print(high_corr_df)

def reduce_colinearity(df):
    cols_to_remove = ['BPMEDS1', '_RFDRHV8', 'SDLONELY','Chronic_Disease_Risk', 'Weighted_Overall_Health_Risk']

    df.drop(columns=cols_to_remove,errors='coerce',inplace=True)

    return df


df  = open_csv(FILE_PATH)
df_final  = reduce_colinearity(df)
print(df.info())




