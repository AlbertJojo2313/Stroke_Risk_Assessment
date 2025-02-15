import os
import pandas as pd
import xport

def load_sas_xpt(xpt_file, encoding="utf-8"):
    """
    Loads a SAS XPT file into a DataFrame.
    
    Args:
    - xpt_file: Path to the .XPT file.
    - encoding: The encoding for reading the file (default is utf-8).
    
    Returns:
    - DataFrame containing the data from the .XPT file.
    """
    try:
        # Check if file exists
        if not os.path.exists(xpt_file):
            raise FileNotFoundError(f"The file {xpt_file} does not exist.")
        
        # Read the SAS XPT file
        df = pd.read_sas(xpt_file, format="xport", encoding=encoding)
        print(f"Successfully loaded {xpt_file}")
        return df
    except Exception as e:
        print(f"Error loading {xpt_file}: {e}")
        return None

def save_to_csv(df, output_file):
    """
    Saves the DataFrame to a CSV file.
    
    Args:
    - df: The DataFrame to save.
    - output_file: The path to the output CSV file.
    """
    try:
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def main(xpt_file, output_file):
    """
    Main function to load the .XPT file and save it to CSV.
    
    Args:
    - xpt_file: Path to the .XPT file.
    - output_file: The path to the output CSV file.
    """
    df = load_sas_xpt(xpt_file)
    if df is not None:
        save_to_csv(df, output_file)

# Example usage
if __name__ == "__main__":
    xpt_file = 'LLCP2023.XPT '  # Change this path accordingly
    output_file = 'brfss_2023.csv'  # Change this path accordingly
    main(xpt_file, output_file)
