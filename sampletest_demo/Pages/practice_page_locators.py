from selenium.webdriver.common.by import By

class PracticePageLocators:
    RADIO_BUTTON = (By.CSS_SELECTOR, 'input#bmwradio')
    CHECKBOX_ONE = (By.CSS_SELECTOR, 'input#bmwcheck')
    DROPDOWN = (By.CSS_SELECTOR, 'select#carselect')
    TEXT_BOX = (By.CSS_SELECTOR, 'input#name')
    SWITCH_TAB = (By.CSS_SELECTOR, 'button#opentab')
    SWITCH_WINDOW = (By.CSS_SELECTOR, 'button#openwindow')
    RELATIVE_XPATH_ONE = (By.XPATH, '//legend[contains(text(),"Radio Button Example")]')
