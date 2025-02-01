import pandas as pd
import json


# open the combined file and create new columns with default values
league = "nba"
df = pd.read_csv(f'raw_data/combined/{league}_market.csv')

df['espn_id'] = "000000000"
df["game_type"] = "N/A"


# try matching up games with dates in espn_mapping files
for index, row in df.iterrows():
    date = row["date"]
    team1 = row["team_1"]
    team2 = row["team_2"]

    # tries the first team
    try:
        with open(f'raw_data/espn_mapping/{league}/{team1}.json', 'r') as json_file:
            mapping = json.load(json_file)
            
            if date in mapping:
                df.at[index, "espn_id"] = mapping[date][0]
                df.at[index, "game_type"] = mapping[date][1]
            else:
                print(f'{team1} {team2} {date}')
    except Exception as e:
        # if first team does not have espn_mapping file (Arizona Coyotes), then try with second team
        try:
            with open(f'raw_data/espn_mapping/{league}/{team2}.json', 'r') as json_file:
                mapping = json.load(json_file)
                
                if date in mapping:
                    df.at[index, "espn_id"] = mapping[date][0]
                    df.at[index, "game_type"] = mapping[date][1]
                else:
                    print(f'{team1} {team2} {date}')
        except Exception as e:
            print(f"Error for {team1} on {date}: {e}")

df = df[df['game_type'] != 'preseason']


save_file = f'processed_data/{league}_espn_combined.csv'
if league == "nfl":
    save_file = "raw_data/nfl_espn_combined.csv"

df.to_csv(save_file, index=False)
