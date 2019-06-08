import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-a-secret-key'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')