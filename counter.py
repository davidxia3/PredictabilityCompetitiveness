import os

def count_files_in_subfolder(subfolder_path):
    # Count the number of files in the subfolder
    file_count = len([f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))])
    print(f"Number of files in '{subfolder_path}':", file_count)

# Example usage
subfolder_path = 'data/espn_mapping/nhl'  # Replace with your subfolder path
count_files_in_subfolder(subfolder_path)
