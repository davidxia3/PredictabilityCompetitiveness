import json

# define teams, league, and file and retrieve file
# teams =  ["bears", "bengals", "bills", "broncos", "browns", "buccaneers", "cardinals", "chargers", "chiefs",
#         "colts", "commanders", "cowboys", "dolphins", "eagles", "falcons", "fortyniners", "giants", 
#         "jaguars", "jets", "lions", "packers", "panthers", "patriots", "raiders", "rams", "ravens",
#         "saints", "seahawks", "steelers", "texans", "titans", "vikings"]

# teams = ["angels", "astros", "athletics", "bluejays", "braves", "brewers", "cardinals", "cubs", "diamondbacks", "dodgers", "giants", 
#         "guardians", "mariners", "marlins", "mets", "nationals", "orioles", "padres", "phillies", "pirates", "rangers", "rays",
#         "reds", "redsox", "rockies", "royals", "tigers", "twins", "whitesox", "yankees"]

# teams = ["bucks", "bulls", "cavaliers", "celtics", "clippers", "grizzlies", "hawks", "heat", "hornets", "jazz", "kings", "knicks",
#         "lakers", "magic", "mavericks", "nets", "nuggets", "pacers", "pelicans", "pistons", "raptors", "rockets", "seventysixers", "spurs",
#         "suns", "thunder", "timberwolves", "trailblazers", "warriors", "wizards"]

teams = ["avalanche", "blackhawks", "bluejackets", "blues", "bruins", "canadiens", "canucks", "capitals", "coyotes", "devils",
        "ducks", "flames", "flyers", "goldenknights", "hurricanes", "islanders", "jets", "kings", "kraken", "lightning", "mapleleafs", 
        "oilers", "panthers", "penguins", "predators", "rangers", "redwings", "sabres", "senators", "sharks", "stars", "wild"]

league = "nhl"
file = "market"
output_file = f'data/{league}/_combined/combined_{file}.json'


# combine files into single list
combined_list = []
id_set = set()
for team in teams:
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
                print('not valid file')
    except FileNotFoundError:
        print(team)
        print("file not found")

with open(output_file, 'w') as outfile:
    json.dump(combined_list, outfile, indent=4)

print("combined")