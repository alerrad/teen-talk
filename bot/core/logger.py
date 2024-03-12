import logging as lg
import sys


formatter = lg.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

# Console stream handler
stream_handler = lg.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

# Log file handler
handler = lg.FileHandler('bot.log')
handler.setFormatter(formatter)

logger = lg.getLogger(__name__)
logger.setLevel(lg.INFO)
logger.addHandler(handler)
logger.addHandler(stream_handler)
