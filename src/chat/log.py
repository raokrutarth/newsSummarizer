import logging
import logging.handlers as handlers
import time
import sys

LOGGER = None

DEBUG_LOG_FILENAME = '/var/log/chat.log'


def get_logger():
    global LOGGER
    if not LOGGER:
        logger = logging.getLogger('chat')
        logger.setLevel(logging.INFO)
        # Here we define our formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        logHandler = handlers.TimedRotatingFileHandler(DEBUG_LOG_FILENAME, when='M', interval=0, backupCount=0)
        logHandler.setLevel(logging.INFO)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)


        # Here we set our logHandler's formatter
        logHandler.setFormatter(formatter)
        logger.addHandler(logHandler)
        logger.addHandler(handler)
        LOGGER = logger
    return LOGGER

def log_info(message):
    get_logger().info(message)
    # get_logger_3().info(message)
    # get_logger_3().debug(message)
    # sys.stdout.write(message)

def log_debug(message):
    get_logger().debug(message)
    # get_logger_3().debug(message)
    # get_logger_3().debug(message)
    # sys.stdout.write(message)

def get_logger_2():
    global LOGGER
    if not LOGGER:
        # set up formatting
        formatter = logging.Formatter('[%(asctime)s] %(levelno)s (%(process)d) %(module)s: %(message)s')

        # set up logging to STDOUT for all levels DEBUG and higher
        sh = logging.StreamHandler(sys.stdout)
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(formatter)

        # set up logging to a file for all levels DEBUG and higher
        fh = logging.FileHandler(DEBUG_LOG_FILENAME)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        # create Logger object
        mylogger = logging.getLogger('chat')
        mylogger.setLevel(logging.DEBUG)
        mylogger.addHandler(sh)
        mylogger.addHandler(fh)

        LOGGER = mylogger
    return LOGGER

def get_logger_3():
    global LOGGER
    if not LOGGER:
        logger = logging.getLogger('chat')
        logger.setLevel(logging.DEBUG)

        # create file handler which logs even debug messages
        fh = logging.FileHandler(path)
        fh.setLevel(logging.DEBUG)


        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(fh)

        LOGGER = logger
    return LOGGER

