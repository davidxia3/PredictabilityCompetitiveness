import pandas as pd

# Load the CSV file into a DataFrame
league = "mlb"
file_path = f'processed_data/{league}_espn_combined.csv'
df = pd.read_csv(file_path)

# Recalculate avg_prob_1
def truncate(value):
    return float(int(value * 10**4)) / 10**4

df['avg_prob_1'] = df.apply(lambda row: truncate(
    abs(row['avg_moneyline_1']) / (abs(row['avg_moneyline_1']) + abs(row['avg_moneyline_2']))
), axis=1)

# Recalculate and truncate high_prob_1
df['high_prob_1'] = df.apply(lambda row: truncate(
    abs(row['high_moneyline_1']) / (abs(row['high_moneyline_1']) + abs(row['high_moneyline_2']))
), axis=1)

# Save the modified DataFrame back to the original file
df.to_csv(file_path, index=False)

print(f"Modified DataFrame saved to '{file_path}'.")