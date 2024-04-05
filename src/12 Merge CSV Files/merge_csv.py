import pandas as pd

def merge_csv_files(input_files, output_file):
    # Read each CSV file into a DataFrame
    dfs = [pd.read_csv(file) for file in input_files]
    # Concatenate the DataFrames, ignoring indexes
    merged_df = pd.concat(dfs, ignore_index=True)
    # Write the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file, index=False)

# Example usage
input_files = ["class1.csv", "class2.csv"]
output_file = "all_students.csv"
merge_csv_files(input_files, output_file)
