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
    PROFILE_USER = (By.XPATH, '//a[@href="/profile"]')

    SPEECH_EXERCISES_RU = (By.XPATH, '//a[@title="Речевые упражнения"]')
    SPEECH_EXERCISES_EN = (By.XPATH, '//a[@title="Speech"]')

    # Speech exercises_EN Header
    WORDS_BUTTON = (By.XPATH, '//button[@data-test-active-link = "Words"]')


class SpeechExercisesPageLocators:
    """
    link: https://brainup.site/groups/2/series/1
    """

    # Cards
    FAMILY_CARD_RU = (By.XPATH, '//a[@title="Слова про семью"]')
    FAMILY_CARD_EN = (By.XPATH, '//a[@title="Family words"]')


class ProfilePageLocators:
    PASSWORD_RECOVERY = (By.XPATH, '//a[@href="/password-recovery"]')
    EMAIL_INPUT = (By.ID, 'email-input')
    SEND_EMAIL = (By.CSS_SELECTOR, 'form [type="button"]')
    NEW_PASSWORD = (By.XPATH, '//input[@name="newPassword"]')
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SUCCESSFUL_MESSAGE = (By.XPATH, '//p[@class="firebaseui-text"]')


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

    FOOTER_TEXT_LOCATORS = {
        "CONTACT_US_LINK": (By.CSS_SELECTOR, "footer a[title]"),
        "WITH_THE_SUPPORT_PHRASE": (By.CSS_SELECTOR, "footer [data-test-support-message]")
    }
