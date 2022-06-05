import logging as log # https://docs.python.org/3/howto/logging.html

# Logging levels
# logging.debug()    #lvl 5
# logging.info()     #lvl 4
# logging.warning()  #lvl 3
# logging.error()    #lvl 2
# logging.critical() #lvl 1

log.basicConfig(level=log.DEBUG, filename="main.log", filemode='w')

log.debug("Hello log")
log.info("Hello log")
log.warning("Hello log")
log.error("Hello log")
log.critical("Hello log")