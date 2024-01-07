import allure
import pytest
from pages.footer_page import FooterPage
from pages.login_page import LoginPage
from locators.locators import FooterLocators
from test_data.links import PagesUrls, SpecificExercisesUrls
from test_data.data import FooterData


@allure.epic("Test Footer")
class TestFooter:
    class TestFooterCommon:
        locators = FooterLocators()
        urls = PagesUrls

        @allure.title("Verify presence and visibility of Footer on each page specified in the kit")
        @pytest.mark.parametrize("element_locator", locators.FOOTER_ELEMENTS_LOCATORS.values())
        @pytest.mark.parametrize("url", urls.pages_urls)
        def test_fp_01_01_verify_presence_and_visibility_of_footer_elements_on_pages(self, driver, element_locator,
                                                                                     url):
            page = FooterPage(driver, url)
            page.open()
            assert page.element_is_visible(element_locator), \
                f"Element in Footer is absent or invisible on the page {url}"

        @allure.title("Verify accuracy of texts in Footer on each page specified in the kit")
        @pytest.mark.parametrize("element_locator, expected_text",
                                 zip(locators.FOOTER_TEXT_LOCATORS.values(),
                                     FooterData.footer_elements_text.values())
                                 )
        @pytest.mark.parametrize("url", urls.pages_urls)
        def test_fp_01_02_verify_text_in_elements_in_footer_on_pages(self, driver, element_locator, expected_text, url):
            page = FooterPage(driver, url)
            page.open()
            actual_text = page.get_text(element_locator)
            assert actual_text in expected_text, \
                f"The actual text '{actual_text}' of the element does not match any of the valid options" \
                f"'{' | '.join(expected_text)}' on the page {url}"

        @allure.title("Verify presence, visibility and accuracy of the image in the JETBRAINS link in Footer")
        def test_fp_01_03_verify_image_in_jetbrains_link(self, driver, main_page_open):
            page = FooterPage(driver)
            assert page.check_jetbrains_image_visibility() \
                   and page.get_jetbrains_image_src() == FooterData.footer_images_src["jetbrains_img_src"] \
                   and page.get_jetbrains_image_alt() == FooterData.footer_images_alt["jetbrains_img_alt"], \
                   "The image in the JETBRAINS link is absent or invisible or inaccurate in Footer"

        @allure.title("Verify presence, visibility and accuracy of the image in the REG.RU link in Footer")
        def test_fp_01_04_verify_image_in_reg_link(self, driver, main_page_open):
            page = FooterPage(driver)
            assert page.check_reg_image_visibility() \
                   and page.get_reg_image_src() == FooterData.footer_images_src["reg_img_src"] \
                   and page.get_reg_image_alt() == FooterData.footer_images_alt["reg_img_alt"], \
                   "The image in the REG.RU link is absent or invisible or inaccurate in Footer"

        @allure.title("Verify presence, visibility and accuracy of the image in the ARASAAC link in Footer")
        def test_fp_01_05_verify_image_in_arasaac_link(self, driver, main_page_open):
            page = FooterPage(driver)
            assert page.check_arasaac_image_visibility() \
                   and page.get_arasaac_image_src() == FooterData.footer_images_src["arasaac_img_src"] \
                   and page.get_arasaac_image_alt() == FooterData.footer_images_alt["arasaac_img_alt"], \
                   "The image in the ARASAAC link is absent or invisible or inaccurate in Footer"

    class TestFooterForAuthorizedUserOnly:

        @allure.title("Verify Footer invisibility through the modal window with the exercise")
        def test_fp_02_01_verify_footer_invisibility_through_the_modal_window(self, driver, main_page_open):
            page = LoginPage(driver)
            page.login_user()

            modal_window_page = FooterPage(driver, SpecificExercisesUrls.URL_OF_EXERCISE_1_MODAL_WINDOW_PAGE)
            modal_window_page.open()
            assert (modal_window_page.check_footer_presence() and modal_window_page.check_jetbrains_image_presence()) \
                and (modal_window_page.check_footer_invisibility()
                     and modal_window_page.check_jetbrains_image_invisibility()), \
                "Footer (including the Jetbrains image) is absent or visible through the modal window"
