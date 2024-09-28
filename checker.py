import json

def check_field_is_int(filename, field_name):
    with open(filename, 'r') as file:
        data = json.load(file)

    for idx, entry in enumerate(data):
        if field_name not in entry:
            print(f"Entry {idx + 1} is missing the field '{field_name}'")
            return False
        if not isinstance(entry[field_name], int):
            print(f"Entry {idx + 1} has a non-integer value for '{field_name}': {entry[field_name]}")
            return False

    print("All entries have the specified field and the value is an integer.")
    return True

# Define the path to your JSON file and the field to check
filename = "data/mlb/athletics/market.json"  # Replace with your JSON file

# Run the check
check_field_is_int(filename, "avg_moneyline_1")
check_field_is_int(filename, "avg_moneyline_2")
check_field_is_int(filename, "high_moneyline_1")
check_field_is_int(filename, "high_moneyline_2")


