import os, shutil
import config

def sort():
    # load config
    config.load_config()
    extensions = config.load_extensions()
    folders = config.load_folders()
    downloads_path = config.get_downloads_path()

    with os.scandir(downloads_path) as it:
        for file in it:
            if file.is_file() and not file.name.endswith(".tmp") and not file.name.endswith('.crdownload'):
                moved = False
                for type in extensions:
                    for extension in extensions[type]:
                        if file.name.endswith(extension):
                            try:
                                shutil.move(file.path, folders[type])
                                moved = True
                            except shutil.Error as e:
                                print(e)
                if not moved:
                    try:
                        shutil.move(file.path, folders['other'])
                    except shutil.Error as e:
                        print(e)

