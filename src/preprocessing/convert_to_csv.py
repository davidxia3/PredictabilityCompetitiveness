import pandas as pd

league = "nfl"
file = "market"

df = pd.read_json(f'data/{league}/_combined/combined_{file}.json')

df.to_csv(f'data/{league}/_combined/combined_{file}.csv', index=False)

print('converted to csv')