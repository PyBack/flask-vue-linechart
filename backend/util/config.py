import logging
import logging.handlers

formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s %(lineno)d: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

stream_log = logging.StreamHandler()
stream_log.setFormatter(formatter)
