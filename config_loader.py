import json
from constants import constants


def config_loader(config):
    config_path = constants.get(config)
    with open(config_path) as file:
        config = json.load(file)
    return config
