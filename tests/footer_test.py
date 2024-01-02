import allure
import pytest
from pages.footer_page import FooterPage
from locators.locators import FooterLocators
from test_data.links import PagesUrls
from test_data.data import FooterData


@allure.epic("Test Footer")
class TestFooter:
    locators = FooterLocators()
    urls = PagesUrls

    @allure.title("Visibility of Footer on each page")
    @pytest.mark.parametrize("element_locator", locators.FOOTER_ELEMENTS_LOCATORS.values())
    @pytest.mark.parametrize("url", urls.pages_urls)
    def test_fp_01_verify_visibility_of_footer_elements_on_pages(self, driver, element_locator, url):
        page = FooterPage(driver, url)
        page.open()
        assert page.element_is_visible(element_locator), f"Element in Footer is invisible on the page {url}"

    @allure.title("Correctness of texts in Footer on each page")
    @pytest.mark.parametrize("element_locator, expected_text",
                             zip(locators.FOOTER_TEXT_LOCATORS.values(),
                                 FooterData.footer_elements_text.values())
                             )
    @pytest.mark.parametrize("url", urls.pages_urls)
    def test_fp_02_verify_text_of_elements_in_footer_on_pages(self, driver, element_locator, expected_text, url):
        page = FooterPage(driver, url)
        page.open()
        actual_text = page.get_text(element_locator)
        assert actual_text in expected_text, f"The actual text '{actual_text}' of the element does not match " \
                                             f"any of the valid options '{' | '.join(expected_text)}' on the page {url}"

    @allure.title("Verify visibility and accuracy of the image in the JETBRAINS link in Footer on the Main Page")
    def test_fp_03_verify_image_visibility_and_accuracy_in_jetbrains_link(self, driver, main_page_open):
        page = FooterPage(driver)
        jetbrains_image = page.element_is_visible(self.locators.JETBRAINS_IMAGE)
        jetbrains_image_src = page.get_image_src(self.locators.JETBRAINS_IMAGE)
        jetbrains_image_alt = page.get_image_alt(self.locators.JETBRAINS_IMAGE)
        assert jetbrains_image is not None \
               and jetbrains_image_src == FooterData.footer_images_src["jetbrains_img_src"] \
               and jetbrains_image_alt == FooterData.footer_images_alt["jetbrains_img_alt"], \
               f"The image in the {jetbrains_image_alt} link is invisible or inaccurate in Footer on the Main Page"
