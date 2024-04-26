"""Locators of web elements on the 'Contacts' page"""
from selenium.webdriver.common.by import By


class ContactsPageLocators:
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_SECTIONS = (By.TAG_NAME, "section")
    SECTION_1_FIRST_LEVEL_ELEMENTS = (By.XPATH, "(//section)[1]/*")
    SECTION_2_FIRST_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*")
    SECTION_2_SECOND_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*/*")
    SECTION_2_THIRD_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*/*/*")
    SECTION_2_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*/*/*/*")
    SECTION_2_FIFTH_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*/*/*/*/*")
