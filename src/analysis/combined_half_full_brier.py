import pandas as pd

files = ['results/moneyline/moneyline_half_full_brier.csv',
         'results/fivethirtyeight_elo/fivethirtyeight_elo_half_full_brier.csv',
         'results/ratingslib/ratingslib_half_full_brier.csv',
         'results/bradley_terry/bradley_terry_half_full_brier.csv']

df_list = [pd.read_csv(file) for file in files]
df_combined = pd.concat(df_list, ignore_index=True)

df_combined.to_csv("results/combined_half_full_brier.csv", index=False)

