
#New test file to test add/remove functionality

import time
import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from config import config
from pages.login_page import LoginPage


@pytest.fixture
def setup():
    driver = webdriver.Firefox()         #starts the browser
    driver.get(config.BASE_URL)
    driver.maximize_window()            #Maximize browser window
    yield driver                        #Give the browser to the test so it can use it
    driver.quit()

def test_add_and_remove_item(setup):

    login = LoginPage(setup)
    time.sleep(2)
    login.enter_username(config.USERNAME)
    time.sleep(2)
    login.enter_password(config.PASSWORD)
    time.sleep(2)
    login.click_login()

    inventory = InventoryPage(setup)        #Create an object called inventory using the InventoryPage class and pass the browser (setup) into it
    time.sleep(2)

    inventory.add_to_cart()                 #that knows how to click the “Add to cart” button using Selenium
    assert inventory.is_remove_button_displayed()       #assert-Check if this is True  #This method checks if the “Remove” button is displayed on the page
    time.sleep(2)

    inventory.remove_from_cart()  # removing it
    time.sleep(2)
    assert inventory.is_add_to_cart_button_displayed()  # check that Add to cart button is back
    time.sleep(2)

    # Add again, and now go to Cart instead of removing
    inventory.add_to_cart()
    time.sleep(2)
    inventory.go_to_cart()
    time.sleep(2)

