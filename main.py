import logging
import logging.config

from config_loader import config_loader
from handlers.manager import Manager


def run():
    logger_config = config_loader(config='logger')
    print(logger_config)
    logging.config.dictConfig(logger_config)
    proxy_logger = logging.getLogger('info_logger')
    proxy_logger.info('Try to load general configs...')
    general_config = config_loader(config='general')
    proxy_logger.info('General configs successfully loaded!')

    manager = Manager(config=general_config)
    manager.start()

if __name__ == '__main__':
    run()
