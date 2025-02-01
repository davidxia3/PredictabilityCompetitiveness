from ratingslib.ratings.elo import Elo
from ratingslib.utils.enums import ratings

league = "nfl"

df = Elo(version=ratings.ELOPOINT, starting_point=0).rate_from_file(f'processed_data/{league}_ratingslib_formatted.csv')

df = df.sort_values(by='ranking', ascending=True)

df.to_csv(f'results/{league}_elopoint_rankings.csv', index=False)