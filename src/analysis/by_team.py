import pandas as pd
from sklearn.metrics import brier_score_loss
from sklearn.metrics import log_loss

league = "nhl"
file = f'processed_data/{league}_espn_combined.csv'
if league == "nfl":
    file = f'processed_data/{league}_espn_combined_with_elo.csv'

df = pd.read_csv(file)

teams = pd.concat([df['team_1'], df['team_2']]).unique()

team_names = []
brier_scores = []
log_losses = []
brier_skill_losses_50_50 = []
brier_skill_losses_team1_grouped = []
brier_skill_losses_team1_overall = []

overall_percentage = df['result'].mean()
overall_brier_score = ((overall_percentage - df['result']) ** 2).mean()

for team in teams:
    team_games = df[(df['team_1'] == team) | (df['team_2'] == team)]

    brier = brier_score_loss(team_games['result'], team_games['avg_prob_1'])

    reference_brier_50_50 = brier_score_loss(team_games['result'], [0.5] * len(team_games))

    overall_win_prob = team_games['avg_prob_1'].mean()

    reference_brier_team1 = brier_score_loss(team_games['result'], [overall_win_prob] * len(team_games))

    brier_skill_score_50_50 = 1 - (brier / reference_brier_50_50)
    
    brier_skill_score_team1_grouped = 1 - (brier / reference_brier_team1)

    brier_skill_score_team1_overall = 1 - (brier / overall_brier_score)

    team_names.append(team)
    brier_scores.append(brier)
    log_losses.append(log_loss(team_games['result'], team_games['avg_prob_1']))
    brier_skill_losses_50_50.append(brier_skill_score_50_50)
    brier_skill_losses_team1_grouped.append(brier_skill_score_team1_grouped)
    brier_skill_losses_team1_overall.append(brier_skill_score_team1_overall)

df_results = pd.DataFrame({
    'team': team_names, 
    'brier_score': brier_scores, 
    'log_loss': log_losses, 
    'brier_skill_loss_50_50': brier_skill_losses_50_50,
    'brier_skill_loss_home_prob_grouped': brier_skill_losses_team1_grouped,
    'brier_skill_loss_home_prob_overall': brier_skill_losses_team1_overall
})

df_results = df_results.round(4)

df_results.to_csv(f'results/{league}_by_team.csv', index=False)
