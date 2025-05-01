import pytest
import os
from dotenv import load_dotenv
from sampletest_demo.browser_manager import WebDriverManager
from Pages.practice_page import PracticePage

load_dotenv()

@pytest.fixture(scope='class')
def setup(request):
    browser = os.getenv('BROWSER')
    base_url = os.getenv('BASE_URL')
    driver = WebDriverManager.get_driver(browser)
    driver.implicitly_wait(int(os.getenv('IMPLICIT_WAIT')))
    driver.maximize_window()
    driver.get(base_url)

    request.cls.driver = driver
    request.cls.practice_page = PracticePage(driver)
    yield
    WebDriverManager.quit_driver()
