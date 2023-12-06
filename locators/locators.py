from selenium.webdriver.common.by import By


class BasePageLocators:
    """
    Locators for main page.
    URL: https://brainup.site
    """
    DESCRIPTION_PAGE = (By.ID, "ember5")
    TELEGRAM_PAGE = (By.XPATH, "//*[contains(text(),'Telegram')]")
    MORE_MENU = (By.CSS_SELECTOR, "#other-menu")
    DONATE_PAGE = (By.XPATH, "//div[@id='other-menu']//a[1]")
    CONTACTS = (By.ID, "ember6")
    SPECIALISTS_PAGE = (By.ID, "ember7")
    GITHUB = (By.XPATH, "//div[@id='other-menu']//a[2]")
    CONTRIBUTORS_PAGE = (By.XPATH, "//div[@id='other-menu']//a[6]")
    USED_RESOURCES_PAGE = (By.XPATH, "//div[@id='other-menu']//a[7]")
    LOGIN_BUTTON = (By.XPATH, '//a[@id="ember11"]')


class LoginPageLocators:
    """
    Locators for login page.
    URL:  https://brainup.site/login
    """
    INPUT_LOGIN = (By.XPATH, '//input[@id="login"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id="password"]')
    SIGN_IN_BUTTON = (By.XPATH, '//*[@type="submit"]')
