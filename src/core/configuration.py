import json
import os

def load(path='../config.json'):
    config_path = os.path.join(os.path.dirname(__file__), path)
    with open(config_path, 'r', errors='ignore', encoding='UTF-8') as file:
        config = json.load(file)
    return config