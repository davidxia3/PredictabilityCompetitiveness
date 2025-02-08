from ratingslib.ratings.elo import Elo
from ratingslib.ratings.keener import Keener
from ratingslib.ratings.massey import Massey
from ratingslib.utils.enums import ratings
from ratingslib.ratings.methods import normalization_rating

leagues = ['nfl', 'nhl', 'mlb','nba']

for league in leagues:

    elopoint = Elo(version=ratings.ELOPOINT, starting_point=0).rate_from_file(f'processed_data/{league}_ratingslib_formatted.csv')
    elopoint = elopoint.sort_values(by='ranking', ascending=True)
    elopoint['rating'] = normalization_rating(elopoint, "rating")
    elopoint.to_csv(f'results/ratings/elopoint/{league}_elopoint_rankings.csv', index=False)

    elowin = Elo(version=ratings.ELOWIN, starting_point=0).rate_from_file(f'processed_data/{league}_ratingslib_formatted.csv')
    elowin = elowin.sort_values(by='ranking', ascending=True)
    elowin['rating'] = normalization_rating(elowin, "rating")
    elowin.to_csv(f'results/ratings/elowin/{league}_elowin_rankings.csv', index=False)

    keener = Keener(normalization=False).rate_from_file(f'processed_data/{league}_ratingslib_formatted.csv')
    keener = keener.sort_values(by='ranking', ascending=True)
    keener['rating'] = normalization_rating(keener, "rating")
    keener.to_csv(f'results/ratings/keener/{league}_keener_rankings.csv', index=False)

    massey = Massey().rate_from_file(f'processed_data/{league}_ratingslib_formatted.csv')
    massey = massey.sort_values(by='ranking', ascending=True)
    massey['rating'] = normalization_rating(massey, "rating")
    massey.to_csv(f'results/ratings/massey/{league}_massey_rankings.csv', index=False)