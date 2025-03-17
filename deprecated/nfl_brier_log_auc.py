import pandas as pd
from sklearn.metrics import log_loss, roc_auc_score
import numpy as np

file_path = "processed_data/combined/nfl_espn_combined_with_elo.csv"
df = pd.read_csv(file_path)

grouped = df.groupby('tournament')

seasons = []
brier_scores = []
log_losses = []
auc_scores = []

for season, group in grouped:
    y_true = group['result']
    y_pred = group['avg_prob_1']
    
    brier_score = np.mean((y_pred - y_true) ** 2)
    
    try:
        log_loss_value = log_loss(y_true, y_pred)
    except ValueError:
        log_loss_value = np.nan 
    
    try:
        auc_value = roc_auc_score(y_true, y_pred)
    except ValueError:
        auc_value = np.nan
    
    seasons.append(season)
    brier_scores.append(brier_score)
    log_losses.append(log_loss_value)
    auc_scores.append(auc_value)

metrics_df = pd.DataFrame({
    'season': seasons,
    'brier_score': brier_scores,
    'log_loss': log_losses,
    'auc': auc_scores
})

output_file = "results/nfl_brier_log_auc.csv"
metrics_df.to_csv(output_file, index=False)

