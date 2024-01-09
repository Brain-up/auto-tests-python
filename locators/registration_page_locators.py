from selenium.webdriver.common.by import By


class RegistrationPageLocators:

    FIRST_NAME = (By.ID, 'firstName')
    BIRTHDAY = (By.ID, 'birthday')
    FEMALE = (By.ID, 'female')
    MALE = (By.ID, 'male')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    REPEAT_PASSWORD = (By.ID, 'repeatPassword')
    AGREEMENT = (By.ID, 'agreement')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    ERROR_MESSAGE = (By.XPATH, '//p[contains(@class, "text-red-500")]')
