import pandas as pd
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

league = "mlb"

df = pd.read_csv(f'data/master/{league}_market.csv')

y_true = df['result'].values 
y_prob = df['avg_prob_1'].values 

fpr, tpr, thresholds = roc_curve(y_true, y_prob)

roc_auc = auc(fpr, tpr)

print("AUC:", roc_auc)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = {:.2f})'.format(roc_auc))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.legend(loc="lower right")
plt.savefig(f'figures/{league}_auc_curve.png')

# plt.show()

