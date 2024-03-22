import os

# Get a list of all files in the current directory
files = os.listdir()

# Filter out only the .txt files
txt_files = [file for file in files if file.endswith('.txt')]

# Delete each .txt file
for txt_file in txt_files:
    os.remove(txt_file)
    print(f"Deleted {txt_file}")
