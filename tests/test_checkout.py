import time
import pytest
from selenium import webdriver

from config import config
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    driver.get(config.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_checkout(setup):
    login = LoginPage(setup)
    inventory = InventoryPage(setup)
    cart = CartPage(setup)
    checkout = CheckoutPage(setup)

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
    checkout.enter_first_name("Ann")
    checkout.enter_last_name("Fernando")
    checkout.enter_postal_code("12345")
    checkout.click_continue()

    # assertion
    assert "checkout-step-two" in setup.current_url

def test_empty_firstname_lastname_postalcode_checkout(setup):
    login = LoginPage(setup)
    inventory = InventoryPage(setup)
    cart = CartPage(setup)
    checkout = CheckoutPage(setup)

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
    checkout.enter_first_name("")
    checkout.enter_last_name("")
    checkout.enter_postal_code("")
    checkout.click_continue()

    # assertion
    error_message = login.get_error_message()
    assert "First Name is required" in error_message

def test_empty_lastname_postalcode_checkout_(setup):
    login = LoginPage(setup)
    inventory = InventoryPage(setup)
    cart = CartPage(setup)
    checkout = CheckoutPage(setup)

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
    checkout.enter_first_name("Ann")
    checkout.enter_last_name("")
    checkout.enter_postal_code("")
    checkout.click_continue()

    # assertion
    error_message = login.get_error_message()
    assert "Last Name is required" in error_message

def test_empty_firstname_postalcode_checkout_(setup):
    login = LoginPage(setup)
    inventory = InventoryPage(setup)
    cart = CartPage(setup)
    checkout = CheckoutPage(setup)

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
    checkout.enter_first_name("")
    checkout.enter_last_name("Fernando")
    checkout.enter_postal_code("")
    checkout.click_continue()

    # assertion
    error_message = login.get_error_message()
    assert "First Name is required" in error_message

def test_empty_firstname_lastname_checkout_(setup):
    login = LoginPage(setup)
    inventory = InventoryPage(setup)
    cart = CartPage(setup)
    checkout = CheckoutPage(setup)

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
    checkout.enter_first_name("")
    checkout.enter_last_name("")
    checkout.enter_postal_code("12345")
    checkout.click_continue()

    # assertion
    error_message = login.get_error_message()
    assert "First Name is required" in error_message

def test_empty_firstname_checkout_(setup):
    login = LoginPage(setup)
    inventory = InventoryPage(setup)
    cart = CartPage(setup)
    checkout = CheckoutPage(setup)

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
    checkout.enter_first_name("")
    checkout.enter_last_name("Fernando")
    checkout.enter_postal_code("12345")
    checkout.click_continue()

    # assertion
    error_message = login.get_error_message()
    assert "First Name is required" in error_message

def test_empty_lastname_checkout(setup):
    login = LoginPage(setup)
    inventory = InventoryPage(setup)
    cart = CartPage(setup)
    checkout = CheckoutPage(setup)

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
    checkout.enter_first_name("Ann")
    checkout.enter_last_name("")
    checkout.enter_postal_code("12345")
    checkout.click_continue()

    # assertion
    error_message = login.get_error_message()
    assert "Last Name is required" in error_message

def test_empty_postalcode_checkout(setup):
    login = LoginPage(setup)
    inventory = InventoryPage(setup)
    cart = CartPage(setup)
    checkout = CheckoutPage(setup)

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
    checkout.enter_first_name("Ann")
    checkout.enter_last_name("Fernando")
    checkout.enter_postal_code("")
    checkout.click_continue()

    # assertion
    error_message = login.get_error_message()
    assert "Postal Code is required" in error_message

def test_cancel_checkout(setup):
    login = LoginPage(setup)
    inventory = InventoryPage(setup)
    cart = CartPage(setup)
    checkout = CheckoutPage(setup)

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

    # Cancel checkout
    checkout.click_cancel()

    # Assert redirected back to cart
    assert "cart" in setup.current_url