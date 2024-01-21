from selenium.webdriver.common.by import By


class DescriptionPageLocators:
    """
    Locators for main page.
    URL: https://brainup.site/description
    """
    TELEGRAM_PAGE = (By.XPATH, "//*[contains(text(),'Telegram')]")
    MORE_MENU = (By.CSS_SELECTOR, "#other-menu")
    DONATE_PAGE = (By.XPATH, "//div[@id='other-menu']//a[1]")
    CONTACTS = (By.ID, "ember6")
    SPECIALISTS_PAGE = (By.ID, "ember7")
    GITHUB = (By.XPATH, "//div[@id='other-menu']//a[2]")
    CONTRIBUTORS_PAGE = (By.XPATH, '//a[@id="ember8"]')
    USED_RESOURCES_PAGE = (By.XPATH, '//a[@id="ember9"]')
    LOGIN_BUTTON = (By.XPATH, '//a[@id="ember11"]')
    BUTTON_START = (By.ID, "ember11")
    REGISTRATION_BUTTON = (By.XPATH, '//a[@href="/registration"]')
    LOGO = (By.ID, "ember4")

