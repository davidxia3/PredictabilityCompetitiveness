# Results Documentation

## Contains the data and graphic forms of results derived from the analysis of processed data

### results/fivethirtyeight_results.csv
- FiveThirtyEight held a NFL probability forecasting game for the 2019, 2020, 2022, and 2023 NFL seasons
- Players would make a probabilistic prediction for every game and they would receive/lose points for their predictions
- They used Brier Scores to calculate the points based on the result and the probabilistic prediction
- This CSV contains the placements and percentiles of a hypothetical player that predicted every game using the moneyline probabilistic prediction

### results/{league}_by_team.csv
- Shows the different loss scores of each team across each league
- brier_score: standard brier score 
- log_loss: standard log loss
- brier_skill_loss_50_50: brier skill loss score, using a naive 50/50 prediction method as reference
- brier_skill_loss_home_prob_grouped: brier skill loss score, using the home win rate of all games involving the specific team as reference
- brier_skill_loss_home_prob_overall: brier skill loss score, using the home win rate of all games as reference

### results/{league}_calibration_quantile.png
- Calibration plot over all games in the league, using 10 quantile bins

### results/{league}_calibration_uniform.png
- Calibration plot over all games in the league, using 10 uniformly distributed bins over (0-1)
- Some extreme bins are missing, because there were no games that had those probabilities as predictions

### results/{league}_seasonal.csv
- Shows the different loss scores of each season across each league
- brier_score: standard brier score 
- log_loss: standard log loss
- brier_skill_loss_50_50: brier skill loss score, using a naive 50/50 prediction method as reference
- brier_skill_loss_home_prob_grouped: brier skill loss score, using the home win rate of all games from that season as reference
- brier_skill_loss_home_prob_overall: brier skill loss score, using the home win rate of all games as reference