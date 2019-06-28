import logging
from logging.handlers import RotatingFileHandler

LOG_SIZE_BYTES = 50000000
LOG_BACKUPS = 5

formatter = logging.Formatter('%(asctime)s|%(name)s|%(filename)s|%(lineno)s|%(levelname)s -  %(message)s')

some_log = logging.getLogger('general')
general_handler = RotatingFileHandler(<path to log>, maxBytes=LOG_SIZE_BYTES, backupCount=LOG_BACKUPS)
general_handler.setFormatter(formatter)
general_log.setLevel(logging.DEBUG)
general_log.addHandler(general_handler)
