from selenium import webdriver # Imports Selenium WebDriver Module
from selenium.webdriver.common.by import By # Allows locating of elements
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service # Wraps the driver startup behavior, Logging, Executable, ports 4.0+
from selenium.webdriver.common.devtools.v133.dom_storage import clear
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import Select, WebDriverWait # Allows you to interact with dropdowns and wait for elements to load.
from selenium.webdriver.support import expected_conditions as EC # Provides predefined condition
from webdriver_manager.chrome import ChromeDriverManager # Correct version of chrome driver
import time

# This is good! So I yoinked it!

current_time = time.time()
readable_time = time.ctime(current_time)
print(readable_time)  # Example: 'Mon Apr 22 10:03:02 2025'
# this too.


# Step 1: Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.southwest.com/")

# Step 2: Waiting for cookie alert
WebDriverWait(driver, 10).until(
    visibility_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
).click()

# Step 3: Attempting to select the flight button oh god
"""
WebDriverWait(driver, 10).until(
    visibility_of_element_located((By.XPATH, 'By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/span/span/div/div/div[1]/button[1]/span/span/span[2]'))
).click()
#let's pretend this didn't hppen for now. It selected by dafault, and therefore, my nemesis.
#Thinking maybe what is appropriate here is a check to see if it is selected, and if not, select it
"""

# Step 4: Attempting to select departing airport, and select pittsburgh
WebDriverWait(driver, timeout=5).until(
    visibility_of_element_located((By.CSS_SELECTOR, "#LandingAirBookingSearchForm_originationAirportCode"))
).send_keys(Keys.CONTROL + "a", Keys.DELETE)



driver.find_element(By.CSS_SELECTOR, "#LandingAirBookingSearchForm_originationAirportCode").send_keys("PIT", Keys.ENTER)
#This is not elegant and will make mac users sad. I could not get clear to work.

# Step 5: Attempting to select arriving airport, and select orlando
driver.find_element(By.CSS_SELECTOR, "#LandingAirBookingSearchForm_destinationAirportCode").send_keys("MCO", Keys.ENTER)
#I am making people sad all over the place

# Step 6: Poorly attempting a departure date.
driver.find_element(By.CSS_SELECTOR, "#LandingAirBookingSearchForm_departureDate").clear()
driver.find_element(By.CSS_SELECTOR, "#LandingAirBookingSearchForm_departureDate").send_keys("5/03")

# Step 7: Poorly attempting a return date.
driver.find_element(By.CSS_SELECTOR, "#LandingAirBookingSearchForm_returnDate").clear()
driver.find_element(By.CSS_SELECTOR, "#LandingAirBookingSearchForm_returnDate").send_keys("6/25")


"""
WebDriverWait(driver, timeout=10).until(
    visibility_of_element_located((By.XPATH, '//*[@id="calendar-326-2025-05-06"]'))
).click()

WebDriverWait(driver, timeout=10).until(
    visibility_of_element_located((By.XPATH, '//*[@id="calendar-329-2025-06-10"]'))
).click()
#I learned that I hate calendars.
"""

#Step 8: I'm stumped! Let's leave it at 1.

#Step 9: This radio button is selected for me by default
# This is what I got for a CSS selector self.fares = (By.CSS_SELECTOR, ".input-group_right-aligned > ul:nth-child(2) > li:nth-child(1) > label:nth-child(1) > input:nth-child(1)")
# but I suspect by ID would be a prettier option
# However I think, like the tab, figuring out how to check if it's already selected would be a good idea.


#Step 10: Let's hit the search button and pray.
driver.find_element(By.CSS_SELECTOR, "#LandingAirBookingSearchForm_submit-button").click()

#Assesment: Potato/5
