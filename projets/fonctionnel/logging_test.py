
import logging,logging.handlers
# create logger
logger = logging.getLogger("log_sample")
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#un autre handler : rotting : Add the log message handler to the logger
rh = logging.handlers.RotatingFileHandler("biblio.log", maxBytes=200, backupCount=5)
# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
rh.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
logger.addHandler(rh)



# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")