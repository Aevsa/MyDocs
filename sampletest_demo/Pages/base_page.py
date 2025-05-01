from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from logger import setup_logger  # assuming you have a logger.py that sets up logging

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.logger = setup_logger(self.__class__.__name__)

    def click_element(self, locator):
        with allure.step(f'Clicking element: {locator}'):
            try:
                element = WebDriverWait(self.driver, self.timeout).until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()
                self.logger.info(f'Clicked on element: {locator}')
            except Exception as e:
                self.logger.error(f'Error clicking element {locator}: {e}')
                raise

    def enter_text(self, locator, text):
        with allure.step(f'Entering text into element: {locator}'):
            try:
                element = WebDriverWait(self.driver, self.timeout).until(
                    EC.visibility_of_element_located(locator)
                )
                element.clear()
                element.send_keys(text)
                self.logger.info(f'Entered text "{text}" into element: {locator}')
            except Exception as e:
                self.logger.error(f'Error entering text into element {locator}: {e}')
                raise

    def get_text(self, locator):
        with allure.step(f'Getting text from element: {locator}'):
            try:
                element = WebDriverWait(self.driver, self.timeout).until(
                    EC.visibility_of_element_located(locator)
                )
                text = element.text
                self.logger.info(f'Fetched text from element {locator}: "{text}"')
                return text
            except Exception as e:
                self.logger.error(f'Error getting text from element {locator}: {e}')
                raise

