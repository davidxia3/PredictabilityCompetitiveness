import pandas as pd
from sklearn.metrics import brier_score_loss
from sklearn.metrics import log_loss

league = "nba"

df = pd.read_csv(f'processed_data/{league}_espn_combined.csv')

season_groups = df.groupby('tournament')

seasons = []
brier_scores = []
log_losses = []
brier_skill_losses_50_50 = []
brier_skill_losses_team1 = []

for season, group in season_groups:
    brier = brier_score_loss(group['result'], group['avg_prob_1'])

    reference_brier_50_50 = brier_score_loss(group['result'], [0.5] * len(group))

    overall_win_prob = group['avg_prob_1'].mean()

    reference_brier_team1 = brier_score_loss(group['result'], [overall_win_prob] * len(group))

    brier_skill_score_50_50 = 1 - (brier / reference_brier_50_50)
    
    brier_skill_score_team1 = 1 - (brier / reference_brier_team1)
    
    brier_skill_loss_50_50 = 1 - brier_skill_score_50_50
    brier_skill_loss_team1 = 1 - brier_skill_score_team1
    
    seasons.append(season)
    brier_scores.append(brier)
    log_losses.append(log_loss(group['result'], group['avg_prob_1']))
    brier_skill_losses_50_50.append(brier_skill_loss_50_50)
    brier_skill_losses_team1.append(brier_skill_loss_team1)

df_results = pd.DataFrame({
    'season': seasons, 
    'brier_score': brier_scores, 
    'log_loss': log_losses, 
    'brier_skill_loss_50_50': brier_skill_losses_50_50,
    'brier_skill_loss_home_prob': brier_skill_losses_team1
})

df_results = df_results.round(4)

df_results.to_csv(f'results/{league}_seasonal.csv', index=False)
