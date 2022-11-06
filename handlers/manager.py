import gevent
import logging

from handlers.server import RequestHandler

logger = logging.getLogger('info_logger')


class Manager:

    def __init__(self, config):
        self.request_handler = RequestHandler(config=config)

        logger.info('Manager object was successfully created!')

    def start(self):
        self.__run_server()

    def __run_server(self):
        self.request_handler.start()
