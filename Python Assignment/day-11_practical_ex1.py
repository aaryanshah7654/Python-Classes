# Practical Exercises
# Exercise 1: File Organizer Script

import os
import shutil
from datetime import datetime

#List files in a directory.
files = os.listdir()  

# Create a new folder named "backup_YYYY-MM-DD" using today’s date.
today = datetime.today().strftime("%Y-%m-%d")
backup_folder = f"backup_{today}"

if not os.path.exists(backup_folder):
    os.mkdir(backup_folder)

# Copy all .txt files to the backup folder.
for file in files:
    if file.endswith(".txt"):
        shutil.copy(file, backup_folder)

print(f"All .txt files backed up to folder: {backup_folder}")