import pandas as pd
import numpy as np

def feature_engineering(df):
    """Enchances the dataset by creating new meaningful features"""

    # Creates a new features

    # Add a new feature that combines all the health features and give the overall score of health risks for instance if you have stroke, diabetes, or pre-diabetes, TOLDHI3, etc.
    # Hypertension and Diabetes
    df['Metabolic_Risk'] = ((df['BPHIGH6'].isin([1,2]) & (df['DIABETE4'].isin([1,2,4])) & df['PREDIAB2'].isin([1,2]))).astype(int)


    # Lifestyle risk
    df['Unhealthy_Behavior'] = ((df['_SMOKER3'].isin([1,2])) & (df['_RFBING6'] == 2)).astype(int)

    # Employment Stability
    df['Employment_Stability'] = ((df['EMPLOY1'].isin([1,2])) & (df['RENTHOM1'] == 1)).astype(int)

    # LifeStyle (Satisfaction) & Emotion Support
    df['LifeStyle_EmotionSupport'] = ((df['MARITAL'].isin([1,2,6])) & df['LSATSIFY'].isin([1,2])).astype(int)

    # -- Combined overall Risk score from all categories
    
    # Create a combined overall risk score
    # df['Combined_Risk_Score'] = 
    
