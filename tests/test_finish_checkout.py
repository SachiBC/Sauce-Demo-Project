import time
import pytest
from selenium import webdriver

from config import config
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.finish_checkout_page import FinishCheckoutPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    driver.get(config.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_finish_checkout(setup):
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

    # Fill form
    checkout.enter_first_name("Ann")
    checkout.enter_last_name("Fernando")
    checkout.enter_postal_code("12345")
    checkout.click_continue()

    finish_checkout.click_finish()
    assert "checkout-complete.html" in setup.current_url


def test_cancel_finish_checkout(setup):
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

    # Fill form
    checkout.enter_first_name("Ann")
    checkout.enter_last_name("Fernando")
    checkout.enter_postal_code("12345")
    checkout.click_continue()

    finish_checkout.click_cancel()
    assert "inventory.html" in setup.current_url