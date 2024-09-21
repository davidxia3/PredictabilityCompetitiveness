import json
import os

def get_json_length(file_path):
    if os.stat(file_path).st_size == 0:
        return 0
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    if isinstance(data, list):
        return len(data)
    elif isinstance(data, dict):
        return len(data)
    else:
        return 0

def print_json_lengths_recursively(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)
                length = get_json_length(file_path)
                if length > 0:
                    print(f"{file_path}: {length} items")

folder_path = 'data/basketball'
print_json_lengths_recursively(folder_path)
