import allure
import pytest
from pages.footer_page import FooterPage
from locators.footer_page_locators import FooterLocators
from test_data.links import PagesUrls, SpecificExercisesUrls
from test_data.footer_data import FooterData


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

        @allure.title("Verify presence, visibility and accuracy of the image in the Selectel link in Footer")
        def test_fp_01_06_verify_image_in_selectel_link(self, driver, main_page_open):
            page = FooterPage(driver)
            assert page.check_selectel_image_visibility() \
                   and page.get_selectel_image_src() == FooterData.footer_images_src["selectel_img_src"] \
                   and page.get_selectel_image_alt() == FooterData.footer_images_alt["selectel_img_alt"], \
                   "The image in the Selectel link is absent or invisible or inaccurate in Footer"

        @allure.title("Verify presence, visibility and accuracy of the image in the EPAM link in Footer")
        def test_fp_01_07_verify_image_in_epam_link(self, driver, main_page_open):
            page = FooterPage(driver)
            assert page.check_epam_image_visibility() \
                   and page.get_epam_image_src() == FooterData.footer_images_src["epam_img_src"] \
                   and page.get_epam_image_alt() == FooterData.footer_images_alt["epam_img_alt"], \
                   "The image in the EPAM link is absent or invisible or inaccurate in Footer"

        @allure.title("Verify accuracy of the attribute 'href' in the Jetbrains link in Footer")
        def test_fp_01_08_verify_href_in_jetbrains_link(self, driver, main_page_open):
            page = FooterPage(driver)
            assert page.get_jetbrains_link_href() == FooterData.footer_links_href["jetbrains_link_href"], \
                "The attribute 'href' of the Jetbrains link does not match the expected value"

        @allure.title("Verify accuracy of the attribute 'href' in the REG.RU link in Footer")
        def test_fp_01_09_verify_href_in_reg_link(self, driver, main_page_open):
            page = FooterPage(driver)
            assert page.get_reg_link_href() == FooterData.footer_links_href["reg_link_href"], \
                f"The attribute 'href' of the link REG.RU does not match the expected value"

        @allure.title("Verify accuracy of the attribute 'href' in the ARASAAC link in Footer")
        def test_fp_01_10_verify_href_in_arasaac_link(self, driver, main_page_open):
            page = FooterPage(driver)
            assert page.get_arasaac_link_href() == FooterData.footer_links_href["arasaac_link_href"], \
                f"The attribute 'href' of the ARASAAC link does not match the expected value"

    class TestFooterForAuthorizedUserOnly:

        @allure.title("Verify Footer invisibility through the modal window with the exercise")
        def test_fp_02_01_verify_footer_invisibility_through_the_modal_window(self, driver, auto_test_user_authorized):
            modal_window_page = FooterPage(driver, SpecificExercisesUrls.URL_OF_EXERCISE_1_MODAL_WINDOW_PAGE)
            modal_window_page.open()
            assert (modal_window_page.check_footer_presence() and modal_window_page.check_jetbrains_image_presence()) \
                and (modal_window_page.check_footer_invisibility()
                     and modal_window_page.check_jetbrains_image_invisibility()), \
                "Footer (including the Jetbrains image) is absent or visible through the modal window"
