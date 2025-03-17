# RatingsLib Documentation

## Contains all scripts to analyze and produce results from processed RatingsLib data
See [RatingsLib](https://github.com/ktalattinis/ratingslib) for documentation and more

### src/analysis/ratingslib/ratingslib_gamewise.py
- Computes the Elo Point, Elo Win, Keener, Massey, and Offense-Defense ratings for every game and converts to probabilistic predictions
- For every game, the games that happen previously in the same season are used to generate the ratings
- Results are saved to results/ratingslib/{league}_ratingslib_predictions.csv

### src/analysis/ratingslib/ratingslib_half_full_brier.py
- Computes the Brier scores for predictions based on the Elo Point, Elo Win, Keener, Massey, and Offense-Defense ratings
- Computes both second half only and full season Brier scores
- Results are saved to results/ratingslib/ratingslib_half_full_brier.csv
