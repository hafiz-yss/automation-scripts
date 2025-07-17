import os
import re

def normalize_name(name):
    # Replace ., _, - with space and lowercase everything
    return re.sub(r"[._-]", " ", name).lower().strip()

downloads_folder = os.path.expanduser("~/Downloads")

series_name = input("Enter the TV series name: ")
target_folder = os.path.expanduser(f"~/videos/{series_name}")

print(f"Moving files from {downloads_folder} to {target_folder}")
print("Checking downloaded files...")

normalized_series = normalize_name(series_name)

# Scan files in Downloads folder
if os.path.exists(downloads_folder):
    for file in os.listdir(downloads_folder):
        normalized_file = normalize_name(file)

        # Better matching, check if series name appears as full word(s)
        if normalized_series in normalized_file:
            print(f"Found: {file}")
else:
    print("Downloads folder does not exist.")
