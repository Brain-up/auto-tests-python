from selenium.webdriver.common.by import By


class LoginPageLocators:
    """
    Locators for login page.
    URL:  https://brainup.site/login
    """
    INPUT_LOGIN = (By.XPATH, '//input[@id="login"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id="password"]')
    SIGN_IN_BUTTON = (By.XPATH, '//*[@type="submit"]')
    SIGN_IN_TAB = (By.XPATH, '//div[contains(@class, "tracking")]')
