import pandas as pd
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve


leagues = ["nfl", "nba", "mlb", "nhl"]

halves = ['', "_half"]


def get_calibration_with_counts(df, col, x, y, n):
    prob_true, prob_pred = calibration_curve(x, y, n_bins=n, strategy='uniform')

    bin_counts = [0] * 10

    for _, row in df.iterrows():
        prediction = str(row[col])
        lead = int(prediction.split(".")[1][0:1])
        bin_counts[lead] = bin_counts[lead] + 1

    props = [round(i/len(df),4) for i in bin_counts]

    return prob_true, prob_pred, bin_counts, props


distribution_data = []

for league in leagues:
    for half in halves:

        plt.figure(figsize=(10, 6))
        plt.plot([0, 1], [0, 0], linestyle='--', color='gray', label='Perfect Calibration',linewidth=3, markersize=10)
        plt.xlim(0, 1)
        plt.ylim(-0.5, 0.5)
        plt.xlabel('Predicted Win Probability', fontsize=20)
        plt.ylabel('Normalized Actual Win Frequency', fontsize=20)
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

            prob_true1, prob_pred1, ml_counts, ml_props = get_calibration_with_counts(ml_df, 'avg_prob_1', actual_results, c1, 10)
            prob_true2, prob_pred2, elo_counts, elo_props = get_calibration_with_counts(ml_df, 'elo_prob_1', actual_results, c2, 10)

            ml_count_row = {'name': 'nfl_ml_counts'+half}
            ml_count_row.update({f'bin_{i+1}': val for i, val in enumerate(ml_counts)})
            distribution_data.append(ml_count_row)

            ml_prop_row = {'name': 'nfl_ml_props'+half}
            ml_prop_row.update({f'bin_{i+1}': val for i, val in enumerate(ml_props)})
            distribution_data.append(ml_prop_row)

            elo_count_row = {'name': 'nfl_elo_counts'+half}
            elo_count_row.update({f'bin_{i+1}': val for i, val in enumerate(elo_counts)})
            distribution_data.append(elo_count_row)

            elo_prop_row = {'name': 'nfl_elo_props'+half}
            elo_prop_row.update({f'bin_{i+1}': val for i, val in enumerate(elo_props)})
            distribution_data.append(elo_prop_row)
            

            plt.plot(prob_pred1, prob_true1 - prob_pred1, marker='o', label='Betting Market Model', color='green',linewidth=3, markersize=10)
            plt.plot(prob_pred2, prob_true2 - prob_pred2, marker='o', label='Elo Model', color='magenta',linewidth=3, markersize=10)

        else:
            ml_df = ml_df[ml_df[['avg_prob_1']].notnull().all(axis=1)]

            c1 = ml_df["avg_prob_1"]
            actual_results = ml_df["result"]

            prob_true1, prob_pred1, ml_counts, ml_props = get_calibration_with_counts(ml_df, 'avg_prob_1', actual_results, c1, 10)
            
            ml_count_row = {'name': league + '_ml_counts'+half}
            ml_count_row.update({f'bin_{i+1}': val for i, val in enumerate(ml_counts)})
            distribution_data.append(ml_count_row)

            ml_prop_row = {'name': league + '_ml_props'+half}
            ml_prop_row.update({f'bin_{i+1}': val for i, val in enumerate(ml_props)})
            distribution_data.append(ml_prop_row)

            plt.plot(prob_pred1, prob_true1 - prob_pred1, marker='o', label='Betting Market Model', color='green',linewidth=3, markersize=10)


        bt_df = pd.read_csv(bradley_terry_path)
        bt_df = bt_df[bt_df[['bradley_terry_prediction']].notnull().all(axis=1)]
        c1 = bt_df["bradley_terry_prediction"]
        actual_results = (bt_df["FTHG"] > bt_df["FTAG"]).astype(int)

        prob_true1, prob_pred1, bt_counts, bt_props = get_calibration_with_counts(bt_df, 'bradley_terry_prediction', actual_results, c1, 10)

        bt_count_row = {'name': league + '_bt_counts'+half}
        bt_count_row.update({f'bin_{i+1}': val for i, val in enumerate(bt_counts)})
        distribution_data.append(bt_count_row)

        bt_prop_row = {'name': league + '_bt_props'+half}
        bt_prop_row.update({f'bin_{i+1}': val for i, val in enumerate(bt_props)})
        distribution_data.append(bt_prop_row)

        plt.plot(prob_pred1, prob_true1 - prob_pred1, marker='o', label='Bradley-Terry Model', color='blue',linewidth=3, markersize=10)



        rl_df = pd.read_csv(ratingslib_path)
        rl_df = rl_df[rl_df[['elopoint_prediction', 'elowin_prediction', 'keener_prediction', 'massey_prediction', 'od_prediction']].notnull().all(axis=1)]
        c1 = rl_df["elopoint_prediction"]
        c2 = rl_df["elowin_prediction"]
        c3 = rl_df["keener_prediction"]
        c4 = rl_df["massey_prediction"]
        c5 = rl_df["od_prediction"]
        actual_results = (rl_df["FTHG"] > rl_df["FTAG"]).astype(int)

        prob_true1, prob_pred1, ep_counts, ep_props = get_calibration_with_counts(rl_df, 'elopoint_prediction', actual_results, c1, 10)
        prob_true2, prob_pred2, ew_counts, ew_props = get_calibration_with_counts(rl_df, 'elowin_prediction',actual_results, c2, 10)
        prob_true3, prob_pred3, ke_counts, ke_props = get_calibration_with_counts(rl_df, 'keener_prediction',actual_results, c3, 10)
        prob_true4, prob_pred4, ma_counts, ma_props = get_calibration_with_counts(rl_df, 'massey_prediction',actual_results, c4, 10)
        prob_true5, prob_pred5, od_counts, od_props = get_calibration_with_counts(rl_df, 'od_prediction',actual_results, c5, 10)

        ep_count_row = {'name': league + '_ep_counts'+half}
        ep_count_row.update({f'bin_{i+1}': val for i, val in enumerate(ew_counts)})
        distribution_data.append(ep_count_row)

        ep_prop_row = {'name': league + '_ep_props'+half}
        ep_prop_row.update({f'bin_{i+1}': val for i, val in enumerate(ew_props)})
        distribution_data.append(ep_prop_row)

        ew_count_row = {'name': league + '_ew_counts'+half}
        ew_count_row.update({f'bin_{i+1}': val for i, val in enumerate(ew_counts)})
        distribution_data.append(ew_count_row)
        
        ew_prop_row = {'name': league + '_ew_props'+half}
        ew_prop_row.update({f'bin_{i+1}': val for i, val in enumerate(ew_props)})
        distribution_data.append(ew_prop_row)

        ke_count_row = {'name': league + '_ke_counts'+half}
        ke_count_row.update({f'bin_{i+1}': val for i, val in enumerate(ke_counts)})
        distribution_data.append(ke_count_row)
        
        ke_prop_row = {'name': league + '_ke_props'+half}
        ke_prop_row.update({f'bin_{i+1}': val for i, val in enumerate(ke_props)})
        distribution_data.append(ke_prop_row)

        ma_count_row = {'name': league + '_ma_counts'+half}
        ma_count_row.update({f'bin_{i+1}': val for i, val in enumerate(ma_counts)})
        distribution_data.append(ma_count_row)
        
        ma_prop_row = {'name': league + '_ma_props'+half}
        ma_prop_row.update({f'bin_{i+1}': val for i, val in enumerate(ma_props)})
        distribution_data.append(ma_prop_row)

        od_count_row = {'name': league + '_od_counts'+half}
        od_count_row.update({f'bin_{i+1}': val for i, val in enumerate(od_counts)})
        distribution_data.append(od_count_row)
        
        od_prop_row = {'name': league + '_od_props'+half}
        od_prop_row.update({f'bin_{i+1}': val for i, val in enumerate(od_props)})
        distribution_data.append(od_prop_row)

        ratingslib_avg = [sum(x) / len(x) for x in zip(*[prob_true1, prob_true2, prob_true3, prob_true4, prob_true5])]


        plt.plot(prob_pred1, ratingslib_avg - prob_pred1, marker='o', label='Ratingslib Average', color='red', linewidth=3, markersize=10)


        plt.legend()
        plt.tight_layout()
        plt.savefig(f'figures/calibration/{league}{half}_calibration.png', dpi=300, bbox_inches='tight')
        plt.close()


df = pd.DataFrame(distribution_data)
df.to_csv(f'results/calibration_statistics.csv', index=False)