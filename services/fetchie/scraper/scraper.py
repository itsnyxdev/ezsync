from scraper.account_manager import AccountManager
from scraper.browser_manager import BrowserManager
from loguru import logger
import config
from scraper.job_scraper import JobScraper


class Scraper:

    def __init__(self):
        self.browser_manager = BrowserManager()
        self.browser_manager.init_driver()
        self.driver = self.browser_manager.get_driver()

        logger.info("Scraper initialized and WebDriver started.")

    def start(self):
        driver = self.driver
        browser_manager = self.browser_manager
        account_manager = AccountManager()
        account_manager.set_browser_manager(self.browser_manager)

        driver.get(config.ENDPOINT_FEED)
        BrowserManager.random_wait(3,6)

        if not account_manager.is_logged_in():
            account_manager.login()

        job_scraper = JobScraper()
        job_scraper.start()

    def end(self):
        if self.browser_manager and self.browser_manager.quit_driver():
            self.driver = None
            self.browser_manager = None
            logger.info("Scraper ended and WebDriver quit successfully.")
        else:
            logger.error("Failed to quit WebDriver during Scraper end.")