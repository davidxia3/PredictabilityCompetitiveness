from ratingslib.ratings.massey import Massey

league = "nfl"

df = Massey().rate_from_file(f'processed_data/{league}_ratingslib_formatted.csv')

df = df.sort_values(by='ranking', ascending=True)


df.to_csv(f'results/{league}_massey_rankings.csv', index=False)
