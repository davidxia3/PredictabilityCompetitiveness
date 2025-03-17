import pandas as pd
import json
import os
import numpy as np

# define the league
leagues = ['nba', 'nfl', 'nhl', 'mlb']

for league in leagues:

    # getting team names
    def list_subfolders(folder_path):
        teams = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]
        return teams

    # load team abbreviations from JSON
    def load_team_abbreviations(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)

    # loading team data
    folder_path = f'raw_data/{league}'
    teams = list_subfolders(folder_path)

    abbreviation_file_path = f'raw_data/abbreviations.json' 
    team_abbreviation_dict = load_team_abbreviations(abbreviation_file_path)

    # combining files into a single list
    combined_list = []
    id_set = set()

    for team in teams:
        file_path = f'raw_data/{league}/{team}/market.csv'
        try:
            data = pd.read_csv(file_path) 
            for _, item in data.iterrows():
                item_id = item.get("game_url")
                team_1 = item.get("team_1")
                team_2 = item.get("team_2")

                # check if both teams are valid (not friendly games)
                if team_1 in team_abbreviation_dict.values() and team_2 in team_abbreviation_dict.values():
                    if item_id and item_id not in id_set:
                        combined_list.append(item)
                        id_set.add(item_id)
        except FileNotFoundError:
            print(f"File not found for team: {team}")

    df = pd.DataFrame(combined_list)

    # differentiate positive and negative moneylines
    def fix_moneyline_signs(row, col1, col2):
        val1, val2 = abs(row[col1]), abs(row[col2])

        if val1 > val2:
            return -val1, val2
        else:
            return val1, -val2

    df[['avg_moneyline_1', 'avg_moneyline_2']] = df.apply(
        lambda row: fix_moneyline_signs(row, 'avg_moneyline_1', 'avg_moneyline_2'), axis=1, result_type='expand'
    )


    # function to truncate probabilities to 4 digits
    def truncate(value):
        return float(int(value * 10**4)) / 10**4

    # calculate moneyline probabilities
    avg_moneyline_1 = abs(df['avg_moneyline_1'])
    avg_moneyline_2 = abs(df['avg_moneyline_2'])

    star1 = np.where(avg_moneyline_2 > avg_moneyline_1, 100 / (avg_moneyline_1 + 100), avg_moneyline_1 / (avg_moneyline_1 + 100))
    star2 = np.where(avg_moneyline_2 > avg_moneyline_1, avg_moneyline_2 / (avg_moneyline_2 + 100), 100 / (avg_moneyline_2 + 100))

    avg_prob_1 = star1 / (star1 + star2)
    df['avg_prob_1'] = avg_prob_1

    # truncate probabilities
    df['avg_prob_1'] = df['avg_prob_1'].apply(truncate)

    # rearranging columns
    new_order = ['date', 'tournament', 'team_1', 'team_2', 'score_1', 'score_2', 'result', 
                'avg_moneyline_1', 'avg_moneyline_2',
                'avg_prob_1', 'game_url']
    df = df[new_order]

    # filter out friendly games and current season
    two_year_pattern = r'^([A-Za-z]{3})_([0-9]{4})/([0-9]{4})$'
    one_year_pattern = r'^[A-Za-z]{3}_[0-9]{4}$'

    df['tournament'] = df['tournament'].str.replace(two_year_pattern, r'\1_\3', regex=True)
    df = df[df['tournament'].str.match(one_year_pattern)]


    df.to_csv(f'raw_data/combined/{league}_market.csv', index=False)

    print("done.")
