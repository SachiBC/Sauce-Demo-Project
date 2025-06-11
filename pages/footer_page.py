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

    def click_hamburger_icon(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FooterPageLocators.HAMBURGER_ICON)
        ).click()

    def click_sidebar_1(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FooterPageLocators.SIDEBAR_1)
        ).click()

    def click_sidebar_2(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FooterPageLocators.SIDEBAR_2)
        ).click()

    def click_sidebar_3(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FooterPageLocators.SIDEBAR_3)
        ).click()

    def click_sidebar_4(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FooterPageLocators.SIDEBAR_4)
        ).click()

    def close_sidebar(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FooterPageLocators.SIDEBAR_CLOSE)
        ).click()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")      # Scrolls from the top (0) to the full height of the page, which is the bottom

    def switch_to_first_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[0])

    def go_back(self):
        self.driver.back()

