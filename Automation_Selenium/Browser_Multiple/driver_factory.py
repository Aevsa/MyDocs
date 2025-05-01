from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class DriverFactory:
    _driver = None # Singleton Design Pattern - Class Variable

    @classmethod
    def get_driver(cls, browser_name):
        if cls._driver is None:
            if browser_name == "chrome":
                cls._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            elif browser_name == "firefox":
                cls._driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            elif browser_name == "edge":
                cls._driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            else:
                raise Exception(f"Unsupported browser: {browser_name}")
            cls._driver.maximize_window()
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
