import pandas as pd
import numpy as np

league = 'nba'

df = pd.read_csv(f'processed_data/{league}_espn_combined.csv')

df['pred_prob'] = df['avg_prob_1']

brier_scores = {}

teams = pd.concat([df['team_1'], df['team_2']]).unique()

for team in teams:
    team_games = df[(df['team_1'] == team) | (df['team_2'] == team)]
    
    team_games['team_result'] = team_games.apply(lambda row: row['result'] if row['team_1'] == team else 1 - row['result'], axis=1)
    team_games['brier_score'] = (team_games['pred_prob'] - team_games['team_result']) ** 2
    
    team_brier_scores = team_games.groupby(['tournament'])['brier_score'].mean()
    
    brier_scores[team] = team_brier_scores

brier_df = pd.DataFrame(brier_scores)

brier_df = brier_df.reset_index()

brier_df = brier_df.round(4)
brier_df.to_csv(f'results/{league}_team_brier.csv', index=False)

