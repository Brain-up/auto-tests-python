from selenium.webdriver.common.by import By


class UsedResourcesPageLocators:
    PAGE_TITLE = (By.TAG_NAME, "h1")
    PAGE_TEXT = (By.XPATH, "//section/p")
    LINKS_SECTION = (By.XPATH, "//section/ul")
    FLORA_LINK = (By.XPATH, "(//section//li)[3]/a")
    FLORA_LINK_SECTION = (By.XPATH, "(//section//li)[3]")
    FLORA_SECTION_ICON = (By.XPATH, "(//*[name()='svg'][@class])[3]")
    FREEPIK_COM_LINK = (By.XPATH, "(//section//li)[1]/a")
    FREEPIK_COM_LINK_SECTION = (By.XPATH, "(//section//li)[1]")
    FREEPIK_COM_SECTION_ICON = (By.XPATH, "(//*[name()='svg'][@class])[1]")
    PLANTS_LINK = (By.XPATH, "(//section//li)[2]/a")
    PLANTS_LINK_SECTION = (By.XPATH, "(//section//li)[2]")
    PLANTS_SECTION_ICON = (By.XPATH, "(//*[name()='svg'][@class])[2]")


class RelatedPagesElementsLocators:
    # on 'Flora' web page
    FLORA_TEXT = (By.XPATH, "//h2")
    # on freepik.com web page
    FREEPIK_COM_TEXT = (By.XPATH, "//main//h1")
    # on 'Plants' web page
    PLANTS_TEXT = (By.XPATH, "//h1/span")
