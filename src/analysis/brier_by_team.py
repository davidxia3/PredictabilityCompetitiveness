import pandas as pd

league = 'nfl'

df = pd.read_csv(f'processed_data/{league}_espn_combined.csv')

df['pred_prob'] = df['avg_prob_1']

brier_scores = {}

teams = pd.concat([df['team_1'], df['team_2']]).unique()
tournaments = pd.concat([df['tournament']]).unique()
tournaments.sort()

for team in teams:
    team_data = []
    for tournament in tournaments:
        score = 0
        count = 0
        for index, row in df.iterrows():
            if row['tournament'] == tournament:
                if row['team_2'] == team or row['team_1'] == team:
                    count = count + 1
                    score = score + ((row['avg_prob_1'] - row['result'])**2)

        team_data.append(score/count)

    brier_scores[team] = team_data

brier_df = pd.DataFrame(brier_scores)

brier_df = brier_df.reset_index()

brier_df = brier_df.round(4)
brier_df.to_csv(f'results/{league}_team_brier.csv', index=False)

