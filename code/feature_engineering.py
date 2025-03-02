def feature_engineering(df):
    """Enhances the dataset by creating new meaningful features with weighted overall health risk."""

    # Add a new feature that combines all the health features and gives the overall score of health risks.
    # Hypertension and Diabetes combined risk factor
    df['Metabolic_Risk'] = ((df['BPHIGH6'].isin([1, 2])) & 
                            (df['DIABETE4'].isin([1, 2, 4])) & 
                            df['PREDIAB2'].isin([1, 2])).astype(int)

    # Lifestyle risk (combining smoking and binge drinking)
    df['Unhealthy_Behavior'] = ((df['_SMOKER3'].isin([1, 2])) & (df['_RFBING6'] == 2)).astype(int)

    # Employment Stability (employment status and owning a home)
    df['Employment_Stability'] = ((df['EMPLOY1'].isin([1, 2])) & (df['RENTHOM1'] == 1)).astype(int)

    # Life satisfaction and emotional support (based on marital status and life satisfaction)
    df['LifeStyle_EmotionSupport'] = ((df['MARITAL'].isin([1, 2, 6])) & df['LSATISFY'].isin([1, 2])).astype(int)


    # BMI-based features
    df['Overweight_or_Obese'] = df['_BMI5CAT'].isin([3, 4]).astype(int)

    # Chronic Disease Risk: Combines diabetes, high blood pressure, and high cholesterol
    df['Chronic_Disease_Risk'] = ((df['BPHIGH6'].isin([1, 2])) |
                                  (df['DIABETE4'].isin([1, 2, 4])) |
                                  (df['TOLDHI3'] == 1)).astype(int)

    # Risk of Stroke: Combining CVD history, cholesterol, hypertension, and diabetes
    df['Stroke_Risk'] = ((df['CVDSTRK3'] == 1) |
                         (df['BPHIGH6'].isin([1, 2])) |
                         (df['DIABETE4'].isin([1, 2, 4])) |
                         (df['TOLDHI3'] == 1)).astype(int)

    # Lifestyle risk factor: smoking and alcohol consumption combined with low physical activity
    df['Lifestyle_Risk'] = ((df['_SMOKER3'].isin([1, 2])) |
                            (df['_RFBING6'] == 2) |
                            (df['_PACAT3'].isin([3, 4]))).astype(int)

    # --- Healthcare Access ---
    # Healthcare Access: Whether a person has health insurance or not
    df['Healthcare_Access'] = (df['_HLTHPL1'] == 1).astype(int)

    # --- Weighted Overall Health Risk ---
  
    
    weights = {
        'Metabolic_Risk': 0.4,        # Higher weight for metabolic risk
        'Chronic_Disease_Risk': 0.3,  # Moderate weight for chronic diseases
        'Stroke_Risk': 0.2,           # Moderate weight for stroke risk
        'Lifestyle_Risk': 0.1         # Lower weight for lifestyle risk
    }

    # Calculate the weighted overall health risk score
    df['Weighted_Overall_Health_Risk'] = (
        weights['Metabolic_Risk'] * df['Metabolic_Risk'] +
        weights['Chronic_Disease_Risk'] * df['Chronic_Disease_Risk'] +
        weights['Stroke_Risk'] * df['Stroke_Risk'] +
        weights['Lifestyle_Risk'] * df['Lifestyle_Risk']
    )

    # --- Additional Features ---
    # You can also normalize the Weighted Overall Health Risk if needed to get it into a 0-1 range
    # Example: df['Normalized_Health_Risk'] = (df['Weighted_Overall_Health_Risk'] - df['Weighted_Overall_Health_Risk'].min()) / (df['Weighted_Overall_Health_Risk'].max() - df['Weighted_Overall_Health_Risk'].min())

    return df
