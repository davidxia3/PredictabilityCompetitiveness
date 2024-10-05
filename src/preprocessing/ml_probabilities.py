import pandas as pd
from datetime import datetime
def truncate(value):
    return float(int(value * 10**4)) / 10**4

league = "nfl"
df = pd.read_csv(f'data/{league}/_combined/combined_market.csv')

df = df.drop(df.columns[0], axis=1)

df['avg_prob_1'] = abs(df['avg_moneyline_1'])/(abs(df['avg_moneyline_1']) + abs(df['avg_moneyline_2']))
df['avg_prob_2'] = abs(df['avg_moneyline_2'])/(abs(df['avg_moneyline_2']) + abs(df['avg_moneyline_1']))

df['high_prob_1'] = abs(df['high_moneyline_1'])/(abs(df['high_moneyline_1']) + abs(df['high_moneyline_2']))
df['high_prob_2'] = abs(df['high_moneyline_2'])/(abs(df['high_moneyline_2']) + abs(df['high_moneyline_1']))

df['avg_prob_1'] = df['avg_prob_1'].apply(truncate)
df['avg_prob_2'] = df['avg_prob_2'].apply(truncate)

df['high_prob_1'] = df['high_prob_1'].apply(truncate)
df['high_prob_2'] = df['high_prob_2'].apply(truncate)


new_order = ['date','tournament', 'team_1', 'team_2', 'score_1', 'score_2', 'result', 
             'avg_moneyline_1', 'avg_moneyline_2', 'high_moneyline_1', 'high_moneyline_2', 
             'avg_prob_1', 'avg_prob_2', 'high_prob_1', 'high_prob_2',
             'game_url']
df = df[new_order]


# df['date'] = pd.to_datetime(df['date'], format="%d %B %Y").date()

df.to_csv(f'data/master/{league}_market.csv', index=False)

print("done.")
