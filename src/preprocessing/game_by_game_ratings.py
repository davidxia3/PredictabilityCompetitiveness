import pandas as pd
from ratingslib.ratings.elo import Elo
from ratingslib.ratings.keener import Keener
from ratingslib.ratings.massey import Massey
from ratingslib.utils.enums import ratings
from ratingslib.ratings.methods import normalization_rating

leagues = ['nfl','nba','mlb','nhl']

for league in leagues:

    df = pd.read_csv(f'processed_data/{league}_ratingslib_formatted.csv')

    unique_teams = pd.unique(df[['HomeTeam', 'AwayTeam']].values.ravel())
    unique_teams_df = pd.DataFrame(unique_teams, columns=['Item'])

    df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")

    df["elopoint_prediction"] = None
    df["elowin_prediction"] = None
    df["keener_prediction"] = None
    df["massey_prediction"] = None

    for index, row in df.iterrows():
        filtered_df = df[(df['Date'] < row['Date']) & (df['Season'] == row['Season'])]

        elopoint = Elo(version=ratings.ELOPOINT, starting_point=0).rate(filtered_df, unique_teams_df)
        elopoint['rating'] = normalization_rating(elopoint, "rating")

        elowin = Elo(version=ratings.ELOWIN, starting_point=0).rate(filtered_df, unique_teams_df)
        elowin['rating'] = normalization_rating(elowin, "rating")

        keener = Keener(normalization=False).rate(filtered_df, unique_teams_df)
        keener['rating'] = normalization_rating(keener, "rating")

        massey = Massey().rate(filtered_df, unique_teams_df)
        massey['rating'] = normalization_rating(massey, "rating")



        home = row['HomeTeam']
        away = row['AwayTeam']

        ep_home = elopoint[elopoint["Item"] == home].iloc[0]["rating"]
        ep_away = elopoint[elopoint["Item"] == away].iloc[0]["rating"]
        df.at[index, "elopoint_prediction"] = ep_home / (ep_home + ep_away)

        ew_home = elowin[elowin["Item"] == home].iloc[0]["rating"]
        ew_away = elowin[elowin["Item"] == away].iloc[0]["rating"]
        df.at[index, "elowin_prediction"] = ew_home / (ew_home + ew_away)

        keener_home = keener[keener["Item"] == home].iloc[0]["rating"]
        keener_away = keener[keener["Item"] == away].iloc[0]["rating"]
        df.at[index, "keener_prediction"] = keener_home / (keener_home + keener_away)

        massey_home = massey[massey["Item"] == home].iloc[0]["rating"]
        massey_away = massey[massey["Item"] == away].iloc[0]["rating"]
        df.at[index, "massey_prediction"] = massey_home / (massey_home + massey_away)


    df.to_csv(f'processed_data/{league}_ratingslib_predictions.csv', index=False)
