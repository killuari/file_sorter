import configparser
import os

config = configparser.ConfigParser()
config_file = 'settings.ini'

def create_default_config():
    """create settings file with default values"""

    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    sorting_path = os.path.join(os.path.expanduser('~'), 'Documents\Sorted')

    config['paths'] = {
        'downloads_path': downloads_path,
        'sorting_path': sorting_path
    }

    config['folders'] = {
        'documents': f"{sorting_path}\documents",
        'images': f"{sorting_path}\images",
        'videos': f"{sorting_path}\\videos",
        'audios': f"{sorting_path}\\audios",
        'executables': f"{sorting_path}\executables",
        'archives': f"{sorting_path}\\archives",
        'other': f"{sorting_path}\other",
    }

    config['extensions'] = {
        'documents': '.doc, .docx, .odt, .pdf, .xls, .xlsx, .ppt, .pptx',
        'images': '.jpg, .jpeg, .jif, .jfif, .png, .gif, .webp, .tiff, .tif, .psd, .raw, .arw, .bmp, .dib, .ind, .jp2, .jpf, .svg',
        'videos': '.webm, .mpg, .mp2, .mpeg, .mpe, .mpv, .ogg, .mp4, .mp4v, .avi, .wmv, .mov, .qt, .flv, .swf, .MTS',
        'audios': '.m4a, .flac, .mp3, .wav, .wma, .aac',
        'executables': '.exe',
        'archives': '.zip, .rar',
    }
    
    with open(config_file, 'w') as configfile:
        config.write(configfile)

def load_config():
    """load settings file"""

    if not os.path.exists(config_file):
        create_default_config()

    config.read(config_file)

def load_extensions(type=None):
    extensions = {}
    if type is None:
        for extension in config.options('extensions'):
            extensions[extension] = load_extensions(extension)
        return extensions
    return config.get('extensions', type).split(', ')

def load_folders(type=None):
    folders = {}
    if type is None:
        for folder in config.options('folders'):
            folders[folder] = load_folders(folder)
        return folders
    return config.get('folders', type)

def get_sorting_path():
    return config.get('paths', 'sorting_path')

def get_downloads_path():
    return config.get('paths', 'downloads_path')
