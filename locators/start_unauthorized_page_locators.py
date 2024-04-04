"""Locators of web elements on the start page for unauthorized users"""

from selenium.webdriver.common.by import By


class StartUnauthorizedPageLocators:
    UNAUTH_START_PAGE_TITLE_1 = (By.XPATH, "(//h2)[1]")
