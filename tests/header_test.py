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

            @allure.title("Verify presence, visibility of links, buttons, images in the Header")
            def test_hp_01_03_verify_header_structural_elements(self, driver, main_page_open):
                page = HeaderPage(driver)
                header_links = page.get_list_of_links()
                logo_link_presence = page.check_logo_link_presence()
                logo_link_visibility = page.check_logo_link_visibility()
                links2_presence = page.get_list_of_links_in_section2()
                links2_visibility = page.check_links_visibility_in_section2()
                ru_en_section_structure = page.get_structure_of_ru_en_section()
                ru_en_buttons_visibility = page.check_elements_visibility_in_ru_en_section()
                logo_image_presence = page.check_logo_image_presence()
                logo_image_visibility = page.check_logo_image_visibility()
                assert header_links, "Links are absent in the Header"
                assert logo_link_presence, "The 'Logo' link is absent on the page"
                assert logo_link_visibility, "The 'Logo' link is invisible"
                assert links2_presence, "Links in section 2 are absent on the page"
                assert links2_visibility, "Links in section 2 are invisible"
                assert ru_en_section_structure, "The 'ru' and 'en' buttons are absent on the page"
                assert ru_en_buttons_visibility, "The 'ru' and 'en' buttons are invisible"
                assert logo_image_presence, "The image in the 'Logo' link is absent on the page"
                assert logo_image_visibility, "The 'Logo' image is invisible"

        class TestHeaderPageText:
            @allure.title("Verify values of the text in links, buttons in the Header")
            def test_hp_02_01_verify_text_in_links2(self, driver, main_page_open):
                page = HeaderPage(driver)
                links2_text = page.get_text_in_links2()
                ru_en_buttons_text = page.get_text_in_ru_en_buttons()
                assert links2_text in HeaderData.links_text, "Text in links 'About', 'Telegram' mismatches valid values"
                assert ru_en_buttons_text == HeaderData.buttons_text, "Text in 'ru-en' buttons mismatches valid values"

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

            @allure.title("""Verify that the 'Logo' link on the Start Unauthorized Page 
                             doesn't refresh the current page or lead to other pages after clicking""")
            def test_hp_03_02_verify_clicking_on_logo_link_on_start_unauthorized_page(self, driver, main_page_open):
                page = HeaderPage(driver)
                handles_before = driver.window_handles
                initial_page_source = page.driver.page_source
                initial_page_url = page.driver.current_url
                current_page_url = page.click_logo_link()
                handles_after = driver.window_handles
                current_page_source = page.driver.page_source
                assert len(handles_before) == len(handles_after), "The number of open tabs changed after clicking"
                assert initial_page_source == current_page_source, \
                    "'Logo' link in the sections 1 refreshes the page after clicking"
                assert initial_page_url == current_page_url, \
                    "'Logo' link in the sections 1 leads to some page after clicking"

            @allure.title("""Verify that the 'Logo' link on the 'Contacts' page leads an unauthorized user 
                             to the Start Unauthorized Page after clicking""")
            def test_hp_03_03_verify_clicking_on_logo_link_on_contacts_page(self, driver, contacts_page_open):
                page = HeaderPage(driver)
                handles_before = driver.window_handles
                initial_page_source = page.driver.page_source
                initial_page_url = page.driver.current_url
                current_page_url = page.click_logo_link()
                handles_after = driver.window_handles
                current_page_source = page.driver.page_source
                assert len(handles_before) == len(handles_after), "The number of open tabs changed after clicking"
                assert initial_page_source != current_page_source, \
                    "'Logo' link in the sections 1 leads an other page after clicking"
                assert initial_page_url != current_page_url, \
                    "'Logo' link in the sections 1 leads to some page after clicking"
                assert current_page_url in HeaderData.links_href, \
                    "'Logo' link in sections 1 leads to incorrect page after clicking"

            @allure.title("Verify if the 'About', 'Telegram' links in the Header lead to correct pages after click")
            def test_hp_03_04_verify_links2_lead_to_correct_pages(self, driver, main_page_open):
                page = HeaderPage(driver)
                opened_pages = page.click_on_links2_and_return_back()
                assert all(page in HeaderData.pages_url_for_navigation_by_links2 for page in opened_pages), \
                    "The 'About' and the 'Telegram' links in the Header lead to incorrect pages after click"

        class TestHeaderPageImages:
            @allure.title("Verify attributes of the image in the 'Logo' link")
            def test_hp_04_01_verify_verify_logo_image_attributes(self, driver, main_page_open):
                page = HeaderPage(driver)
                image_xmlns = page.get_xmlns_of_logo_image()
                image_sizes = page.get_sizes_of_logo_image()
                image_sizes_change = page.check_size_changes_of_logo_section()
                assert image_xmlns, "The 'xmlns' attribute value of the 'Logo' image is empty"
                assert image_xmlns == HeaderData.logo_image_xmlns, \
                    "The 'xmlns' attribute value of the 'Logo' image is unaccurate"
                assert image_sizes != 0, f"The 'Logo' image is invisible due its size = 0, 0"
                assert image_sizes_change, "Checks of changes in image sizes have not carried out"
