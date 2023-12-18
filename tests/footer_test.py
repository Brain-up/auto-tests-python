from pages.base_page import BasePage
from locators.locators import FooterLocators
from test_data.links import PagesUrls
import pytest


class TestFooterParameterization:
    locators = FooterLocators()

    @pytest.mark.parametrize("element_locator", locators.FOOTER_ELEMENTS_LOCATORS.values())
    @pytest.mark.parametrize("url", PagesUrls.PAGES_URLS)
    def test_fp_01_verify_visibility_of_footer_elements_on_pages(self, driver, element_locator, url):
        """Checks if elements in Footer are visible on each page specified in PAGES_URLS"""
        page = BasePage(driver, url)
        page.open()
        assert page.element_is_visible(element_locator), f"Element in Footer is invisible on the page {url}"
