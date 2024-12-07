import pandas as pd

csv_file_path = "raw_data/nhl/CBJ/market.csv" 
column_to_check = "date"   

try:
    df = pd.read_csv(csv_file_path)
    print(f"CSV file '{csv_file_path}' loaded successfully.")
except FileNotFoundError:
    print(f"Error: File '{csv_file_path}' not found.")
    exit()

if column_to_check not in df.columns:
    print(f"Error: Column '{column_to_check}' not found in the CSV file.")
    exit()

duplicates = df[column_to_check].duplicated(keep=False)

if duplicates.any():
    print(f"Duplicates found in column '{column_to_check}':")
    duplicate_values = df.loc[duplicates, column_to_check]
    print(duplicate_values)
else:
    print(f"No duplicates found in column '{column_to_check}'.")

unique_duplicates = duplicate_values.unique()
print(f"Unique duplicate dates:\n{unique_duplicates}")
