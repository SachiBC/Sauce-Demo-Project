from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locator import CartPageLocators
from pages.inventory_page import InventoryPage


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def is_remove_button_displayed(self):
        time.sleep(2)
        try:  # trying to check if the Remove button is visible on the screen
            return WebDriverWait(self.driver, 10).until(
                # Waits up to 10 seconds until the Remove button becomes visible
                EC.visibility_of_element_located(CartPageLocators.REMOVE_CART)
            ).is_displayed()  # If the button is visible, return True
        except:
            return False

    def remove_from_cart(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartPageLocators.REMOVE_CART)
        ).click()

    def click_continue_shopping(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartPageLocators.CONTINUE_BUTTON)
        ).click()

    def click_checkout(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartPageLocators.CHECKOUT_BUTTON)
        ).click()

