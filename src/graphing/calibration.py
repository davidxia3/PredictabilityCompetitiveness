import pandas as pd
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve


leagues = ["nfl", "nba", "mlb", "nhl"]

halves = ['', "_half"]


for league in leagues:
    for half in halves:

        plt.figure(figsize=(10, 6))
        plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label='Perfect Calibration',linewidth=3, markersize=10)
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.xlabel('Predicted Win Probability', fontsize=20)
        plt.ylabel('Actual Win Frequency', fontsize=20)
        plt.legend(fontsize=15)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tick_params(axis='both', which='major', labelsize=15)


        suffix = ""
        if league == "nfl":
            suffix = "_with_elo"
        moneyline_path = f'processed_data/combined/{league}{half}_espn_combined{suffix}.csv'
        bradley_terry_path = f'results/bradley_terry/{league}{half}_bradley_terry_predictions.csv'
        ratingslib_path = f'results/ratingslib/{league}{half}_ratingslib_predictions.csv'

        ml_df = pd.read_csv(moneyline_path)
        if league == "nfl":
            ml_df = ml_df[ml_df[['avg_prob_1', 'elo_prob_1']].notnull().all(axis=1)]
            c1 = ml_df["avg_prob_1"]
            c2 = ml_df["elo_prob_1"]
            actual_results = ml_df["result"]

            prob_true1, prob_pred1 = calibration_curve(actual_results, c1, n_bins=10, strategy='uniform')
            prob_true2, prob_pred2 = calibration_curve(actual_results, c2, n_bins=10, strategy='uniform')

            plt.plot(prob_pred1, prob_true1, marker='o', label='Betting Market Model', color='green',linewidth=3, markersize=10)
            plt.plot(prob_pred2, prob_true2, marker='o', label='Elo Model', color='magenta',linewidth=3, markersize=10)

        else:
            ml_df = ml_df[ml_df[['avg_prob_1']].notnull().all(axis=1)]

            c1 = ml_df["avg_prob_1"]
            actual_results = ml_df["result"]

            prob_true1, prob_pred1 = calibration_curve(actual_results, c1, n_bins=10, strategy='uniform')

            plt.plot(prob_pred1, prob_true1, marker='o', label='Betting Market Model', color='green',linewidth=3, markersize=10)


        bt_df = pd.read_csv(bradley_terry_path)
        bt_df = bt_df[bt_df[['bradley_terry_prediction']].notnull().all(axis=1)]
        c1 = bt_df["bradley_terry_prediction"]
        actual_results = (bt_df["FTHG"] > bt_df["FTAG"]).astype(int)

        prob_true1, prob_pred1 = calibration_curve(actual_results, c1, n_bins=10, strategy='uniform')

        plt.plot(prob_pred1, prob_true1, marker='o', label='Bradley Terry Model', color='blue',linewidth=3, markersize=10)



        rl_df = pd.read_csv(ratingslib_path)
        rl_df = rl_df[rl_df[['elopoint_prediction', 'elowin_prediction', 'keener_prediction', 'massey_prediction', 'od_prediction']].notnull().all(axis=1)]
        c1 = rl_df["elopoint_prediction"]
        c2 = rl_df["elowin_prediction"]
        c3 = rl_df["keener_prediction"]
        c4 = rl_df["massey_prediction"]
        c5 = rl_df["od_prediction"]
        actual_results = (rl_df["FTHG"] > rl_df["FTAG"]).astype(int)

        prob_true1, prob_pred1 = calibration_curve(actual_results, c1, n_bins=10, strategy='uniform')
        prob_true2, prob_pred2 = calibration_curve(actual_results, c2, n_bins=10, strategy='uniform')
        prob_true3, prob_pred3 = calibration_curve(actual_results, c3, n_bins=10, strategy='uniform')
        prob_true4, prob_pred4 = calibration_curve(actual_results, c4, n_bins=10, strategy='uniform')
        prob_true5, prob_pred5 = calibration_curve(actual_results, c5, n_bins=10, strategy='uniform')

        plt.plot(prob_pred1, prob_true1, marker='o', label='Elo Point Model', color='crimson', linewidth=3, markersize=10)
        plt.plot(prob_pred2, prob_true2, marker='o', label='Elo Win Model', color='firebrick', linewidth=3, markersize=10)
        plt.plot(prob_pred3, prob_true3, marker='o', label='Keener Model', color='indianred', linewidth=3, markersize=10)
        plt.plot(prob_pred4, prob_true4, marker='o', label='Massey Model', color='tomato', linewidth=3, markersize=10)
        plt.plot(prob_pred5, prob_true5, marker='o', label='Offense-Defense Model', color='lightcoral', linewidth=3, markersize=10)


        plt.legend()
        plt.tight_layout()
        plt.savefig(f'figures/calibration/{league}{half}_calibration.png', dpi=300, bbox_inches='tight')
        plt.close()

        

