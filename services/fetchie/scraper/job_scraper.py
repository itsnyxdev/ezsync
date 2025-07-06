import datetime

from bson import ObjectId, Timestamp
from loguru import logger
from selenium.webdriver.common.by import By
from slugify import slugify

from config import ENDPOINT_JOBS, ENDPOINT_JOBS_SEARCH
from core.db_connection import DBConnection
from scraper.browser_manager import BrowserManager


class JobScraper:

    def __init__(self):
        self.browser_manager = BrowserManager()
        self.driver = self.browser_manager.get_driver()

        logger.info("Job scraper initialized.")

    def start(self):
        driver = self.driver
        crawled_categories = []

        db = DBConnection().get_db()
        categories = db['categories'].find()

        driver.get(ENDPOINT_JOBS)
        logger.info("Jobs page is loading.")
        driver.implicitly_wait(10)
        logger.info("Jobs page was successfully loaded.")

        for category in categories:
            _id = category['_id']
            name = category['name']
            self.collect(_id, name, driver)

    def collect(self, _id, name, driver):
        logger.info(f"Start scraping for category: {_id}:'{name}'")
        jobs_level = {
            'entry': [1, 2, 3],
            'mid': [4],
            'senior': [5, 6]
        }

        for level, levels in jobs_level.items():
            str_levels = None
            if len(level) > 1:
                str_levels = ','.join([str(i) for i in levels])
            else:
                str_levels = str(levels[0])

            logger.info(f"Scraping jobs for level: {level} with levels: {str_levels}")

            params = {
                "f_E": str_levels,
                "f_TPR": "r86400",
                "geoId": "103644278",
                "keywords": name
            }
            endpoint = BrowserManager.create_url(ENDPOINT_JOBS_SEARCH, params)
            logger.info(f"Fetching jobs from endpoint: {endpoint}")

            driver.implicitly_wait(5)
            driver.get(endpoint)
            self.scroll(driver)

            jobs_titles = driver.find_elements(By.CSS_SELECTOR,
                                               '.artdeco-entity-lockup__title span[aria-hidden="true"]')
            jobs_locations = driver.find_elements(By.CLASS_NAME, "artdeco-entity-lockup__caption")
            jobs_links = driver.find_elements(By.CLASS_NAME, "job-card-container__link")
            jobs_companies = driver.find_elements(By.CLASS_NAME, "artdeco-entity-lockup__subtitle")
            jobs_details = zip(jobs_titles, jobs_locations, jobs_links, jobs_companies)

            self.save_jobs(level, _id, jobs_details)

    def save_jobs(self, level, category_id, jobs_details):
        db = DBConnection().get_db()
        jobs_collection = db['jobs']

        for title, location, link, company in jobs_details:
            job = jobs_collection.find({"link": link.get_attribute("href")}, {"levelType": 1, "jobId": 1}).limit(1)

            if len(list(job)) > 0:
                logger.info(f"Job already exists: {title.text} - {link.get_attribute('href')}")

                if level not in job[0]['levelType']:
                    jobs_collection.update_one(
                        {"jobId": job[0]['jobId']},
                        {"$push": {"levelType": level}}
                    )
            else:
                logger.info(f"Saving new job: {title.text} - {link.get_attribute('href')}")

                job_data = {
                    "slug": slugify(title.text),
                    "title": title.text,
                    "company": company.text,
                    "location": {
                        "city": location.text,
                        "country": "United States"
                    },
                    "categoryId": category_id,
                    "levelType": [level],
                    "jobId": ObjectId(),
                    "modifiedAt": datetime.datetime.now(datetime.timezone.utc)
                }

                jobs_collection.update_one(
                    {
                        "link": link.get_attribute("href"),
                        "slug": job_data['slug']
                    },
                    {"$setOnInsert": job_data},
                    upsert=True
                )

                logger.info(f"Job saved: {title.text} - {link.get_attribute('href')}")

    def scroll(self, driver):
        logger.info("Scrolling down the page to load more jobs.")

        window = driver.find_element(By.CSS_SELECTOR,
                                     "#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__list > div")
        for _ in range(25):
            driver.execute_script("arguments[0].scrollBy(0, arguments[0].scrollHeight);", window)
            self.browser_manager.random_wait(0.2, 0.7)

        logger.info("Scrolling completed.")
