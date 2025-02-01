from ratingslib.ratings.elo import Elo
from ratingslib.utils.enums import ratings

league = "mlb"

df = Elo(version=ratings.ELOWIN, starting_point=0).rate_from_file(f'processed_data/{league}_ratingslib_formatted.csv')

df = df.sort_values(by='ranking', ascending=True)

df.to_csv(f'results/{league}_elowin_rankings.csv', index=False)
