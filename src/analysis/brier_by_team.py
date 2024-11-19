import pandas as pd
import numpy as np

league = 'nfl'

df = pd.read_csv(f'processed_data/{league}_espn_combined.csv')
df['pred_prob'] = df['avg_prob_1']

brier_scores = {}

df['brier_score'] = (df['pred_prob'] - df['result']) ** 2

teams = pd.concat([df['team_1'], df['team_2']]).unique()
tournaments = df['tournament'].unique()
tournaments.sort()

for team in teams:
    team_data = (
        df[(df['team_1'] == team) | (df['team_2'] == team)] 
        .groupby('tournament')['brier_score']               
        .mean()                                            
        .reindex(tournaments, fill_value=np.nan)           
    )
    brier_scores[team] = team_data.values 

brier_df = pd.DataFrame(brier_scores, index=tournaments).reset_index()
brier_df = brier_df.rename(columns={'index': 'tournament'}) 
brier_df = brier_df.round(4)

brier_df.to_csv(f'results/{league}_team_brier.csv', index=False)
