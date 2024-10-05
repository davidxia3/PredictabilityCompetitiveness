import pandas as pd
from sklearn.metrics import brier_score_loss

league = "nfl"

df = pd.read_csv(f'data/master/{league}_market.csv')


y_true = df['result'].values 
y_prob = df['avg_prob_1'].values

brier_score = brier_score_loss(y_true, y_prob)

print("Brier Score:", brier_score)
#0.2345882850794258