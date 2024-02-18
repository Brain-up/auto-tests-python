from selenium.webdriver.common.by import By


class UsedResourcesPageLocators:
    PAGE_TITLE = (By.TAG_NAME, "h1")
    PAGE_TEXT = (By.XPATH, "//section/p")
    LINKS_SECTION = (By.XPATH, "//section/ul")
    FREEPIK_COM_LINK = (By.XPATH, "(//section//li)[1]/a")
    FREEPIK_COM_LINK_SECTION = (By.XPATH, "(//section//li)[1]")


class RelatedPagesElementsLocators:
    # on freepik.com web page
    FREEPIK_COM_TEXT = (By.XPATH, "//main//h1")
