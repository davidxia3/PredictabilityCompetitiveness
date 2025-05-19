# Bradley-Terry Documentation

## Contains all scripts to analyze and produce results from processed Bradley-Terry data

### src/analysis/bradley_terry/bradley_terry_gamewise.py
- Computes the Bradley-Terry based probabilistic predictions for each game
- For every game, the games that happen previously in the same season are used to generate the ratings
- Prediction results are saved to results/bradley_terry/{league}_bradley_terry_predictions.csv
- Computes pre-game Bradley-Terry based ratings for the home and away team
- Rating results are saved to results/bradley_terry/{league}_bradley_terry_ratings.csv

### src/analysis/bradley_terry/bradley_terry_half_full_brier.py
- Computes the Brier scores for Bradley-Terry based predictions
- Computes both second half only and full season Brier scores
- Results are saved to results/bradley_terry/bradley_terry_half_full_brier.csv

### src/analysis/bradley_terry/bradley_terry_half_full_log_loss.py
- Computes the Log Loss for Bradley-Terry based predictions
- Computes both second half only and full season Log Loss
- Results are saved to results/bradley_terry/bradley_terry_half_full_log_loss.csv
