from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PASSWORD_RECOVERY = (By.XPATH, '//a[@href="/password-recovery"]')
    EMAIL_INPUT = (By.ID, 'email-input')
    SEND_EMAIL = (By.CSS_SELECTOR, 'form [type="button"]')
    NEW_PASSWORD = (By.XPATH, '//input[@name="newPassword"]')
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SUCCESSFUL_MESSAGE = (By.XPATH, '//p[@class="firebaseui-text"]')
    PROFILE = (By.XPATH, '//a[@href="/profile"]')
    WRONG_AUTH_DATA_MSG = (By.XPATH, '//p[contains(@class, "text-red-500")]')
