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


class AuthorizedUserHomePageLocators:
    """
    link: https://brainup.site/groups?locale=ru-ru
    """
    # Header
    EN_BUTTON = (By.XPATH, "//*[contains(text(),'EN')]")
    RU_BUTTON = (By.XPATH, "//*[contains(text(),'RU')]")

    SPEECH_EXERCISES = (By.XPATH, '//a[@title="Речевые упражнения"]')


class SpeechExercisesPageLocators:
    """
    link: https://brainup.site/groups/2/series/1
    """
    FAMILY_CARD = (By.XPATH, '//a[@title="Слова про семью"]')


class FooterLocators:
    FOOTER_ELEMENTS_LOCATORS = {
        "FOOTER_SECTION": (By.TAG_NAME, "footer"),
        "FOOTER_CONTENT": (By.CSS_SELECTOR, "footer > div"),
        "CONTACT_US_LINK": (By.CSS_SELECTOR, "footer a[title]"),
        "WITH_THE_SUPPORT_PHRASE": (By.CSS_SELECTOR, "footer [data-test-support-message]"),
        "JETBRAINS_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(1)"),
        "REG_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(2)"),
        "ARASAAC_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(3)"),
        "SELECTEL_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(4)"),
        "EPAM_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(5)")
    }
