"""Locators of web elements in the HEADER on group of pages"""

from selenium.webdriver.common.by import By


class HeaderPageLocators:
    HEADER_CONTENT = (By.XPATH, "//div[contains(@class, 'header')]")
    HEADER_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*")
    HEADER_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*")
    HEADER_THIRD_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*")
    HEADER_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*/*")
    HEADER_FIFTH_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*/*/*")
    HEADER_SIXTH_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'header')]/*/*/*/*/*/*")
    LOGO_LINK = (By.XPATH, "//a[@data-test-logo]")
    MORE_MENU = (By.ID, "other-menu")
    CONTACTS_LINK_IN_MORE_MENU = (By.ID, "ember6")
    SPECIALISTS_LINK_IN_MORE_MENU = (By.ID, "ember7")
