import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locator import CheckoutPageLocators


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):         # first_name: The text you want to input in the "First Name" field.
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(CheckoutPageLocators.FIRST_NAME)
        ).send_keys(first_name)

    def enter_last_name(self, last_name):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(CheckoutPageLocators.LAST_NAME)
        ).send_keys(last_name)      # Once the element is found and visible, it types the last_name value into the field.

    def enter_postal_code(self, postal_code):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(CheckoutPageLocators.POSTAL_CODE)
        ).send_keys(postal_code)

    def click_continue(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(  # waits until the button is clickable
            EC.element_to_be_clickable(CheckoutPageLocators.CONTINUE_BUTTON)
        ).click()

    def click_cancel(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(  # waits until the button is clickable
            EC.element_to_be_clickable(CheckoutPageLocators.CANCEL_BUTTON)
        ).click()
