import os
import config

config.create_default_config()

config.load_config()
sorting_path = config.get_sorting_path()
folders = config.load_folders()

try:
    os.mkdir(sorting_path)
    print("Documents Folder created")
except FileNotFoundError:
    print("Documents Folder couldn't be located")
except FileExistsError:
    print("Sorted Folder already exists")

for folder in folders:
    try:
        os.mkdir(folders[folder])
        print(f"{folder} Folder created")
    except FileNotFoundError:
        print("Documents or Sorted Folder couldn't be located")
    except FileExistsError:
        print(f"{folder} Folder already exists")
