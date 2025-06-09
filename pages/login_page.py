
#This file contains all actions related to the login page like typing username, password, and clicking login
#__init__ connects the Selenium driver (initialized)
#Each method does one action: type username, password, or click
#WebDriverWait waits until the element is visible or clickable (no sleep()!)

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locator import LoginPageLocators

class LoginPage:
    def __init__(self, driver):         #Connects the browser to this class   #constructor — it runs automatically when we create an object of this class
        self.driver = driver            #stores the browser inside the class so we can use it later

    def enter_username(self, username):     #a function that types the username in the username box
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(       #Wait up to 10 seconds
            EC.visibility_of_element_located(LoginPageLocators.USERNAME_INPUT)         #Wait until the username box appears
        ).send_keys(username)               #Type the username

    def enter_password(self, password):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        ).send_keys(password)

    def click_login(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(           #waits until the button is clickable
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()           #clicks it

    def get_error_message(self):            #This function tries to find the error message after a login attempt
        try:            #Try to do this...
            return self.driver.find_element(*LoginPageLocators.ERROR_MESSAGE).text      #Find the error message using a locator from locator.py     #.text - Get/reads the text of the error message
        except:         #If not found (e.g., no error message shown), don’t crash
            return None     #Just return nothing (so the test can still handle it)
