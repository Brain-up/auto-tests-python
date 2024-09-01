"""Locators of web elements in the HEADER on group of pages"""

from selenium.webdriver.common.by import By


class HeaderPageLocators:
    CONTACTS_LINK = (By.ID, "ember6")
    HEADER_BUTTONS = (By.XPATH, "//button")
    HEADER_CONTENT = (By.XPATH, "//div[contains(@class, 'header')]")
    HEADER_LINKS = (By.XPATH, "//nav//a")
    HEADER_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*")
    HEADER_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*")
    HEADER_THIRD_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*")
    HEADER_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*/*")
    HEADER_FIFTH_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*/*/*")
    HEADER_SIXTH_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*/*/*/*")
    LINK_ABOUT = (By.XPATH, "//div[contains(@class, 'text-s')]/a[1]")
    LINK_TELEGRAM = (By.XPATH, "//div[contains(@class, 'text-s')]/a[2]")
    LINKS2 = (By.XPATH, "//div[contains(@class, 'text-s')]/a")
    LINKS3 = (By.XPATH, "//div[contains(@class, 'bottom')]/a")
    LOGO_IMAGE = (By.XPATH, "//nav//*[name()='svg']")
    LOGO_LINK = (By.XPATH, "//a[@data-test-logo]")
    LOGO_SECTION = (By.XPATH, "//nav/div")
    MORE_BUTTON = (By.ID, "other-menu")
    REGISTRATION_LINK = (By.ID, "ember10")
    RU_EN_BUTTONS = (By.XPATH, "//span/button")
    RU_EN_BUTTONS_SECTION = (By.XPATH, "//nav//span")
    SPECIALISTS_LINK = (By.ID, "ember7")
