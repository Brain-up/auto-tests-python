"""Locators of web elements on the 'Contributors' page"""
from selenium.webdriver.common.by import By


class ContributorsPageLocators:
    ALL_LINKS = (By.XPATH, "//section//a")
    ALL_TEAM_LINK = (By.XPATH, "//div[contains(@class, 'mt-20')]/a")
    # CARD_DESCRIPTIONS = (By.CSS_SELECTOR, ".leading-5")
    CARD_DESCRIPTIONS = (By.XPATH, "//div[contains(@class, 'leading-5')]")
    CARD_IMAGES = (By.CSS_SELECTOR, ".team-member img")
    CARD_LINKS = (By.CSS_SELECTOR, "a.mb-1")
    CONTRIBUTOR_CARDS = (By.CSS_SELECTOR, ".team-member")
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//main/*")
    PAGE_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//section/*")
    PAGE_THIRD_LEVEL_ELEMENTS = (By.XPATH, "//section/*/*")
    PAGE_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "//section/*/*/*")
    PAGE_FOURTH_LEVEL_CONTAINERS = (By.XPATH, "//section/*/*/div")
    PAGE_FIFTH_LEVEL_ELEMENTS = (By.XPATH, "//section/*/*/*/*")
    PAGE_LINKS = (By.XPATH, "//section//a")
    PAGE_SECTIONS = (By.TAG_NAME, "section")
    PAGE_SUBSECTIONS = (By.XPATH, "//section/div")
    PAGE_SUBTITLES = (By.TAG_NAME, "h3")
    PAGE_TEXT = (By.CSS_SELECTOR, ".mb-16")
    PAGE_TITLE = (By.TAG_NAME, "h2")
