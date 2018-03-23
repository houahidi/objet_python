import logging.config





logging.config.fileConfig("logging.conf")
# create logger
logger = logging.getLogger("logger1")
# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")