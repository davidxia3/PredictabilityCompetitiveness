import pandas as pd

# Read the CSV into a DataFrame
df = pd.read_csv('failures.csv')

# Count the number of rows for each unique team
team_counts = df['team'].value_counts()

print(team_counts)
