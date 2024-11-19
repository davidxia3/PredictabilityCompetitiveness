import pandas as pd
import numpy as np

league = 'nba'

df = pd.read_csv(f'processed_data/{league}_espn_combined.csv')
df['pred_prob'] = df['avg_prob_1']

log_losses = {}

# Calculate log loss
def log_loss(pred_prob, result):
    # Clip probabilities to prevent log(0) errors
    pred_prob = np.clip(pred_prob, 1e-15, 1 - 1e-15)
    return - (result * np.log(pred_prob) + (1 - result) * np.log(1 - pred_prob))

df['log_loss'] = log_loss(df['pred_prob'], df['result'])

teams = pd.concat([df['team_1'], df['team_2']]).unique()
tournaments = df['tournament'].unique()
tournaments.sort()

for team in teams:
    team_data = (
        df[(df['team_1'] == team) | (df['team_2'] == team)] 
        .groupby('tournament')['log_loss']               
        .mean()                                            
        .reindex(tournaments, fill_value=np.nan)           
    )
    log_losses[team] = team_data.values 

log_loss_df = pd.DataFrame(log_losses, index=tournaments).reset_index()
log_loss_df = log_loss_df.rename(columns={'index': 'tournament'}) 
log_loss_df = log_loss_df.round(4)

log_loss_df.to_csv(f'results/{league}_team_log_loss.csv', index=False)
