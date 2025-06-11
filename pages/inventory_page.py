
#Handles actions on the inventory (products) page

import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locator import InventoryPageLocators


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(InventoryPageLocators.ADD_CART)
        ).click()

    def is_remove_button_displayed(self):
        time.sleep(2)
        try:    #trying to check if the Remove button is visible on the screen
            return WebDriverWait(self.driver, 10).until(    #Waits up to 10 seconds until the Remove button becomes visible
                EC.visibility_of_element_located(InventoryPageLocators.REMOVE_CART)
            ).is_displayed()        #If the button is visible, return True
        except:
            return False

    def remove_from_cart(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(InventoryPageLocators.REMOVE_CART)
        ).click()

    def go_to_cart(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(InventoryPageLocators.CART_ICON)
        ).click()

    def is_add_to_cart_button_displayed(self):
        time.sleep(2)
        try:    #trying to check if the add to cart button is visible on the screen
            return WebDriverWait(self.driver, 10).until(    #Waits up to 10 seconds until the Remove button becomes visible
                EC.visibility_of_element_located(InventoryPageLocators.ADD_CART)
            ).is_displayed()        #If the button is visible, return True
        except:
            return False
