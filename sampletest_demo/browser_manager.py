from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Correct Service imports
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

class WebDriverManager:
    _driver = None

    @classmethod
    def get_driver(cls, browser_name='chrome'):
        if cls._driver is None:
            if browser_name.lower() == 'chrome':
                options = ChromeOptions()
                options.add_argument('--start-maximized')
                cls._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            elif browser_name.lower() == 'firefox':
                options = FirefoxOptions()
                options.add_argument('--width=1920')
                options.add_argument('--height=1080')
                cls._driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
            elif browser_name.lower() == 'edge':
                options = EdgeOptions()
                options.add_argument('--start-maximized')
                cls._driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
            else:
                raise Exception(f'Browser {browser_name} is not supported')
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
