import allure
from pages.base_page import BasePage
from locators.locators import FooterLocators
from test_data.links import PagesUrls
from test_data.data import FooterData
import pytest


@allure.epic("Test Footer")
class TestFooter:
    locators = FooterLocators()
    urls = PagesUrls

    @allure.title("Visibility of Footer on each page")
    @pytest.mark.parametrize("element_locator", locators.FOOTER_ELEMENTS_LOCATORS.values())
    @pytest.mark.parametrize("url", urls.pages_urls)
    def test_fp_01_verify_visibility_of_footer_elements_on_pages(self, driver, element_locator, url):
        page = BasePage(driver, url)
        page.open()
        assert page.element_is_visible(element_locator), f"Element in Footer is invisible on the page {url}"

    @allure.title("Correctness of texts in Footer on each page")
    @pytest.mark.parametrize("element_locator, expected_text",
                             zip(locators.FOOTER_TEXT_LOCATORS.values(),
                                 FooterData.footer_elements_text.values())
                             )
    @pytest.mark.parametrize("url", urls.pages_urls)
    def test_fp_02_verify_text_of_elements_in_footer_on_pages(self, driver, element_locator, expected_text, url):
        page = BasePage(driver, url)
        page.open()
        actual_text = page.get_text(element_locator)
        assert actual_text in expected_text, f"The actual text '{actual_text}' of the element does not match " \
                                             f"any of the valid options '{' | '.join(expected_text)}' on the page {url}"
