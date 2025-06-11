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

def test_social_media_icons(setup):
    login = LoginPage(setup)

    # Login
    login.enter_username(config.USERNAME)
    login.enter_password(config.PASSWORD)
    login.click_login()

    footer = FooterPage(setup)
    time.sleep(2)
    footer.scroll_to_bottom()
    footer.click_twitter_icon()
    time.sleep(2)
    footer.switch_to_first_tab()
    footer.scroll_to_bottom()
    footer.click_facebook_icon()
    time.sleep(2)
    footer.switch_to_first_tab()
    footer.scroll_to_bottom()
    footer.click_linkedin_icon()
    time.sleep(2)

def test_sidebar(setup):
    login = LoginPage(setup)

    # Login
    login.enter_username(config.USERNAME)
    login.enter_password(config.PASSWORD)
    login.click_login()

    footer = FooterPage(setup)
    time.sleep(2)
    footer.click_hamburger_icon()
    footer.click_sidebar_1()
    assert "inventory" in setup.current_url
    footer.close_sidebar()
    footer.click_hamburger_icon()
    footer.click_sidebar_2()
    footer.go_back()

    footer.click_hamburger_icon()
    footer.click_sidebar_3()
    assert config.BASE_URL in setup.current_url
    login.enter_username(config.USERNAME)
    login.enter_password(config.PASSWORD)
    login.click_login()
    footer.click_hamburger_icon()
    footer.click_sidebar_4()
    assert "inventory" in setup.current_url
    footer.close_sidebar()
