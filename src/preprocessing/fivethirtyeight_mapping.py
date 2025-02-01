import pandas as pd
import json


file_path = 'raw_data/fivethirtyeight/fivethirtyeight_nfl_elo.csv'

df = pd.read_csv(file_path)

mapping = {}

for index, row in df.iterrows():
    date = row["date"].split("-")
    year = date[0]
    month = date[1]
    day = date[2]
    team1 = row["team1"]
    team2 = row["team2"]

    if team1 == "OAK":
        team1 = "LV"
    if team2 == "OAK":
        team2 = "LV"

    key = day+"-"+month+"-"+year+"_"+team1+"_"+team2
    key2 = day+"-"+month+"-"+year+"_"+team2+"_"+team1

    mapping[key] = row["elo_prob1"]
    mapping[key2] = 1-row["elo_prob1"]

with open("raw_data/fivethirtyeight/fivethirtyeight_mapping.json", 'w') as json_file:
    json.dump(mapping, json_file, indent=4)