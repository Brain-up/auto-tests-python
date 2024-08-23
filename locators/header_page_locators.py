"""Locators of web elements in the HEADER on group of pages"""

from selenium.webdriver.common.by import By


class HeaderPageLocators:
    CONTACTS_LINK_IN_MORE_MENU = (By.ID, "ember6")
    HEADER_CONTENT = (By.XPATH, "//div[contains(@class, 'header')]")
    HEADER_LINKS = (By.XPATH, "//nav//a")
    HEADER_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*")
    HEADER_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*")
    HEADER_THIRD_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*")
    HEADER_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*/*")
    HEADER_FIFTH_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*/*/*")
    HEADER_SIXTH_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*/*/*/*")
    LINK_ABOUT = (By.XPATH, "(//div)[4]/div/a[1]")
    LINK_TELEGRAM = (By.XPATH, "(//div)[4]/div/a[2]")
    LINKS2 = (By.XPATH, "(//div)[4]/div/a")
    LOGO_IMAGE = (By.XPATH, "//nav//*[name()='svg']")
    LOGO_LINK = (By.XPATH, "//a[@data-test-logo]")
    LOGO_SECTION = (By.XPATH, "//nav/div")
    MORE_MENU = (By.ID, "other-menu")
    RU_EN_BUTTONS = (By.XPATH, "//nav//span/*")
    RU_EN_BUTTONS_SECTION = (By.XPATH, "//nav//span")
    SPECIALISTS_LINK_IN_MORE_MENU = (By.ID, "ember7")
