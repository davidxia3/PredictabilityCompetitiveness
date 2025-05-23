# Graphing Documentation

## Contains all the scripts to graph processed data and create figures

### brier_vs_log_loss.py
- Compares the scaled performances of prediction methods using both the Brier Score and the Log Loss metrics 

### src/graphing/calibration.py
- Creates the calibration plot of the four leagues using the betting market based, Bradley-Terry based, and Ratingslib based probabilistic predictions
- 10 uniform bins are used for each league and method
- Also creates a separate calibration plot for just second half of season games
- Results are saved to figures/calibration/{league}_calibration.png
- Second half of season only results are saved to figures/calibration/{league}_half_calibration.png
- Saves the counts and normalized counts of each bin of each plot to results/calibration_statistics.csv

### src/graphing/nfl_brier_modelwise.py
- Computes the brier score of four probabilistic prediction (betting market, Elo, home bias coinflip, 50/50 coinflip) models for NFL by season
- Results are saved to figures/nfl_brier_modelwise.png

### src/graphing/nfl_teamwise_sorted.py
- Computes the Brier score of each NFL team using the betting market probabilistic predictions and sorts them in ascending order
- Results are saved to figures/nfl_teamwise_sorted.py

### src/graphing/nfl_teamwise_winrate_corr.py
- Computes the correlation between the Brier score measured predictability of teams and the team win rate
- Results are saved to figures/nfl_teamwise_winrate_corr.png

### src/graphing/predicted_home_win_box_plot.py
- Creates a box plot showing the distributions of the moneyline based predicted home team win probability of the four leagues
- Results are saved to figures/predicted_home_win_box_plot.png

### src/graphing/seasonal.py
- Computes the seasonal Brier scores of each of the four leagues using the betting market based probabilistic predictions
- Results are saved to figures/seasonal.png
