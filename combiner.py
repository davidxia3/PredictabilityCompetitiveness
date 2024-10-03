import json

mlb_teams = [
    "angels", "astros", "athletics", "bluejays", "braves", "brewers", "cardinals", "cubs", "diamondbacks", "dodgers", "giants",
    "guardians", "mariners", "marlins", "mets", "nationals", "orioles", "padres", "phillies", "pirates", "rangers", "rays",
    "reds", "redsox", "rockies", "royals", "tigers", "twins", "whitesox", "yankees"
]

league = "mlb"
file = "market"
output_file = f'data/{league}/combined/combined_{file}.json'

combined_list = []
id_set = set()

for team in mlb_teams:
    file_path = f'data/{league}/{team}/{file}.json'
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                for item in data:
                    item_id = item.get("game_url")
                    if item_id and item_id not in id_set:
                        combined_list.append(item)
                        id_set.add(item_id)
            else:
                print(f"Warning: {file_path} does not contain a list")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

with open(output_file, 'w') as outfile:
    json.dump(combined_list, outfile, indent=4)

print(f"Combined JSON list saved to {output_file} with unique IDs.")
