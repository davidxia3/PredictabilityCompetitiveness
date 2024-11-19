import pandas as pd


df = pd.read_csv('processed_data/nfl_espn_combined.csv')

seasons = ['NFL_2019', 'NFL_2020', 'NFL_2022', 'NFL_2023']

# for season in seasons:
#     score_avg = 0
#     for index, row in df.iterrows():
#         if row['tournament'] != season:
#             continue
#         if row['game_type'] != 'regular_season' and row['game_type'] != 'postseason':
#             continue

#         prediction_avg = row['avg_prob_1']*100
#         result = row['result']

#         if result == 1:
#             score_avg += 25 - (((prediction_avg-100)**2)/100)
#         else:
#             score_avg += 25 - (((prediction_avg)**2)/100)

#     print(score_avg)

placements = [39, 27, 70, 48]
totals = [15073 + 1, 15141 + 1, 9781 + 1, 9983 + 1]
percentiles = []
for i in range(len(totals)):
    percentiles.append((totals[i]-placements[i])/totals[i])


df = pd.DataFrame({'season': seasons, 'percentiles': percentiles, 'placements': placements})

df.to_csv(f'results/fivethirtyeight_results.csv', index=False)
