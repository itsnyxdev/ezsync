from loguru import logger
from core.db_connection import DBConnection
from scraper.scraper import Scraper

logger.add("../../shared/logs/services/fetchie/info.log", retention="7 Days", level="INFO")
logger.add("../../shared/logs/services/fetchie/error.log", retention="7 Days", level="ERROR")
logger.add("../../shared/logs/services/fetchie/debug.log", retention="7 Days", level="DEBUG")


db = DBConnection().get_db()
scraper = Scraper()
scraper.start()
scraper.end()