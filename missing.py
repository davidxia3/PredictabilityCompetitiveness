import json

games_file = 'data/nba/clippers/games.json'
market_file = 'data/nba/clippers/market.json'

sport = "basketball"

with open(games_file, 'r') as f:
    games_data = json.load(f)

with open(market_file, 'r') as f:
    market_data = json.load(f)

games_urls = {game['game_url'] for game in games_data if 'game_url' in game}
market_urls = {market['game_url'] for market in market_data if 'game_url' in market}

urls_diff = games_urls - market_urls

if urls_diff:
    print("Game URLs in games.json but not in market.json:")
    for url in urls_diff:
        print(f'https://www.oddsportal.com/{sport}/'  + url)
else:
    print("No differences found.")
