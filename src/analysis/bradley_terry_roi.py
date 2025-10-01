import pandas as pd


leagues = ["mlb", "nfl", "nba", "nhl"]



total_df_out = pd.DataFrame(columns=[
        "league",
        "n", 
        "favorite_roi", 
        "underdog_roi"
])

for league in leagues:

    bt_df = pd.read_csv(f"results/bradley_terry/{league}_bradley_terry_predictions.csv")

    if league == "nfl":
        ml_df = pd.read_csv(f"processed_data/combined/{league}_espn_combined_with_elo.csv")
    else:
        ml_df = pd.read_csv(f"processed_data/combined/{league}_espn_combined.csv")

    if len(bt_df) != len(ml_df):
        print(f"!!! ({league}) non matching lengths")
        continue

    total_n = 0
    total_favorite_invested = 0
    total_favorite_revenue = 0
    total_underdog_invested = 0
    total_underdog_revenue = 0

    n = [0,0,0,0,0,0,0,0,0,0]
    favorite_invested = [0,0,0,0,0,0,0,0,0,0]
    favorite_revenue = [0,0,0,0,0,0,0,0,0,0]
    underdog_invested = [0,0,0,0,0,0,0,0,0,0]
    underdog_revenue = [0,0,0,0,0,0,0,0,0,0]

    seasonal_n = {}
    seasonal_favorite_invested = {}
    seasonal_favorite_revenue = {}
    seasonal_underdog_invested = {}
    seasonal_underdog_revenue = {}
    seasonal_favorite_roi = {}
    seasonal_underdog_roi = {}

    for idx, bt_row in bt_df.iterrows():
        if bt_row.isna().any():
            continue

        ml_row = ml_df.iloc[idx]

        
        if (ml_row["team_1"] != bt_row["HomeTeam"]) or (ml_row["team_2"] != bt_row["AwayTeam"]):
            print("!!! mismatch")
            continue


        tournament = ml_row["tournament"]

        if tournament not in seasonal_n:
            seasonal_n[tournament] = [0,0,0,0,0,0,0,0,0,0]
            seasonal_favorite_invested[tournament] = [0,0,0,0,0,0,0,0,0,0]
            seasonal_favorite_revenue[tournament] = [0,0,0,0,0,0,0,0,0,0]
            seasonal_underdog_invested[tournament] = [0,0,0,0,0,0,0,0,0,0]
            seasonal_underdog_revenue[tournament] = [0,0,0,0,0,0,0,0,0,0]
            seasonal_favorite_roi[tournament] = [0,0,0,0,0,0,0,0,0,0]
            seasonal_underdog_roi[tournament] = [0,0,0,0,0,0,0,0,0,0]


        bt_prob = bt_row["bradley_terry_prediction"]
        bin = int(prob * 10)
        if bin == 10:
            bin = 9

        total_n += 1
        n[bin] += 1
        seasonal_n[tournament][bin] += 1

        ml1 = ml_row["avg_moneyline_1"]
        ml2 = ml_row["avg_moneyline_2"]
        result = ml_row["result"]

        def payout(ml, win):
            if ml < 0:
                odds = 100 / abs(ml)
            else:
                odds = ml / 100
            return (100 + 100 * odds) * win

        if bt_prob >= 0.5:  
            game_favorite_revenue = payout(ml1, result)
            game_underdog_revenue = payout(ml2, 1 - result)
        else:
            game_favorite_revenue = payout(ml2, 1 - result)
            game_underdog_revenue = payout(ml1, result)

        total_favorite_invested += 100
        total_favorite_revenue += game_favorite_revenue

        total_underdog_invested += 100
        total_underdog_revenue += game_underdog_revenue

        favorite_invested[bin] += 100
        favorite_revenue[bin] += game_favorite_revenue

        underdog_invested[bin] += 100
        underdog_revenue[bin] += game_underdog_revenue

        seasonal_favorite_invested[tournament][bin] += 100
        seasonal_favorite_revenue[tournament][bin] += game_favorite_revenue

        seasonal_underdog_invested[tournament][bin] += 100
        seasonal_underdog_revenue[tournament][bin] += game_underdog_revenue


    if total_favorite_invested == 0:
        total_favorite_roi = -2
    else:
        total_favorite_roi = (total_favorite_revenue / total_favorite_invested) - 1

    if total_underdog_invested == 0:
        total_underdog_roi = -2
    else:
        total_underdog_roi = (total_underdog_revenue / total_underdog_invested) - 1

    total_df_out.loc[len(total_df_out)] = [league, total_n, total_favorite_roi, total_underdog_roi]

    total_df_out.to_csv(f"results/bradley_terry_roi/total_roi.csv", index=False)


    favorite_roi = [0,0,0,0,0,0,0,0,0,0]
    underdog_roi = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        if favorite_invested[i] == 0:
            favorite_roi[i] = -2
        else:
            favorite_roi[i] = (favorite_revenue[i]/favorite_invested[i]) - 1
        if underdog_invested[i] == 0:
            underdog_roi[i] = -2
        else:
            underdog_roi[i] = (underdog_revenue[i]/underdog_invested[i]) - 1

    df_out = pd.DataFrame({
        "bin": list(range(10)),
        "n": n,
        "favorite_roi": favorite_roi,
        "underdog_roi": underdog_roi
    })

    df_out.to_csv(f"results/bradley_terry_roi/{league}_binned_roi.csv", index=False)


    df_out = pd.DataFrame(columns=[
        "season",
        "bin", 
        "n", 
        "favorite_roi", 
        "underdog_roi"
    ])

    for tourny in seasonal_n.keys():
        for i in range(10):
            if seasonal_favorite_invested[tourny][i] == 0:
                seasonal_favorite_roi[tourny][i] = -2
            else:
                seasonal_favorite_roi[tourny][i] = (seasonal_favorite_revenue[tourny][i]/seasonal_favorite_invested[tourny][i]) - 1

            if seasonal_underdog_invested[tourny][i] == 0:
                seasonal_underdog_roi[tourny][i] = -2
            else:
                seasonal_underdog_roi[tourny][i] = (seasonal_underdog_revenue[tourny][i]/seasonal_underdog_invested[tourny][i]) - 1


            df_out.loc[len(df_out)] = [tourny, i, seasonal_n[tourny][i], seasonal_favorite_roi[tourny][i], seasonal_underdog_roi[tourny][i]]


    df_out.to_csv(f"results/bradley_terry_roi/{league}_seasonal_binned_roi.csv", index=False)

        

