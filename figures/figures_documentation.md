# Figures Documentation

## Contains all figures and graphs

### figures/calibration/
- Folder with four calibration files, one for each of the leagues
- Shows the calibration plot of moneyline based probabilistic predictions
- Uses 10 uniform bins

### brier_seasonal.png
- Shows the Brier scores of the four leagues by season

### brier_vs_log_loss.py
- Compares the scaled performances of prediction methods using both the Brier Score and the Log Loss metrics 

### figures/nfl_brier_seasonal.png
- Shows Brier scores of four different models (betting market, Elo, home bias coinflip, 50/50 coinflip) for NFL by season

### figures/nfl_brier_teamwise.png
- Shows Brier scores of the games involving each of the 32 NFL teams
- Sorted in ascending order

### figures/nfl_teamwise_winrate_corr.png
- Shows the correlation between the Brier score of a team's games and the teams deviation from the baseline 50% win rate

### figures/predicted_home_win_box_plot.png
- Shows a box plot for the moneyline based probabilistic home team prediction distribution of the four different leagues
- Baselin 50% is shown in black
