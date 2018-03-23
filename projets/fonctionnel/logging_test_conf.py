import logging.config
import os

file = os.path.abspath(__file__)
print("file : ", file)
repertoire = os.path.dirname(file)
print("dir : ", repertoire)
projet = os.path.dirname(repertoire)
print("dir : ", projet)





logging.config.fileConfig("{}/conf/logging.conf".format(projet))


# create logger
logger = logging.getLogger("logger1")
# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")