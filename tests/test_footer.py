import time
import pytest
from selenium import webdriver
from config import config
from pages.footer_page import FooterPage
from pages.login_page import LoginPage

@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    driver.get(config.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_twitter(setup):
    login = LoginPage(setup)

    # Login
    login.enter_username(config.USERNAME)
    login.enter_password(config.PASSWORD)
    login.click_login()

    footer = FooterPage(setup)
    time.sleep(2)
    footer.click_twitter_icon()
    time.sleep(2)
    footer.click_facebook_icon()
    time.sleep(2)
    footer.click_linkedin_icon()
    time.sleep(2)