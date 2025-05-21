import os
import configparser

def get_config():
    """ get config file """    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = os.path.join(BASE_DIR, '..', 'config', 'config.ini')
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config