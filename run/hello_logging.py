import logging.config

from my_project_module.conf.logging_conf import LOGGING_CONF

if __name__ in ('__main__', 'builtins'):
    logging.config.dictConfig(LOGGING_CONF)
    logger = logging.getLogger("MyLogger")
    logging.info("Hello World")
    filelogger = logging.getLogger("myCustomLogger")
    filelogger.warning("This is written to file")
