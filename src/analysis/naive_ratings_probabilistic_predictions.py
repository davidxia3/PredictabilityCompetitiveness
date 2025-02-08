import pandas as pd
import numpy as np

leagues = ['nfl', 'nhl', 'mlb','nba']
ratingtypes = ["elopoint", "elowin", "keener", "massey"]

for ratingtype in ratingtypes:
    for league in leagues:
        df = pd.read_csv(f'results/ratings/{ratingtype}/{league}_{ratingtype}_rankings.csv')

        ratings = df["rating"].values

        rating_matrix = ratings[:, None] / (ratings[:, None] + ratings[None, :])

        np.fill_diagonal(rating_matrix, 0.5)

        rating_matrix = np.round(rating_matrix, 4)

        df_matrix = pd.DataFrame(rating_matrix)


        df_matrix.to_csv(f'results/ratings/{ratingtype}/{league}_{ratingtype}_predictions.csv', index=False)