"""Locators of web elements on the 'Contacts' page"""
from selenium.webdriver.common.by import By


class ContactsPageLocators:
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_DIVIDING_LINE = (By.TAG_NAME, "hr")
    PAGE_STRUCTURE = (By.XPATH, "//main/*")
    PAGE_SECTIONS = (By.TAG_NAME, "section")
    SECTION_1_FIRST_LEVEL_ELEMENTS = (By.XPATH, "(//section)[1]/*")
    SECTION_1_TITLE = (By.TAG_NAME, "h1")
    SECTION_2_FIRST_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*")
    SECTION_2_SECOND_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*/*")
    SECTION_2_SUBTITLES = (By.TAG_NAME, "h2")
    SECTION_2_THIRD_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*/*/*")
    SECTION_2_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*/*/*/*")
    SECTION_2_TEXT_PAR = (By.XPATH, "//section//li")
    SECTION_2_FIFTH_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*/*/*/*/*")
    SECTION_2_LINKS = (By.XPATH, "//section//a")
    SECTION_2_LINK_EMAIL = (By.PARTIAL_LINK_TEXT, "@")
    SECTION_2_LINKS_TM = (By.PARTIAL_LINK_TEXT, "https")
    SECTION_2_LINKS_TM_1 = (By.XPATH, "(//section//a)[1]")
    SECTION_2_LINKS_TM_2 = (By.XPATH, "(//section//a)[3]")
