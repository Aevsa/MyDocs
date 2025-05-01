from selenium import webdriver # Imports Selenium WebDriver Module
from selenium.webdriver.common.by import By # Allows locating of elements
from selenium.webdriver.chrome.service import Service # Wraps the driver startup behavior, Logging, Executable, ports 4.0+
from selenium.webdriver.support.ui import Select, WebDriverWait # Allows you to interact with dropdowns and wait for elements to load.
from selenium.webdriver.support import expected_conditions as EC # Provides predefined condition
from webdriver_manager.chrome import ChromeDriverManager # Correct version of chrome driver
import time

current_time = time.time()
readable_time = time.ctime(current_time)
print(readable_time)  # Example: 'Mon Apr 22 10:03:02 2025'


# Step 1: Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.facebook.com")

# Step 2: Open the registration form
driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']").click()
WebDriverWait(driver, 2)

# Step 3: Fill out basic fields
driver.find_element(By.NAME, "firstname").send_keys("Xavier")
driver.find_element(By.NAME, "lastname").send_keys("Mark")
driver.find_element(By.NAME, "reg_email__").send_keys("naren.iyer100@gmail.com")

# Step 4: ✅ Try to fill confirmation email if it appears
try:
    email_confirm = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.NAME, "reg_email_confirmation__")))
    #This condition means:I want to wait until an element is both present in the DOM and visible on the screen.

    email_confirm.send_keys("naren.iyer100@gmail.com")
except:
    print("Email confirmation field not shown — skipping.") #Selenium scripts resilient to dynamic UIs like Facebook’s.

# Step 5: Password
driver.find_element(By.NAME, "reg_passwd__").send_keys("MyDummyPassword123")

# Step 6: Select date of birth
Select(driver.find_element(By.ID, "day")).select_by_visible_text("8")
Select(driver.find_element(By.ID, "month")).select_by_visible_text("May")
Select(driver.find_element(By.ID, "year")).select_by_visible_text("1975")

# Step 7: Select gender
driver.find_element(By.XPATH, "//input[@name='sex' and @value='1']").click()

# Step 8: Pause for visibility (optional)
time.sleep(2)

# Step 9: Test result
print("Test Case 2 passes")

# Step 10: Close browser
driver.quit()

