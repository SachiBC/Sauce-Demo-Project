from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locator import FinishCheckoutPageLocators
import time

class FinishCheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_finish(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(FinishCheckoutPageLocators.FINISH_BUTTON)
        ).click()

    def click_cancel(self):
        time.sleep(2)
        WebDriverWait(self.driver,  10).until(
            EC.element_to_be_clickable(FinishCheckoutPageLocators.CANCEL_BUTTON)
        ).click()
