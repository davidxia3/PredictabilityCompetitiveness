import pandas as pd
import json

file_path = 'raw_data/nfl_espn_combined.csv'
output_path = 'processed_data/nfl_espn_combined_with_elo.csv'

df = pd.read_csv(file_path)

with open("raw_data/fivethirtyeight_mapping.json", 'r') as json_file:
    mapping = json.load(json_file)

elo_prob_1_values = []

for index, row in df.iterrows():
    date = row["date"]
    team1 = row["team_1"]
    team2 = row["team_2"]
    key = date + "_" + team1 + "_" + team2
    
    elo_prob_1 = mapping.get(key, None)
    elo_prob_1_values.append(elo_prob_1)

df['elo_prob_1'] = elo_prob_1_values

df.to_csv(output_path, index=False)


    