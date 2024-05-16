"""Locators of web elements on the 'Contributors' page"""
from selenium.webdriver.common.by import By


class ContributorsPageLocators:
    GRID_CARD_DESCRIPTIONS = (By.XPATH, "//div[contains(@class, 'team')]/div[contains(@class, 'Sans')]")
    GRID_CARD_IMAGES = (By.XPATH, "//div[contains(@class, 'team-member')]//img")
    GRID_CARD_LINKS = (By.XPATH, "//div[contains(@class, 'team-member')]//a")
    GRID_CONTRIBUTOR_CARDS = (By.XPATH, "//div[contains(@class, 'team-member')]")
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_STRUCTURE = (By.XPATH, "//main/*")
    PAGE_SECTIONS = (By.TAG_NAME, "section")
    PAGE_SUBSECTIONS = (By.XPATH, "//section/div")
    SECTION_SUBTITLES = (By.TAG_NAME, "h3")
    SECTION_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//section/*")
    SECTION_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "//section/*/*/*/*")
    SECTION_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//section/*/*")
    SECTION_THIRD_LEVEL_ELEMENTS = (By.XPATH, "//section/*/*/*")
    SECTION_THIRD_LEVEL_CONTAINERS = (By.XPATH, "//section/*/*/div")
    SECTION_TITLE = (By.TAG_NAME, "h2")

