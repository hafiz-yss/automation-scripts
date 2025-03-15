import subprocess
import tkinter as tk
from tkinter import filedialog
import time

def select_folder():
    """Open a folder selection dialog and launch MongoDB, VS Code, and Chrome."""
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        launch(selected_folder)

def launch(path):
    """Launch MongoDB, VS Code in the selected folder, and open Chrome with localhost:3000."""
    
    commands = [
        "start cmd /k mongod",  # Start MongoDB
        f'start cmd /k "cd /d {path} && code ."',  # Open VS Code
        "start chrome"  # Open Chrome
    ]

    for cmd in commands:
        subprocess.Popen(cmd, shell=True)
        time.sleep(2) 

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    select_folder()
