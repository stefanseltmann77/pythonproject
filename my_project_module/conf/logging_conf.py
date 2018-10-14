import logging
import os

LOGGING_PATH = './'
LOGGING_FORMAT = '%(asctime)s | %(levelname)-7s | %(name)-28s | %(funcName)-20s |%(message)s'

LOGGING_CONF = dict(version=1,
                    root={
                        'handlers': ['consoleHandler'],
                        'level': logging.DEBUG
                    },
                    handlers={
                        'consoleHandler': {'class': 'logging.StreamHandler',
                                           'formatter': 'default',
                                           'level': logging.DEBUG
                                           },
                        'customFileHandle': {'class': 'logging.FileHandler',
                                             'formatter': 'default',
                                             'filename': os.path.sep.join([LOGGING_PATH, 'logfile.log']),
                                             'level': logging.DEBUG
                                             },
                    },
                    formatters={
                        'default': {'format': LOGGING_FORMAT}
                    },
                    loggers={
                        'myCustomLogger': {
                            'handlers': ['customFileHandle'],
                            'level': 'INFO',
                            'qualname': 'myCustomLogger'
                        }
                    }
                    )
