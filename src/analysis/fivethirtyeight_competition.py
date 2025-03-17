import pandas as pd

df = pd.read_csv('processed_data/combined/nfl_espn_combined_with_elo.csv')

seasons = ['NFL_2019', 'NFL_2020', 'NFL_2022', 'NFL_2023']

for season in seasons:
    score_avg = 0
    for index, row in df.iterrows():
        s = 0
        if row['tournament'] != season:
            continue
        if row['game_type'] != 'regular_season' and row['game_type'] != 'postseason':
            continue

        prediction_avg = row['avg_prob_1']*100
        result = row['result']

        if result == 1:
            s = 25 - (((prediction_avg-100)**2)/100)
        else:
            s = 25 - (((prediction_avg)**2)/100)

        if row['game_type'] == 'postseason':
            s = s * 2

        score_avg += s
    print(score_avg)

placements = [30, 27, 53, 11]
totals = [15073 + 1, 15141 + 1, 9781 + 1, 9983 + 1]
percentiles = []
for i in range(len(totals)):
    percentiles.append((totals[i]-placements[i])/totals[i])


df = pd.DataFrame({'season': seasons, 'percentiles': percentiles, 'placements': placements})

df.to_csv(f'results/fivethirtyeight_competition.csv', index=False)
