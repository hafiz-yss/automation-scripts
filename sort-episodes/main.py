import os

downloads_folder = os.path.expanduser("~/Downloads")

series_name = input("Enter the TV series name: ")
target_folder = os.path.expanduser(f"~/videos/{series_name}")

print(f"Moving files from {downloads_folder} to {target_folder}")
print("Checking downloaded files...")

# Scan files in Downloads folder
if os.path.exists(downloads_folder):
    for file in os.listdir(downloads_folder):
        if series_name.lower() in file.lower():
            print(f"Found: {file}")
else:
    print("Downloads folder does not exist.")
