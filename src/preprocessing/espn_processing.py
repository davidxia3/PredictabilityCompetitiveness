import pandas as pd
import json

league = "nhl"
df = pd.read_csv(f'data/combined/{league}_market.csv')

df['espn_id'] = "000000000"
df["game_type"] = "N/A"

for index, row in df.iterrows():
    date = row["date"]
    team1 = row["team_1"]
    team2 = row["team_2"]

    try:
        with open(f'data/espn_mapping/{league}/{team1}.json', 'r') as json_file:
            mapping = json.load(json_file)
            
            if date in mapping:
                df.at[index, "espn_id"] = mapping[date][0]
                df.at[index, "game_type"] = mapping[date][1]
            else:
                print(f'{team1} {team2} {date}')
    except Exception as e:
        try:
            with open(f'data/espn_mapping/{league}/{team2}.json', 'r') as json_file:
                mapping = json.load(json_file)
                
                if date in mapping:
                    df.at[index, "espn_id"] = mapping[date][0]
                    df.at[index, "game_type"] = mapping[date][1]
                else:
                    print(f'{team1} {team2} {date}')
        except Exception as e:
            print(f"Error for {team1} on {date}: {e}")

df.to_csv(f'data/espn_combined/{league}_espn_combined.csv', index=False)
