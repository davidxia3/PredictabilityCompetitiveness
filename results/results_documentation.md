# Results Documentation

## Contains all processed results for graphing and figures

### results/bradley_terry/
- Folder that contains results of Bradley-Terry based probabilistic predictions for the four leagues
    - {league}_bradley_terry_predictions.csv has the gamewise probabilistic predictions for all games
    - {league}_bradley_terry_ratings.csv has the gamewise Bradley-Terry ratings for all games
    - bradley_terry_half_full_brier.csv contains Bradley-Terry based Brier score of all leagues based on second half only and full season
    - bradley_terry_half_full_log_loss.csv contains Bradley-Terry based Log Loss of all leagues based on second half only and full season
- Also contains parallel version of each file with only second half of season games


### resuls/fivethirtyeight_elo/
- results/fivethirtyeight_elo/fivethirtyeight_elo_half_full_brier.csv contains second half only and full season Brier scores for each of the four league based on FiveThirtyEight Elo predictions
- results/fivethirtyeight_elo/fivethirtyeight_elo_half_full_log_loss.csv contains second half only and full season Log Loss for each of the four league based on FiveThirtyEight Elo predictions

### results/moneyline/
- Folder that contains results of moneyline based probabilistic predictions for the four leagues
    - results/moneyline/brier/
        - Folder that contains a file for each of the four leagues that has the Brier score of moneyline based and baseline prediction models (and FivethirtyEight Elo model for NFL)
    - results/moneyline/seasonal/
        - Folder that contains a file for each of the four leagues that has the seasonal Brier score, log loss, AUC, and three different Brier skill loss scores by season
            - brier_skill_loss_50_50 (baseline is 50/50 coinflip model)
            - brier_skill_loss_home_prob_grouped (baseline is home team's historical home win probability based model)
            - brier_skill_loss_home_prob_overall (baseline is historical home win probability based model)
    - results/moneyline/teamwise/
        - Folder that contains a file for each of the four leagues that has the teamwise Brier score, log loss, AUC, and the same three Brier skill loss scores as above
    - results/moneyline/moneyline_half_full_brier.csv contains second half only and full season Brier scores for each of the four league based on moneyline predictions
    - results/moneyline/moneyline_half_full_log_loss.csv contains second half only and full season Log Loss for each of the four league based on moneyline predictions
    
### results/ratingslib/
- See [RatingsLib](https://github.com/ktalattinis/ratingslib) for documentation and more
- Folder that contains results of RatingsLib based probabilistic predictions for the four leagues
    - {league}_full_ratingslib_predictions.csv has the gamewise probabilistic predictions for all games using the Elo Point, Elo Win, Keener, Massey, and Offense-Defense ratings
    - ratingslib_half_full_brier.csv contains RatingsLib based Brier score of all leagues and ratings based on second half only and full season
    - ratingslib_half_full_log_loss.csv contains RatingsLib based Log Loss of all leagues and ratings based on second half only and full season
- Also contains parallel version of each file with only second half of season games

### results/binary_accuracy.csv
- Contains binary accuracy of moneyline based predictions in the four leagues

### results/calibration_statistics.csv
- Contains the counts and normalized counts of each bin of every plot in calibration plots

### results/combined_half_full_brier.csv
- Contains the second half only and full season Brier scores for moneyline, FiveThirtyEight Elo, RatingsLib, and Bradley-Terry based prediction models

### results/combined_half_full_log_loss.csv
- Contains the second half only and full season Log Loss for moneyline, FiveThirtyEight Elo, RatingsLib, and Bradley-Terry based prediction models

### results/fivethirtyeight_competition.csv
- Contains the placement and percentile of a hypothetical player using moneyline based probabilistic predictions in the FiveThirtyEight NFL prediction competition

- ### results/nfl_teamwise_winrate.csv
- Contains the win rate for all 32 NFL teams across all seasons in the range