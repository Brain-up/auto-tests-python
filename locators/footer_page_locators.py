from selenium.webdriver.common.by import By


class FooterLocators:
    FOOTER_ELEMENTS_LOCATORS = {
        "FOOTER_SECTION": (By.TAG_NAME, "footer"),
        "FOOTER_CONTENT": (By.CSS_SELECTOR, "footer > div"),
        "ARASAAC_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(3)"),
        "CONTACT_US_LINK": (By.CSS_SELECTOR, "footer a[title]"),
        "EPAM_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(5)"),
        "JETBRAINS_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(1)"),
        "REG_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(2)"),
        "SELECTEL_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(4)"),
        "WITH_THE_SUPPORT_PHRASE": (By.CSS_SELECTOR, "footer [data-test-support-message]")
    }

    FOOTER_TEXT_LOCATORS = {
        "CONTACT_US_LINK": (By.CSS_SELECTOR, "footer a[title]"),
        "WITH_THE_SUPPORT_PHRASE": (By.CSS_SELECTOR, "footer [data-test-support-message]")
    }

    FOOTER_LINKS_LOCATORS = {
        "ARASAAC_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(3)"),
        "CONTACT_US_LINK": (By.CSS_SELECTOR, "footer a[title]"),
        "EPAM_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(5)"),
        "JETBRAINS_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(1)"),
        "REG_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(2)"),
        "SELECTEL_LINK": (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(4)")
    }

    ARASAAC_IMAGE = (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(3) img")
    EPAM_IMAGE = (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(5) img")
    FOOTER_SECTION = (By.TAG_NAME, "footer")
    JETBRAINS_IMAGE = (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(1) img")
    JETBRAINS_LINK = (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(1) a")
    # body > footer > div > div.flex.items - center > div: nth - child(2) > ul > li:nth - child(1) > a
    REG_IMAGE = (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(2) img")
    SELECTEL_IMAGE = (By.CSS_SELECTOR, "footer [data-test-support-logo]:nth-child(4) img")
