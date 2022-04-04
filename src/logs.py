import os
import logging

def setup_logger(loglevel: str = None) -> logging.Logger:
    """
    Initialize log settings using the base class

    See: https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html
    """
    # Define formatter
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s')

    # Define handler
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    # Create logger instance
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)

    # If loglevel not set, try to get it from env, otherwise set to INFO
    if loglevel is None:
        loglevel = os.environ.get("LOG_LEVEL", "INFO")

    if loglevel == "DEBUG":
        logger.setLevel(logging.DEBUG)
    elif loglevel == "INFO":
        logger.setLevel(logging.INFO)
    elif loglevel == "WARNING":
        logger.setLevel(logging.WARNING)
    elif loglevel == "ERROR":
        logger.setLevel(logging.ERROR)
    elif loglevel == "CRITICAL":
        logger.setLevel(logging.CRITICAL)
    else:
        logger.setLevel(logging.INFO)

    return logger