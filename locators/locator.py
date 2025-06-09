
#This file stores the locators of elements (like textbox, button, etc.)
#Each element is found using a strategy like By.ID or By.CSS_SELECTOR
#These are used in the Page Object class
#locator file like a map



from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "user-name")       #Just stores the locator info of username
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

class InventoryPageLocators:
    ADD_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_CART = (By.ID, "remove-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

class CartPageLocators:
    ITEM_VISIBLE = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_CART = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_BUTTON = (By.ID, "continue-shopping")

class CheckoutPageLocators:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")

class FinishCheckoutPageLocators:
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")

class CompletePageLocators:
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

class FooterPageLocators:
    TWITTER_ICON = (By.XPATH, '//a[@data-test="social-twitter"]')
    FACEBOOK_ICON = (By.XPATH, '//a[@data-test="social-facebook"]')
    LINKEDIN_ICON = (By.XPATH, '//a[@data-test="social-linkedin"]')