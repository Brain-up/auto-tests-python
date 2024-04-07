"""Locators of web elements on the starting page for unauthorized users"""

from selenium.webdriver.common.by import By


class StartUnauthorizedPageLocators:
    UNAUTH_START_PAGE_TITLE_1 = (By.XPATH, "(//h2)[1]")
    UNAUTH_START_PAGE_TEXT_1 = (By.XPATH, "//p[contains(@class, 'text-lg')]")
