import os

BASE_PATH = os.path.abspath(__file__)

config_constants = {
    'general': os.path.join(os.path.dirname(BASE_PATH), 'general_config.json'),
    'logger': os.path.join(os.path.dirname(BASE_PATH), 'logger.json')
}

sensitive_fields = {
    'password',
    'token'
}
