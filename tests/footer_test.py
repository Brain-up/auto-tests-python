import allure
import pytest
import requests

from pages.footer_page import FooterPage
from locators.footer_page_locators import FooterLocators
from test_data.links import PagesUrls, SpecificExercisesUrls, FooterLinks
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

        @allure.title("Verify presence, visibility, clickability, href, status code of the ARASAAC link in Footer")
        def test_fp_01_03_verify_arasaac_link(self, driver, main_page_open):
            page = FooterPage(driver)
            link_presence = page.check_arasaac_link_presence()
            link_visibility = page.check_arasaac_link_visibility()
            link_clickability = page.check_arasaac_link_clickability()
            link_href = page.get_arasaac_link_href()
            link_status_code = requests.head(link_href).status_code
            assert link_presence is not None, "The ARASAAC link is absent"
            assert link_visibility, "The ARASAAC link is invisible"
            assert link_clickability, "The ARASAAC link is unclickable"
            assert link_href == FooterData.footer_links_href["arasaac_link_href"], \
                "The attribute 'href' of the ARASAAC link does not match the expected value"
            assert link_status_code == FooterData.footer_links_status_codes["arasaac_link_status_code"], \
                "The ARASAAC link status code does not match the expected value"

        @allure.title("Verify presence, visibility and accuracy of the EPAM link and link's image in Footer")
        def test_fp_01_04_verify_epam_link(self, driver, main_page_open):
            page = FooterPage(driver)
            link_presence_and_visibility = page.check_epam_link_presence_and_visibility()
            link_clickability = page.check_epam_link_clickability()
            link_href = page.get_epam_link_href()
            link_status_code = requests.head(link_href).status_code
            link_image_visibility = page.check_epam_image_visibility()
            link_image_src = page.get_epam_image_src()
            link_image_alt = page.get_epam_image_alt()
            assert link_presence_and_visibility is not None, "The EPAM link is absent or invisible"
            assert link_clickability is not None, "The EPAM link is unclickable"
            assert link_href == FooterData.footer_links_href["epam_link_href"], \
                "The attribute 'href' of the EPAM link does not match the expected value"
            assert link_status_code == FooterData.footer_links_status_codes["epam_link_status_code"], \
                "The EPAM link status code does not match the expected value"
            assert link_image_visibility is not None, "The EPAM link image is absent or invisible"
            assert link_image_src == FooterData.footer_images_src["epam_img_src"], "The EPAM link image is unaccurate"
            assert link_image_alt == FooterData.footer_images_alt["epam_img_alt"], "The EPAM link image is unaccurate"

        @allure.title("Verify presence, visibility and accuracy of the JETBRAINS link and link's image in Footer")
        def test_fp_01_05_verify_jetbrains_link(self, driver, main_page_open):
            page = FooterPage(driver)
            link_presence_and_visibility = page.check_jetbrains_link_presence_and_visibility()
            link_clickability = page.check_jetbrains_link_clickability()
            link_href = page.get_jetbrains_link_href()
            link_status_code = requests.head(link_href).status_code
            link_image_visibility = page.check_jetbrains_image_visibility()
            link_image_src = page.get_jetbrains_image_src()
            link_image_alt = page.get_jetbrains_image_alt()
            assert link_presence_and_visibility is not None, "The JETBRAINS link is absent or invisible"
            assert link_clickability is not None, "The JETBRAINS link is unclickable"
            assert link_href == FooterData.footer_links_href["jetbrains_link_href"], \
                "The attribute 'href' of the JETBRAINS link does not match the expected value"
            assert link_status_code == FooterData.footer_links_status_codes["jetbrains_link_status_code"], \
                "The JETBRAINS link status code does not match the expected value"
            assert link_image_visibility is not None, "The JETBRAINS link image is absent or invisible"
            assert link_image_src == FooterData.footer_images_src["jetbrains_img_src"], \
                "The JETBRAINS link image is unaccurate"
            assert link_image_alt == FooterData.footer_images_alt["jetbrains_img_alt"], \
                "The JETBRAINS link image is unaccurate"

        @allure.title("Verify presence, visibility and accuracy of the REG.RU link and link's image in Footer")
        def test_fp_01_06_verify_reg_link(self, driver, main_page_open):
            page = FooterPage(driver)
            link_presence_and_visibility = page.check_reg_link_presence_and_visibility()
            link_clickability = page.check_reg_link_clickability()
            link_href = page.get_reg_link_href()
            link_status_code = requests.head(link_href).status_code
            link_image_visibility = page.check_reg_image_visibility()
            link_image_src = page.get_reg_image_src()
            link_image_alt = page.get_reg_image_alt()
            assert link_presence_and_visibility is not None, "The REG.RU link is absent or invisible"
            assert link_clickability is not None, "The REG.RU link is unclickable"
            assert link_href == FooterData.footer_links_href["reg_link_href"], \
                "The attribute 'href' of the REG.RU link does not match the expected value"
            assert link_status_code in FooterData.footer_links_status_codes["reg_link_status_code"], \
                "The REG.RU link status code does not match any of the expected values"
            assert link_image_visibility is not None, "The REG.RU link image is absent or invisible"
            assert link_image_src == FooterData.footer_images_src["reg_img_src"], \
                "The REG.RU link image is unaccurate"
            assert link_image_alt == FooterData.footer_images_alt["reg_img_alt"], \
                "The REG.RU link image is unaccurate"

        @allure.title("Verify presence, visibility and accuracy of the Selectel link and link's image in Footer")
        def test_fp_01_07_verify_selectel_link(self, driver, main_page_open):
            page = FooterPage(driver)
            link_presence_and_visibility = page.check_selectel_link_presence_and_visibility()
            link_clickability = page.check_selectel_link_clickability()
            link_href = page.get_selectel_link_href()
            link_status_code = requests.head(link_href).status_code
            link_image_visibility = page.check_selectel_image_visibility()
            link_image_src = page.get_selectel_image_src()
            link_image_alt = page.get_selectel_image_alt()
            assert link_presence_and_visibility is not None, "The Selectel link is absent or invisible"
            assert link_clickability is not None, "The Selectel link is unclickable"
            assert link_href == FooterData.footer_links_href["selectel_link_href"], \
                "The attribute 'href' of the Selectel link does not match the expected value"
            assert link_status_code == FooterData.footer_links_status_codes["selectel_link_status_code"], \
                "The Selectel link status code does not match the expected value"
            assert link_image_visibility is not None, "The Selectel link image is absent or invisible"
            assert link_image_src == FooterData.footer_images_src["selectel_img_src"], \
                "The Selectel link image is unaccurate"
            assert link_image_alt == FooterData.footer_images_alt["selectel_img_alt"], \
                "The Selectel link image is unaccurate"

        @allure.title("Verify presence, visibility and accuracy of the Contact us link in Footer")
        def test_fp_01_08_verify_contact_us_link(self, driver, main_page_open):
            page = FooterPage(driver)
            link_presence_and_visibility = page.check_contact_us_link_presence_and_visibility()
            link_clickability = page.check_contact_us_link_clickability()
            link_href = page.get_contact_us_link_href()
            link_prefix_and_subject = page.check_contact_us_link_href()
            assert link_presence_and_visibility is not None, "The Contact us link is absent or invisible"
            assert link_clickability is not None, "The Contact us link is unclickable"
            assert link_href == FooterData.footer_links_href["contact_us_link_href"], \
                "The attribute 'href' of the Contact us link does not match the expected value"
            assert link_prefix_and_subject, \
                "The attribute 'href' of the Contact us link does not contain the proper prefix and/or subject"

    class TestFooterForAuthorizedUserOnly:

        @allure.title("Verify Footer invisibility through the modal window with the exercise")
        def test_fp_02_01_verify_footer_invisibility_through_the_modal_window(self, driver, auto_test_user_authorized):
            modal_window_page = FooterPage(driver, SpecificExercisesUrls.URL_OF_EXERCISE_1_MODAL_WINDOW_PAGE)
            modal_window_page.open()
            assert (modal_window_page.check_footer_presence() and modal_window_page.check_jetbrains_image_presence()), \
                "Footer (including the Jetbrains image) is absent in the DOM tree"
            assert (modal_window_page.check_footer_invisibility()
                    and modal_window_page.check_jetbrains_image_invisibility()), \
                "Footer (including the Jetbrains image) is visible through the modal window"

    class TestFooterNavigation:
        @allure.title("Verify that the ARASAAC link in Footer leads to the correct page after click")
        def test_fp_03_01_verify_arasaac_link_leads_to_the_correct_page(self, driver, main_page_open):
            page = FooterPage(driver)
            page.click_arasaac_link()
            page.switch_to_new_window()
            text_on_opened_tab = page.get_element_text_on_opened_arasaac_tab()
            assert text_on_opened_tab in FooterData.footer_related_elements_text["arasaac_start_page_text"], \
                "The ARASAAC link in Footer leads to an incorrect page after click " \
                "or opened page does not load correctly"

        @allure.title("Verify that the EPAM link in Footer leads to the correct page after click")
        def test_fp_03_02_verify_epam_link_leads_to_the_correct_page(self, driver, main_page_open):
            page = FooterPage(driver)
            page.click_epam_link()
            page.switch_to_new_window()
            text_on_opened_tab = page.get_element_text_on_opened_epam_tab()
            assert text_on_opened_tab == FooterData.footer_related_elements_text["epam_start_page_text"], \
                "The EPAM link in Footer leads to an incorrect page after click " \
                "or opened page does not load correctly"

        @allure.title("Verify that the JETBRAINS link in Footer leads to the correct page after click")
        def test_fp_03_03_verify_jetbrains_link_leads_to_the_correct_page(self, driver, main_page_open):
            page = FooterPage(driver)
            page.click_jetbrains_link()
            page.switch_to_new_window()
            text_on_opened_tab = page.get_element_text_on_opened_jetbrains_tab()
            assert text_on_opened_tab == FooterData.footer_related_elements_text["jetbrains_start_page_text"], \
                "The JETBRAINS link in Footer leads to an incorrect page after click " \
                "or opened page does not load correctly"

        @allure.title("Verify that the REG.RU link in Footer leads to the correct page after click")
        def test_fp_03_04_verify_reg_link_leads_to_the_correct_page(self, driver, main_page_open):
            page = FooterPage(driver)
            page.click_reg_link()
            page.switch_to_new_window()
            assert page.driver.current_url in FooterLinks.REG_LINK, \
                "The REG.RU link in Footer leads to an incorrect page after click"

        @allure.title("Verify that the SELECTEL link in Footer leads to the correct page after click")
        def test_fp_03_05_verify_selectel_link_leads_to_the_correct_page(self, driver, main_page_open):
            page = FooterPage(driver)
            page.click_selectel_link()
            page.switch_to_new_window()
            text_on_opened_tab = page.get_element_text_on_opened_selectel_tab()
            assert text_on_opened_tab == FooterData.footer_related_elements_text["selectel_start_page_text"], \
                "The SELECTEL link in Footer leads to an incorrect page after click " \
                "or opened page does not load correctly"

        @allure.title("Verify that the Contact us link in Footer calls an email client")
        def test_fp_03_06_verify_contact_us_link_calls_an_email_client(self, driver, main_page_open):
            page = FooterPage(driver)
            page.click_contact_us_link()
            assert True, "the Contact us link in Footer does not call an email client"

    class TestFooterImages:
        @allure.title("Verify presence, visibility and accuracy of the ARASAAC link's image in Footer")
        def test_fp_04_01_verify_arasaac_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_image_presence = page.check_arasaac_image_presence()
            link_image_visibility = page.check_arasaac_image_visibility()
            link_image_src = page.get_arasaac_image_src()
            link_image_alt = page.get_arasaac_image_alt()
            assert link_image_presence is not None, "The image in the ARASAAC link is absent"
            assert link_image_visibility, "The ARASAAC link image is invisible"
            assert link_image_src, "The 'src' attribute value of the ARASAAC link's image is empty"
            assert link_image_src == FooterData.footer_images_src["arasaac_img_src"], \
                "The 'src' attribute value of the ARASAAC link image is unaccurate"
            assert link_image_alt, "The 'alt' attribute value of the ARASAAC link image is empty"
            assert link_image_alt == FooterData.footer_images_alt["arasaac_img_alt"], \
                "The ARASAAC link image is unaccurate"
