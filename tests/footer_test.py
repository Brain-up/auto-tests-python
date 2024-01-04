import allure
import pytest
from pages.footer_page import FooterPage
from pages.login_page import LoginPage
from locators.locators import FooterLocators
from test_data.links import PagesUrls, MainPageLinks
from test_data.data import FooterData


@allure.epic("Test Footer")
class TestFooter:
    class TestFooterCommon:
        locators = FooterLocators()
        urls = PagesUrls

        @allure.title("Visibility of Footer on each page")
        @pytest.mark.parametrize("element_locator", locators.FOOTER_ELEMENTS_LOCATORS.values())
        @pytest.mark.parametrize("url", urls.pages_urls)
        def test_fp_01_01_verify_visibility_of_footer_elements_on_pages(self, driver, element_locator, url):
            page = FooterPage(driver, url)
            page.open()
            assert page.element_is_visible(element_locator), f"Element in Footer is invisible on the page {url}"

        @allure.title("Correctness of texts in Footer on each page")
        @pytest.mark.parametrize("element_locator, expected_text",
                                 zip(locators.FOOTER_TEXT_LOCATORS.values(),
                                     FooterData.footer_elements_text.values())
                                 )
        @pytest.mark.parametrize("url", urls.pages_urls)
        def test_fp_01_02_verify_text_of_elements_in_footer_on_pages(self, driver, element_locator, expected_text, url):
            page = FooterPage(driver, url)
            page.open()
            actual_text = page.get_text(element_locator)
            assert actual_text in expected_text, f"The actual text '{actual_text}' of the element does not match " \
                                                 f"any of the valid options '{' | '.join(expected_text)}' on the page {url}"

        @allure.title("Verify visibility and accuracy of the image in the JETBRAINS link in Footer on the Home Page")
        def test_fp_01_03_verify_image_visibility_and_accuracy_in_jetbrains_link(self, driver, main_page_open):
            page = FooterPage(driver)
            jetbrains_image = page.element_is_visible(self.locators.JETBRAINS_IMAGE)
            jetbrains_image_src = page.get_image_src(self.locators.JETBRAINS_IMAGE)
            jetbrains_image_alt = page.get_image_alt(self.locators.JETBRAINS_IMAGE)
            assert jetbrains_image is not None \
                   and jetbrains_image_src == FooterData.footer_images_src["jetbrains_img_src"] \
                   and jetbrains_image_alt == FooterData.footer_images_alt["jetbrains_img_alt"], \
                   f"The image in the {jetbrains_image_alt} link is invisible or inaccurate in Footer on the Home Page"

        @allure.title("Verify visibility and accuracy of the image in the РЕГ.РУ link in Footer on the Home Page")
        def test_fp_01_04_verify_image_visibility_and_accuracy_in_reg_link(self, driver, main_page_open):
            page = FooterPage(driver)
            reg_image = page.element_is_visible(self.locators.REG_IMAGE)
            reg_image_src = page.get_image_src(self.locators.REG_IMAGE)
            reg_image_alt = page.get_image_alt(self.locators.REG_IMAGE)
            assert reg_image is not None \
                   and reg_image_src == FooterData.footer_images_src["reg_img_src"] \
                   and reg_image_alt == FooterData.footer_images_alt["reg_img_alt"], \
                   f"The image in the {reg_image_alt} link is invisible or inaccurate in Footer on the Home Page"

        @allure.title("Verify visibility and accuracy of the image in the ARASAAC link in Footer on the Home Page")
        def test_fp_01_05_verify_image_visibility_and_accuracy_in_arasaac_link(self, driver, main_page_open):
            page = FooterPage(driver)
            arasaac_image = page.element_is_visible(self.locators.ARASAAC_IMAGE)
            arasaac_image_src = page.get_image_src(self.locators.ARASAAC_IMAGE)
            arasaac_image_alt = page.get_image_alt(self.locators.ARASAAC_IMAGE)
            print(arasaac_image_alt)
            assert arasaac_image is not None \
                   and arasaac_image_src == FooterData.footer_images_src["arasaac_img_src"] \
                   and arasaac_image_alt == FooterData.footer_images_alt["arasaac_img_alt"], \
                   f"The image in the {arasaac_image_alt} link is invisible or inaccurate in Footer on the Home Page"

    class TestFooterForAuthorizedUsersOnly:

        @allure.title("Verify Footer invisibility through the modal window of the exercise")
        def test_fp_02_01_verify_footer_invisibility_through_the_modal_window(self, driver, main_page_open):
            page = LoginPage(driver)
            page.login_user()

            modal_window_page = FooterPage(driver, MainPageLinks.URL_OF_EXERCISE_1_MODAL_WINDOW_PAGE)
            modal_window_page.open()

            footer_presence = modal_window_page.check_footer_presence()
            jetbrains_image_presence = modal_window_page.check_jetbrains_image_presence()
            footer_invisibility = modal_window_page.check_footer_invisibility()
            jetbrains_image_invisibility = modal_window_page.check_jetbrains_image_invisibility()
            assert (footer_presence and jetbrains_image_presence) \
                   and (footer_invisibility and jetbrains_image_invisibility), \
                   "Footer (including the Jetbrains image) is not present in the DOM tree " \
                   "or is visible through the modal window"
