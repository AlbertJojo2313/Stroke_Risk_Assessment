import os
from preprocess import preprocess_dataframe

OUTPUT_DIR = os.path.expanduser(
    "~/DataScience_Projects/Stroke_Risk_Assessment/data/Processed")


def convert_df_to_csv():
    brfss_df = preprocess_dataframe()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    brfss_file_path = os.path.join(OUTPUT_DIR, "brfss.csv")

    if os.path.exists(brfss_file_path):
        # Overwrites the previous file
        brfss_df.to_csv(brfss_file_path, mode="w", index=False)
    else:
        brfss_df.to_csv(brfss_file_path, index=False)  # Creates a new file


def main():
    convert_df_to_csv()
    print("Process Complete ...")


if __name__ == "__main__":
    main()
