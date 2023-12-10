import os
import config
import shutil

# load config
config.load_config()
extensions = config.load_extensions()
folders = config.load_folders()
downloads_path = config.config.get('paths', 'downloads_path')
sorting_path = config.get_sorting_path()


with os.scandir(downloads_path) as it:
    for file in it:
        if file.is_file():
            for type in extensions:
                for extension in extensions[type]:
                    print(folders[type])
                    if file.name.endswith(extension):
                        shutil.move(file.path, folders[type])


