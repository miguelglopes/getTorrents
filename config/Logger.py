"""
Logger Module.

This module defines logging setting to use.
"""
from Config.Config import Config

# TODO: os logs para  oficheiro nao tao a funcionar...
config = Config().config
logFile = config.get("Logs", "logsFile")
logLevel = config.get("Logs", "logLevel")

LOG_SETTINGS = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': "%(asctime)s: (%(filename)s->%(funcName)s #%(lineno)d): [%(levelname)s] - %(message)s"
            }
        },
        'handlers': {
            'file': {
                'level': logLevel,
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'formatter': 'default',
                'filename': logFile,
                'when': 'midnight',
                'interval': 1,
                'backupCount': 5
            }
        },
        'loggers': {
            'log1': {
                'handlers': ['file'],
                'level': logLevel,
                'propagate': True
            },
        }
    }
