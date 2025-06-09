import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locator import LoginPageLocators, FooterPageLocators


class FooterPage:
    def __init__(self, driver):         #Connects the browser to this class   #constructor — it runs automatically when we create an object of this class
        self.driver = driver            #stores the browser inside the class so we can use it later

    def click_twitter_icon(self):     #a function
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(       #Wait up to 10 seconds
            EC.visibility_of_element_located(FooterPageLocators.TWITTER_ICON)
        ).click()

    def click_facebook_icon(self):     #a function
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(       #Wait up to 10 seconds
            EC.visibility_of_element_located(FooterPageLocators.FACEBOOK_ICON)
        ).click()

    def click_linkedin_icon(self):     #a function
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(       #Wait up to 10 seconds
            EC.visibility_of_element_located(FooterPageLocators.LINKEDIN_ICON)
        ).click()
