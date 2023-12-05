from selenium.webdriver.common.by import By


class BasePageLocators:
    """Locators for main page https://brainup.site/groups"""
    DESCRIPTION_PAGE = (By.ID, "ember5")
    TELEGRAM_PAGE = (By.XPATH, "//*[contains(text(),'Telegram')]")
    MORE_MENU = (By.CSS_SELECTOR, "#other-menu")
    DONATE_PAGE = (By.XPATH, "//div[@id='other-menu']//a[1]")
    CONTACTS = (By.ID, "ember6")
    SPECIALISTS_PAGE = (By.ID, "ember7")
    GITHUB = (By.XPATH, "//div[@id='other-menu']//a[2]")
    CONTRIBUTORS_PAGE = (By.XPATH, "//div[@id='other-menu']//a[6]")
    USED_RESOURCES_PAGE = (By.XPATH, "//div[@id='other-menu']//a[7]")
