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
    BUTTON_START = (By.ID, "ember11")


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
    BUTTON_START = (By.XPATH, '//button[@aria-label="Start exercise"]')
    LIST_CARD_WORDS_WE = (By.XPATH, '//li[@class="task-player__option flex"]')

    # Language
    FAMILY_CARD_RU = (By.XPATH, '//a[@title="Слова про семью"]')
    FAMILY_CARD_EN = (By.XPATH, '//a[@title="Family words"]')

    # SubGroups
    SIMILAR_PHRASES = (By.ID, 'ember313')
    WORDS_GROUP = (By.ID, 'ember314')
    SENTENCES = (By.ID, 'ember315')
    WORDS_GROUP_BY_FREQUENCY = (By.ID, 'ember316')
    WORDS = (By.ID, 'ember317')

    LIST_CARDS_ID = (By.XPATH, '//div[@class="flex"]')


class ProfilePageLocators:
    PASSWORD_RECOVERY = (By.XPATH, '//a[@href="/password-recovery"]')
    EMAIL_INPUT = (By.ID, 'email-input')
    SEND_EMAIL = (By.CSS_SELECTOR, 'form [type="button"]')
    NEW_PASSWORD = (By.XPATH, '//input[@name="newPassword"]')
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SUCCESSFUL_MESSAGE = (By.XPATH, '//p[@class="firebaseui-text"]')
    PROFILE = (By.CSS_SELECTOR, '#ember19 p')
    WRONG_AUTH_DATA_MSG = (By.XPATH, '//p[contains(@class, "text-red-500")]')


class FooterLocators:
    FOOTER_ELEMENTS_LOCATORS = {
        "FOOTER_SECTION": (By.TAG_NAME, "footer"),
        "FOOTER_CONTENT": (By.CSS_SELECTOR, "footer > div"),
        "ARASAAC_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(3)"),
        "CONTACT_US_LINK": (By.CSS_SELECTOR, "footer a[title]"),
        "EPAM_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(5)"),
        "JETBRAINS_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(1)"),
        "REG_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(2)"),
        "SELECTEL_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(4)"),
        "WITH_THE_SUPPORT_PHRASE": (By.CSS_SELECTOR, "footer [data-test-support-message]")
    }

    FOOTER_TEXT_LOCATORS = {
        "CONTACT_US_LINK": (By.CSS_SELECTOR, "footer a[title]"),
        "WITH_THE_SUPPORT_PHRASE": (By.CSS_SELECTOR, "footer [data-test-support-message]")
    }

    ARASAAC_IMAGE = (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(3) img")
    JETBRAINS_IMAGE = (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(1) img")
    REG_IMAGE = (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(2) img")
