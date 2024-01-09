from selenium.webdriver.common.by import By


class AuthorizedUserHomePageLocators:
    """
    link: https://brainup.site/groups?locale=ru-ru
    """
    # Header
    EN_BUTTON = (By.XPATH, "//*[contains(text(),'EN')]")
    RU_BUTTON = (By.XPATH, "//*[contains(text(),'RU')]")
    PROFILE_USER = (By.XPATH, '//a[@href="/profile"]')

    SPEECH_EXERCISES_RU = (By.XPATH, '//a[@title="Речевые упражнения"]')
    SPEECH_EXERCISES_EN = (By.XPATH, '//a[@title="Speech"]')

    # Speech exercises_EN Header
    WORDS_BUTTON = (By.XPATH, '//button[@data-test-active-link = "Words"]')
