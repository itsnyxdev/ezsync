import config
from loguru import logger

from scraper.browser_manager import BrowserManager
from selenium.webdriver.common.by import By


class AccountManager:

    def __init__(self):
        self.driver = None
        self.browser_manager = None
        self.email = config.ACCOUNT_EMAIL
        self.password = config.ACCOUNT_PASSWORD

        logger.info("AccountManager initialized with email: {}", self.email)

    def set_browser_manager(self, browser_manager: BrowserManager):
        self.browser_manager = browser_manager
        self.driver = browser_manager.get_driver()
        logger.info("BrowserManager set for AccountManager.")

    def is_logged_in(self):
        if not self.browser_manager:
            logger.error("BrowserManager is not set in AccountManager.")
            return False

        current = self.driver.current_url

        if "login" in current:
            return False

        try:
            self.driver.find_element(By.CSS_SELECTOR, "img.global-nav__me-photo")
            logger.info("User is logged in.")
            return True
        except Exception as e:
            logger.error("User is not logged in: {}", e)
            return False

    def login(self):
        if not self.browser_manager:
            logger.error("BrowserManager is not set in AccountManager.")
            return False

        self.driver.get("https://www.linkedin.com/login")

        email_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

        email_input.send_keys(self.email)
        password_input.send_keys(self.password)
        login_button.click()

        BrowserManager.random_wait()

        if self.is_logged_in():
            logger.info("Login successful.")
            return True
        else:
            logger.error("Login failed.")
            return False
