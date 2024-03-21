"""Locators of web elements on the 'Specialists' page"""

from selenium.webdriver.common.by import By


class SpecialistsPageLocators:
    PAGE_GRID = (By.XPATH, "//div[contains(@class, 'grid')]")
    PAGE_GRID_CONTENT = (By.XPATH, "//div[contains(@class, 'grid')]/div")
    PAGE_TEXT = (By.XPATH, "//div[contains(@class, 'text-lg')]")
    PAGE_TITLE = (By.TAG_NAME, "h2")
