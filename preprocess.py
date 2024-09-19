"""Demo script for data preprocessing.

Author: Jan Aarts

Usage: python preprocess.py dataset1.csv dataset2.csv instructions.json
"""


#imports
from sys import argv
from pathlib import Path
import pandas as pd
import json

def parse_args(arguments):
    instructions = {}
    list_of_csvs = []
    for argument in arguments:
        if Path(argument).suffix == ".csv":
            df = pd.read_csv(Path(argument))
            list_of_csvs.append(df)
        elif Path(argument).suffix == ".json":
            with open(Path(argument)) as json_file:
                instructions = json.load(json_file)
    if len(list_of_csvs) == 0:
        print("No csv files found. Creating empty dataset.")
        df = pd.DataFrame
        list_of_csvs.append(df)
    return list_of_csvs, instructions

def merge_csvs(list_dfs):
    try:
        combined_df = pd.concat(list_dfs, ignore_index=True)
    except Exception as e:
        # If an error occurs, print the error message
        print(f"An error occurred: {e}")
        combined_df = None
    finally:
        # If an error occurred, return the DataFrame from the first CSV file
        if combined_df is None:
            print("Returning the first CSV file's data due to an error.")
            combined_df = list_dfs[0]
    return combined_df

def write_output(df_to_write):
    df_to_write.to_csv("output.csv")


def main():
    #load list of files as csv
    print(argv)
    list_dfs, instructions = parse_args(argv)
    merged_df = merge_csvs (list_dfs)
    write_output(merged_df)






if __name__ == "__main__":
    main()
