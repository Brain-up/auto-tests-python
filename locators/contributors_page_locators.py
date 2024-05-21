"""Locators of web elements on the 'Contributors' page"""
from selenium.webdriver.common.by import By


class ContributorsPageLocators:
    ALL_TEAM_LINK = (By.XPATH, "(//section//a)[67]")
    GRID_CARD_DESCRIPTIONS = (By.CSS_SELECTOR, ".leading-5")
    GRID_CARD_IMAGES = (By.CSS_SELECTOR, ".team-member img")
    GRID_CARD_LINKS = (By.CSS_SELECTOR, "a.mb-1")
    GRID_CONTRIBUTOR_CARDS = (By.CSS_SELECTOR, ".team-member")
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_STRUCTURE = (By.XPATH, "//main/*")
    PAGE_SECTIONS = (By.TAG_NAME, "section")
    PAGE_SUBSECTIONS = (By.XPATH, "//section/div")
    SECTION_SUBTITLES = (By.TAG_NAME, "h3")
    SECTION_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//section/*")
    SECTION_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "//section/*/*/*/*")
    SECTION_LINKS = (By.XPATH, "//section//a")
    SECTION_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//section/*/*")
    SECTION_THIRD_LEVEL_ELEMENTS = (By.XPATH, "//section/*/*/*")
    SECTION_THIRD_LEVEL_CONTAINERS = (By.XPATH, "//section/*/*/div")
    SECTION_TITLE = (By.TAG_NAME, "h2")
    SLOGAN = (By.CSS_SELECTOR, ".mb-16")
