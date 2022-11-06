import json
import logging
import requests
from uuid import uuid1
from gevent.pool import Pool
from gevent.pywsgi import WSGIServer

from constants import sensitive_fields

logger = logging.getLogger('info_logger')


class RequestHandler:

    def __init__(self, config):
        self.host = config['general']['host']
        self.port = config['general']['port']
        self.pool_size = config['general']['workers_pool'] + 1
        self.gevent_pool = Pool(self.pool_size)
        self.base_url = config['general']['base_url']
        self.methods_mapper = config['general']['methods_mapper']
        self.cache = {}

    def start(self):
        WSGIServer((self.host, self.port), self.handler).serve_forever()

    def handler(self, env, start_response):
        if env['PATH_INFO'] == '/session/login':
            data = json.loads(env['wsgi.input'].read())
            response = self.command_login(data=data)
        if env['PATH_INFO'] == '/login':
            ...
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello']

    def command_login(self, data):
        url = f'{self.base_url}/session/login'
        method = self.methods_mapper.get('login')
        response = {}
        status_code = 500
        request_id = uuid1()
        log_request = self.hide_sensitive_fields(dict(data))
        logger.info(f'LOGIN REQUEST {request_id} request: {log_request}, method: {method}')

        try:
            response = getattr(requests, method)(url=url, json=data, verify=False)
            status_code = response.status_code
        except Exception as e:
            log_response = self.hide_sensitive_fields(dict(response))
            logger.critical(f'LOGIN Unhandled exception {request_id} reason: {e}\t request: {data}, method: {data}, '
                            f'response: {log_response}')
        else:
            log_response = self.hide_sensitive_fields(dict(response))
            logger.info(f'LOGIN RESPONSE {request_id} response: {log_response}')
        finally:
            return response, status_code

    def command_get(self):
        ...

    @staticmethod
    def hide_sensitive_fields(data):
        for field in sensitive_fields:
            if field in data:
                data[field] = '*****'
        return data
