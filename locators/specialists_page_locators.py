"""Locators of web elements on the 'Specialists' page"""

from selenium.webdriver.common.by import By


class SpecialistsPageLocators:
    GRID_CARD_01_IMAGE = (By.XPATH, "(//img[@class='rounded-full'])[1]")
    PAGE_GRID = (By.XPATH, "//div[contains(@class, 'grid')]")
    PAGE_GRID_CONTENT = (By.XPATH, "//div[contains(@class, 'rounded-lg')]")
    PAGE_TEXT = (By.XPATH, "//div[contains(@class, 'text-lg')]")
    PAGE_TITLE = (By.TAG_NAME, "h2")
