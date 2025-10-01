# Analysis Documentation

## Contains all scripts to analyze and produce results from processed data

### src/analysis/binary_accuracy.py
- Computes binary accuracy rate of moneyline based predictions (and elo for NFL only) across the four major American sports leagues (MLB, NBA, NHL, NFL)
- Results are saved to results/binary_accuracy.csv

### src/analysis/combined_half_full_brier.py
- Compiles the half and full Brier scores for moneyline, FiveThirtyEight Elo, RatingsLib, and Bradley-Terry
- Results are saved to results/combined_half_full_brier.csv

### src/analysis/combined_half_full_log_loss.py
- Compiles the half and full Log Loss for moneyline, FiveThirtyEight Elo, RatingsLib, and Bradley-Terry
- Results are saved to results/combined_half_full_log_loss.csv

### src/analysis/fivethirtyeight_elo_half_full_brier.py
- Computes the Brier scores for each league based on second half only or the full season FiveThirtyEight Elo predictions
- Results are saved to results/elo/elo_half_full_brier.csv

### src/analysis/fivethirtyeight_elo_half_full_log_loss.py
- Computes the Log Loss for each league based on second half only or the full season FiveThirtyEight Elo predictions
- Results are saved to results/elo/elo_half_full_log_loss.csv

### fivethirtyeight_competition.py
- Outputs the result if the moneyline based predictions were a competitor in the FiveThirtyEight NFL prediction games
- Results are saved to results/fivethirtyeight_competition.csv

### src/analysis/brier.py
- Computes and compares the Brier scores by season using three different prediction models (moneyline based, baseline 50/50, and FiveThirtyEight Elo)
- Results are saved to results/moneyline/brier/{league}_brier.csv

### src/analysis/moneyline_half_full_brier.py
- Computes the Brier scores for each league based on second half only or the full season moneyline predictions
- Results are saved to results/moneyline/moneyline_half_full_brier.csv

### src/analysis/moneyline_half_full_log_loss.py
- Computes the Log Loss for each league based on second half only or the full season moneyline predictions
- Results are saved to results/moneyline/moneyline_half_full_log_loss.csv

### src/analysis/moneyline_teamwise_brier.py
- Uses moneyline based probabilistic predictions to compute the Brier scores for games involving each team
- Results are saved to results/moneyline/{league}_teamwise_brier.csv

### src/analysis/nfl_teamwise_winrate.py
- Computes the win rate of each NFL team across all seasons 
- Results are saved to results/nfl_teamwise_winrate.csv

### src/analysis/seasonal_brier.py
- Uses moneyline based probabilistic predictions to compute the seasonal Brier score, log loss, AUC, and three different Brier skill loss metrics
    - brier_skill_loss_50_50 (baseline is 50/50 coinflip model)
    - brier_skill_loss_home_prob_grouped (baseline is home team's historical home win probability)
    - brier_skill_loss_home_prob_overall (baseline is historical home win probability)
- Results are saved to results/moneyline/seasonal/{league}_seasonal_brier.csv



