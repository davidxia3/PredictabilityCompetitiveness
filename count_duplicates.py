import json

input_file = 'data/basketball/bucks/market.json' 
output_file = 'data/basketball/bucks/market.json'  

with open(input_file, 'r') as f:
    data = json.load(f)

seen_ids = set()

filtered_data = []
for item in data:
    if item['id'] not in seen_ids:
        filtered_data.append(item)
        seen_ids.add(item['id'])

with open(output_file, 'w') as f:
    json.dump(filtered_data, f, indent=4)

print(f"Filtered data saved to {output_file}")
