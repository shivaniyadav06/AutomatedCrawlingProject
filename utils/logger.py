import logging
import config

def setup_logger():
    logger = logging.getLogger("TestLogger")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(config.LOG_FILE_PATH, mode='a')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

LOGGER = setup_logger()
