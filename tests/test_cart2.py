
import time
import pytest
from selenium import webdriver

from config import config
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def setup():
    driver = webdriver.Firefox()         #starts the browser
    driver.get(config.BASE_URL)
    driver.maximize_window()            #Maximize browser window
    yield driver                        #Give the browser to the test so it can use it
    driver.quit()

def test_cart_page_actions(setup):
    # Setup pages with the browser
    login = LoginPage(setup)
    inventory = InventoryPage(setup)
    cart = CartPage(setup)

    # Perform login
    login.enter_username(config.USERNAME)
    login.enter_password(config.PASSWORD)
    login.click_login()

    # Add item to cart
    inventory.add_to_cart()

    # Go to cart page
    inventory.go_to_cart()

    #Remove item from cart
    cart.remove_from_cart()

    # Click Continue Shopping
    cart.click_continue_shopping()

    inventory.add_to_cart()     # Add item again
    inventory.go_to_cart()      # Go back to cart
    cart.click_checkout()       # Click on checkout button