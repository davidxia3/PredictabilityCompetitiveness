import os
import json

main_folder = 'data/nfl'

for subfolder in os.listdir(main_folder):
    subfolder_path = os.path.join(main_folder, subfolder)
    
    if os.path.isdir(subfolder_path):
        games_file = os.path.join(subfolder_path, 'games.json')
        market_file = os.path.join(subfolder_path, 'market.json')
        
        try:
            with open(games_file, 'r') as f:
                games_data = json.load(f)
            with open(market_file, 'r') as f:
                market_data = json.load(f)
            
            print(f"Difference found in {subfolder}:")
            print(len(games_data)- len(market_data))

        except Exception as e:
            print(f"Error in {subfolder}: {e}")
