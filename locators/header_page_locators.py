"""Locators of web elements in the HEADER on group of pages"""

from selenium.webdriver.common.by import By


class HeaderPageLocators:
    MORE_MENU = (By.ID, "other-menu")
    SPECIALISTS_LINK_IN_MORE_MENU = (By.ID, "ember7")
