"""Auto tests for verifying web elements in the Header of the site"""
import allure
from pages.header_page import HeaderPage
from test_data.header_data import HeaderData


@allure.epic("Test Header")
class TestHeaderPage:
    class TestUnauthorizedHeaderPage:
        class TestHeaderPageStructure:
            @allure.title("Verify presence and visibility of the Header")
            def test_hp_01_01_verify_header_presence_and_visibility(self, driver, main_page_open):
                page = HeaderPage(driver)
                page_content_presence = page.check_header_presence()
                page_content_visibility = page.check_header_visibility()
                assert page_content_presence is not None, "The Header is absent in DOM"
                assert page_content_visibility, "The Header is invisible"

            @allure.title("Verify composition, visibility of elements on the 1st-6th levels of nesting in the Header")
            def test_hp_01_02_verify_header_structure_and_visibility(self, driver, main_page_open):
                page = HeaderPage(driver)
                structure_of_1st_level = page.get_structure_of_1st_level()
                visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level_on_page()
                structure_of_2nd_level = page.get_structure_of_2nd_level()
                visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_on_page()
                structure_of_3rd_level = page.get_structure_of_3rd_level()
                visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level_on_page()
                structure_of_4th_level = page.get_structure_of_4th_level()
                visibility_of_elements_on_4th_level = page.check_elements_visibility_on_4th_level_on_page()
                structure_of_5th_level = page.get_structure_of_5th_level()
                visibility_of_elements_on_5th_level = page.check_elements_visibility_on_5th_level_on_page()
                structure_of_6th_level = page.get_structure_of_6th_level()
                invisibility_of_elements_on_6th_level = page.check_elements_invisibility_on_6th_level_on_page()
                assert structure_of_1st_level, "The Header is empty"
                assert visibility_of_elements_on_1st_level, "1th-level elements are invisible"
                assert structure_of_2nd_level, "Elements on the 2nd level are absent on the page"
                assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
                assert structure_of_3rd_level, "Elements on the 3rd level are absent on the page"
                assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible"
                assert structure_of_4th_level, "Elements on the 4th level are absent on the page"
                assert visibility_of_elements_on_4th_level, "4th-level elements are invisible"
                assert structure_of_5th_level, "Elements on the 5th level are absent on the page"
                assert visibility_of_elements_on_5th_level, "5th-level elements are invisible"
                assert structure_of_6th_level, "Elements on the 6th level are absent on the page"
                assert invisibility_of_elements_on_6th_level, "6th-level elements are visible"

            @allure.title("Verify presence, visibility of links, buttons in the Header")
            def test_hp_01_03_verify_header_structural_elements(self, driver, main_page_open):
                page = HeaderPage(driver)
                header_links = page.get_list_of_links()
                header_direct_links = page.get_list_of_direct_links()
                header_direct_links_visibility = page.check_direct_links_visibility()
                links_in_more_presence = page.get_list_of_links_in_more()
                links_in_more_invisibility = page.check_links_invisibility_in_more()
                links_in_more_visibility = page.check_links_visibility_in_more()
                logo_link_presence = page.check_logo_link_presence()
                logo_link_visibility = page.check_logo_link_visibility()
                registration_link_presence = page.check_registration_link_presence()
                registration_link_visibility = page.check_registration_link_visibility()
                buttons_presence = page.get_list_of_buttons()
                buttons_visibility = page.check_buttons_visibility()
                ru_en_buttons_presence = page.get_list_of_ru_en_buttons()
                ru_en_buttons_visibility = page.check_ru_en_buttons_visibility()
                more_button_presence = page.check_more_button_presence()
                more_button_visibility = page.check_more_button_visibility()
                assert header_links, "Links are absent in the Header"
                assert header_direct_links, "Direct links are absent in the Header"
                assert header_direct_links_visibility, "Direct links are invisible"
                assert links_in_more_presence, "Links in the dropdown 'More' are absent on the page"
                assert links_in_more_invisibility, "Links in the dropdown 'More' are visible"
                assert links_in_more_visibility, "Links in the dropdown 'More' are invisible"
                assert logo_link_presence, "The 'Logo' link is absent on the page"
                assert logo_link_visibility, "The 'Logo' link is invisible"
                assert registration_link_presence, "The 'Registration' link is absent on the page"
                assert registration_link_visibility, "The 'Registration' link is invisible"
                assert buttons_presence, "Buttons are absent on the page"
                assert buttons_visibility, "Buttons are invisible"
                assert ru_en_buttons_presence, "The 'ru' and 'en' buttons are absent on the page"
                assert ru_en_buttons_visibility, "The 'ru' and 'en' buttons are invisible"
                assert more_button_presence, "The 'More' button is absent on the page"
                assert more_button_visibility, "The 'More' button is invisible"

        class TestHeaderPageText:
            @allure.title("Verify values of the text in links, buttons in the Header")
            def test_hp_02_01_verify_text_in_links_and_buttons(self, driver, main_page_open):
                page = HeaderPage(driver)
                direct_links_text = page.get_text_in_direct_links()
                links_in_more_text = page.get_text_of_links_in_more()
                buttons_text = page.get_text_in_buttons()
                ru_en_buttons_text = page.get_text_in_ru_en_buttons()
                assert all(link_text in HeaderData.links_text for link_text in direct_links_text), \
                    "Text in links in section 2 mismatches valid values"
                assert all(link_text in HeaderData.links_text for link_text in links_in_more_text), \
                    "Text in links in section 3 mismatches valid values"
                assert all(button_text in HeaderData.buttons_text for button_text in buttons_text), \
                    "Text in buttons mismatches valid values"
                assert all(button_text in HeaderData.ru_en_buttons_text for button_text in ru_en_buttons_text), \
                    "Text in 'ru-en' buttons mismatches valid values"

        class TestHeaderPageLinks:
            @allure.title("Verify clickability, href, status code of links in the Header")
            def test_hp_03_01_verify_header_links(self, driver, main_page_open):
                page = HeaderPage(driver)
                links_clickability = page.check_links_clickability()
                links_href = page.get_links_href()
                link_status_codes = page.get_links_status_codes()
                assert links_clickability, "Links are unclickable"
                assert links_href, "Links href are empty"
                assert all(link_href in HeaderData.links_href for link_href in links_href), \
                    "Attributes 'href' of links mismatch valid values"
                assert all(status_code == HeaderData.link_status_codes for status_code in link_status_codes), \
                    "Status codes of links mismatch valid values"

            @allure.title("Verify if internal links in the Header lead to correct pages after click")
            def test_hp_03_02_verify_internal_links_lead_to_correct_pages(self, driver, main_page_open):
                page = HeaderPage(driver)
                internal_links_in_more = page.get_list_of_internal_links_in_more()
                opened_pages = page.click_on_internal_links_in_header()
                assert internal_links_in_more, "Internal links are not collected in the list"
                assert all(page in HeaderData.pages_urls for page in opened_pages), \
                    "Some of internal links lead to incorrect pages after clicking"

            @allure.title("Verify if external links in the Header lead to correct pages after click")
            def test_hp_03_03_verify_external_links_lead_to_correct_pages(self, driver, main_page_open):
                page = HeaderPage(driver)
                external_links_in_more = page.get_list_of_external_links_in_more()
                opened_pages = page.click_on_external_links_in_header()
                assert external_links_in_more, "External links are not collected in the list"
                assert all(page in HeaderData.pages_urls for page in opened_pages), \
                    "Some of external links lead to incorrect pages after clicking"

            @allure.title("""Verify that the 'Logo' link on the Start Unauthorized Page 
                             doesn't refresh the current page or lead to other pages after clicking""")
            def test_hp_03_04_verify_clicking_on_logo_link_on_start_unauthorized_page(self, driver, main_page_open):
                page = HeaderPage(driver)
                handles_before = driver.window_handles
                initial_page_source = page.driver.page_source
                initial_page_url = page.driver.current_url
                current_page_url = page.click_on_logo_link()
                handles_after = driver.window_handles
                current_page_source = page.driver.page_source
                assert len(handles_before) == len(handles_after), "The number of open tabs changed after clicking"
                assert initial_page_source == current_page_source, \
                    "'Logo' link in the sections 1 refreshes the page after clicking"
                assert initial_page_url == current_page_url, \
                    "'Logo' link in the sections 1 leads to some page after clicking"

            @allure.title("Verify the dropdown opens/closes after clicking on the 'More' button in the Header")
            def test_hp_03_05_verify_more_button_click(self, driver, main_page_open):
                page = HeaderPage(driver)
                button_click = page.check_dropdown_opens_and_closes()
                assert button_click, "The dropdown isn't open/closed after clicking the 'More' button"

            @allure.title("Verify switching of the 'ru' and 'en' buttons in the Header")
            def test_hp_03_06_verify_ru_en_buttons_switching(self, driver, main_page_open):
                page = HeaderPage(driver)
                text_ru = page.check_language_change_ru()
                text_en = page.check_language_change_en()
                assert text_ru == HeaderData.title_text_ru, "RU language isn't enabled after clicking the 'ru' button"
                assert text_en == HeaderData.title_text_en, "EN language isn't enabled after clicking the 'en' button"

        class TestHeaderPageImages:
            @allure.title("Verify presence, visibility and attributes of the image in the 'Logo' link")
            def test_hp_04_01_verify_logo_image(self, driver, main_page_open):
                page = HeaderPage(driver)
                logo_image_presence = page.check_logo_image_presence()
                logo_image_visibility = page.check_logo_image_visibility()
                image_xmlns = page.get_xmlns_of_logo_image()
                assert logo_image_presence, "An image in the 'Logo' link is absent on the page"
                assert logo_image_visibility, "The 'Logo' image is invisible"
                assert image_xmlns, "The 'xmlns' attribute value of the 'Logo' image is empty"
                assert image_xmlns == HeaderData.logo_image_xmlns, \
                    "The 'xmlns' attribute value of the 'Logo' image mismatches valid value"

            @allure.title("Verify size of the image in the 'Logo' link")
            def test_hp_04_02_verify_logo_image_size(self, driver, main_page_open):
                page = HeaderPage(driver)
                image_size = page.get_size_of_logo_image()
                image_size_change = page.check_size_changes_of_logo_image()
                assert image_size != 0, f"The image in the 'Logo' image has not size"
                assert image_size_change, "The 'Logo' image size is changed"
