
#write the actual test using pytest
#setup() is a pytest fixture to open the browser before the test and close it after
#test_valid_login() performs login and checks if URL has "inventory" (successful login page)

import time                             # Import time module
import pytest
from selenium import webdriver
from config import config
from pages.login_page import LoginPage

@pytest.fixture                         #fixture is a special function in pytest that runs before your test starts
def setup():
    driver = webdriver.Chrome()         #starts the browser
    driver.get(config.BASE_URL)
    driver.maximize_window()            #Maximize browser window
    yield driver                        #Give the browser to the test so it can use it
    driver.quit()                       #Close the browser after the test

#Valid Username and Password
def test_valid_login(setup):            #def - Python keyword used to define a function  #test_valid_login- name of your test function and it must start with test_ so that pytest knows it’s a test case and will automatically run it
    login = LoginPage(setup)            #creating an object of the LoginPage class which created inside login_page.py
    time.sleep(2)                               # Wait before typing username
    login.enter_username(config.USERNAME)       # correct username
    time.sleep(2)                               # Wait before typing password
    login.enter_password(config.PASSWORD)       # correct password
    time.sleep(2)                               # Wait before clicking login
    login.click_login()
    time.sleep(2)                               # Wait to observe result
    assert "inventory" in setup.current_url     #checking if the word "inventory" is part of the current page URL after login
                                                #assert	- Check that a condition is true
#Invalid Username and Password
def test_invalid_login(setup):
    login = LoginPage(setup)
    time.sleep(2)
    login.enter_username("invalid_user")  # wrong username
    time.sleep(2)
    login.enter_password("wrong_password")      # wrong password
    time.sleep(2)
    login.click_login()
    time.sleep(2)
    error_message = login.get_error_message()
    assert "epic sadface" in error_message.lower()      #checking if the error message (after a failed login) contains the text
                                                        #.lower() - error message converted to lowercase
#Empty username and password
def test_login_empty_username_password(setup):
    login = LoginPage(setup)
    time.sleep(2)
    login.enter_username("")   # leave empty
    time.sleep(2)
    login.enter_password("")   # leave empty
    time.sleep(2)
    login.click_login()
    time.sleep(2)
    error_message = login.get_error_message()
    assert "epic sadface" in error_message.lower()

#Only username filled
def test_login_only_username(setup):
    login = LoginPage(setup)
    time.sleep(2)
    login.enter_username(config.USERNAME)  # valid username
    time.sleep(2)
    login.enter_password("")  # empty password
    time.sleep(2)
    login.click_login()
    time.sleep(2)
    error_message = login.get_error_message()
    assert "epic sadface" in error_message.lower()

#Only password filled
def test_login_only_password(setup):
    login = LoginPage(setup)
    time.sleep(2)
    login.enter_username("")                # empty username
    time.sleep(2)
    login.enter_password(config.PASSWORD)    # valid password
    time.sleep(2)
    login.click_login()
    time.sleep(2)
    error_message = login.get_error_message()
    assert "epic sadface" in error_message.lower()

#Locked out user
def test_login_locked_out_user(setup):
    login = LoginPage(setup)
    time.sleep(2)
    login.enter_username("locked_out_user")
    time.sleep(2)
    login.enter_password(config.PASSWORD)
    time.sleep(2)
    login.click_login()
    time.sleep(2)
    assert "locked out" in login.get_error_message().lower()

# Problem user
def test_login_problem_user(setup):
    login = LoginPage(setup)
    time.sleep(2)
    login.enter_username("problem_user")
    time.sleep(2)
    login.enter_password(config.PASSWORD)
    time.sleep(2)
    login.click_login()
    time.sleep(2)
    assert "inventory" in setup.current_url

# Performance glitch user
def test_login_performance_glitch_user(setup):
    login = LoginPage(setup)
    time.sleep(2)
    login.enter_username("performance_glitch_user")
    time.sleep(2)
    login.enter_password(config.PASSWORD)
    time.sleep(2)
    login.click_login()
    time.sleep(2)
    assert "inventory" in setup.current_url

# Error user
def test_login_error_user(setup):
    login = LoginPage(setup)
    time.sleep(2)
    login.enter_username("error_user")
    time.sleep(2)
    login.enter_password(config.PASSWORD)
    time.sleep(2)
    login.click_login()
    time.sleep(2)
    assert "inventory" in setup.current_url

# Visual user
def test_login_visual_user(setup):
    login = LoginPage(setup)
    time.sleep(2)
    login.enter_username("visual_user")
    time.sleep(2)
    login.enter_password(config.PASSWORD)
    time.sleep(2)
    login.click_login()
    time.sleep(2)
    assert "inventory" in setup.current_url

