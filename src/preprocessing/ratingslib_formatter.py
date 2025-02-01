import pandas as pd

league = "nba"

df = pd.read_csv(f'processed_data/{league}_espn_combined.csv')

df['Date'] = pd.to_datetime(df['date'], format='%d-%m-%Y').dt.strftime('%d/%m/%Y')

df.rename(columns={
    'team_1': 'HomeTeam',
    'team_2': 'AwayTeam',
    'score_1': 'FTHG',
    'score_2': 'FTAG'
}, inplace=True)

df = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']]

df.to_csv(f'processed_data/{league}_ratingslib_formatted.csv', index=False)

