import pandas as pd

df = pd.read_csv("processed_data/nfl_espn_combined_with_elo.csv")

team_1_wins = df[['team_1', 'result']].copy()
team_1_wins.columns = ['team', 'win']
team_1_wins['win'] = team_1_wins['win']

team_2_wins = df[['team_2', 'result']].copy()
team_2_wins.columns = ['team', 'win']
team_2_wins['win'] = 1 - team_2_wins['win']

all_teams = pd.concat([team_1_wins, team_2_wins])

win_rates = all_teams.groupby('team')['win'].mean()

win_rates_df = win_rates.reset_index().rename(columns={'win': 'win_rate'}).sort_values(by='win_rate', ascending=False)

win_rates_df.to_csv("results/nfl_team_win_rates.csv", index=False)
