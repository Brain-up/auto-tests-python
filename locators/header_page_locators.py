"""Locators of web elements in the HEADER on group of pages"""

from selenium.webdriver.common.by import By


class HeaderUnauthorizedLocators:
    HEADER_BUTTONS = (By.XPATH, "//button")
    HEADER_CONTENT = (By.XPATH, "//div[contains(@class, 'header')]")
    HEADER_LINKS_UNAUTH = (By.XPATH, "//nav//a")
    HEADER_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*")
    HEADER_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*")
    HEADER_THIRD_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*")
    HEADER_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*/*")
    HEADER_FIFTH_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*/*/*")
    HEADER_SIXTH_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*/*/*/*")
    LINK_ABOUT = (By.XPATH, "(//nav//a)[2]")
    LINK_CONTACTS = (By.XPATH, "(//nav//a)[6]")
    LINK_CONTRIBUTORS = (By.XPATH, "(//nav//a)[8]")
    LINK_DONATE = (By.XPATH, "(//nav//a)[4]")
    LINK_GITHUB = (By.XPATH, "(//nav//a)[5]")
    LINK_LOGO = (By.XPATH, "(//nav//a)[1]")
    LINK_REGISTRATION = (By.XPATH, "(//nav//a)[10]")
    LINK_SPECIALISTS = (By.XPATH, "(//nav//a)[7]")
    LINK_TELEGRAM = (By.XPATH, '//a[@href="https://t.me/BrainUpUsers"]')
    LINK_USED_RESOURCES = (By.XPATH, "(//nav//a)[9]")
    LINKS_IN_MORE = (By.XPATH, "//div[contains(@class, 'bottom')]/a")
    # LINK_ABOUT = (By.XPATH, "//div[contains(@class, 'text-s')]/a[1]")
    # LINK_CONTACTS = (By.XPATH, "//div[contains(@class, 'bottom')]/a[3]")
    # LINK_CONTRIBUTORS = (By.XPATH, "//div[contains(@class, 'bottom')]/a[5]")
    # LINK_DONATE = (By.XPATH, "//div[contains(@class, 'bottom')]/a[1]")
    # LINK_GITHUB = (By.XPATH, "//div[contains(@class, 'bottom')]/a[2]")
    # LINK_REGISTRATION = (By.ID, "ember10")
    # LINK_SPECIALISTS = (By.XPATH, "//div[contains(@class, 'bottom')]/a[4]")
    # LINK_TELEGRAM = (By.XPATH, "(//nav//a)[3]")
    # LINK_TELEGRAM = (By.XPATH, "//div[contains(@class, 'text-s')]/a[2]")
    # LINK_USED_RESOURCES = (By.XPATH, "//div[contains(@class, 'bottom')]/a[6]")
    LINKS2 = (By.XPATH, "//div[contains(@class, 'text-s')]/a")
    LOGO_IMAGE_UNAUTH = (By.XPATH, "//nav//*[name()='svg']")
    LOGO_LINK = (By.XPATH, "//a[@data-test-logo]")
    LOGO_SECTION = (By.XPATH, "//nav/div")
    MORE_BUTTON = (By.ID, "other-menu")
    EN_BUTTON = (By.XPATH, "(//span/button)[2]")
    RU_BUTTON = (By.XPATH, "(//span/button)[1]")
    RU_EN_BUTTONS = (By.XPATH, "//span/button")
    RU_EN_BUTTONS_SECTION = (By.XPATH, "//nav//span")


class HeaderAuthorizedLocators:
    HEADER_LINKS_AUTH = (By.XPATH, "//nav//a")
    ICON_HEADPHONE = (By.XPATH, "(//nav//*[name()='svg'])[2]")
    LINK_PROFILE = (By.XPATH, "(//nav//a)[12]")
    LINK_TELEGRAM_AUTH = (By.XPATH, "(//nav//a)[5]")
    LOGO_IMAGE_AUTH = (By.XPATH, "(//nav//*[name()='svg'])[1]")
    LOGOUT_BUTTON = (By.XPATH, "//button[@data-test-logout-button]")
    LOGOUT_ICON = (By.XPATH, "(//nav//*[name()='svg'])[3]")


class StartPagesLocators:
    START_AUTHORIZED_PAGE_TITLE = (By.XPATH, "//h3")
    START_UNAUTHORIZED_PAGE_TITLE = (By.XPATH, "(//h2)[2]")
