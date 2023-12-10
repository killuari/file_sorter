import configparser
import os

config = configparser.ConfigParser()
config_file = 'settings.ini'
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
documents_path = os.path.join(os.path.expanduser('~'), 'Documents')


def create_default_config():
    """create settings file with default values"""

    config['defaults'] = {
        'downloads_path': downloads_path,
        'sorting_interval': 'daily',
        'sorting_path': f'{documents_path}\Files'
    }
    
    with open(config_file, 'w') as configfile:
        config.write(configfile)

def load_config():
    """load settings file"""

    if not os.path.exists(config_file):
        create_default_config()

    config.read(config_file)
    return config