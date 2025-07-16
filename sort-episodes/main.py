import os

downloads_folder = os.path.expanduser("~/Downloads")

series_name = input("Enter the TV series name: ")
target_folder = os.path.expanduser(f"~/videos/{series_name}")

print(f"Moving files from {downloads_folder} to {target_folder}")
