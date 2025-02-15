import pandas as pd

leagues = ['mlb','nba','nfl','nhl']

for league in leagues:
    filename = f'processed_data/{league}_espn_combined.csv'
    if league == 'nfl':
        filename = 'processed_data/nfl_espn_combined_with_elo.csv'
    df = pd.read_csv(filename)


    df['Date'] = pd.to_datetime(df['date'], format='%d-%m-%Y').dt.strftime('%d/%m/%Y')

    df.rename(columns={
        'team_1': 'HomeTeam',
        'team_2': 'AwayTeam',
        'score_1': 'FTHG',
        'score_2': 'FTAG',
        'tournament': 'Season'
    }, inplace=True)

    df = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'Season']]

    df.to_csv(f'processed_data/{league}_ratingslib_formatted.csv', index=False)

