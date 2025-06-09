import pytest
from selenium import webdriver

from config import config
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.finish_checkout_page import FinishCheckoutPage

@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    driver.get(config.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_complete(setup):
    login = LoginPage(setup)
    inventory = InventoryPage(setup)
    cart = CartPage(setup)
    checkout = CheckoutPage(setup)
    finish_checkout = FinishCheckoutPage(setup)

    # Login
    login.enter_username(config.USERNAME)
    login.enter_password(config.PASSWORD)
    login.click_login()

    # Add item to cart
    inventory.add_to_cart()

    # Go to cart
    inventory.go_to_cart()

    # Proceed to checkout
    cart.click_checkout()

    # Fill checkout form
    checkout.enter_first_name("John")
    checkout.enter_last_name("Doe")
    checkout.enter_postal_code("12345")
    checkout.click_continue()

    finish_checkout.click_finish()