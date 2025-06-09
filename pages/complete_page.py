from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locator import FinishCheckoutPageLocators, CompletePageLocators
import time

class CompletePage:
    def __init__(self, driver):
        self.driver = driver

    def click_back_home(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CompletePageLocators.BACK_HOME_BUTTON)
        ).click()