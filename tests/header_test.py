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

            @allure.title("Verify the section with the 'ru' and 'en' buttons in the Header")
            def test_hp_01_03_verify_structure_and_visibility_of_ru_en_section(self, driver, main_page_open):
                page = HeaderPage(driver)
                ru_en_section_structure = page.get_structure_of_ru_en_section()
                ru_en_buttons_visibility = page.check_elements_visibility_in_ru_en_section()
                assert ru_en_section_structure, "The 'ru' and 'en' buttons are absent in DOM"
                assert ru_en_buttons_visibility, "The 'ru' and 'en' buttons are invisible in the Header"

        class TestHeaderPageSection1:

            @allure.title("""Verify presence, visibility, clickability, href, status code  
                             of the 'Logo' link in the section 1 in the Header""")
            def test_hp_02_01_verify_logo_link(self, driver, main_page_open):
                page = HeaderPage(driver)
                link_presence = page.check_logo_link_presence()
                link_visibility = page.check_logo_link_visibility()
                link_clickability = page.check_logo_link_clickability()
                link_href = page.get_logo_link_href()
                link_status_code = page.get_logo_link_status_code()
                assert link_presence, "The 'Logo' link is absent in DOM"
                assert link_visibility, "The 'Logo' link is invisible on the page"
                assert link_clickability, "The 'Logo' link is unclickable"
                assert link_href == HeaderData.links_href["logo_link_href"], \
                    f"The attribute 'href' of the {link_href} link does not match the valid value"
                assert link_status_code == HeaderData.links_status_code, \
                    f"The status code of the {link_href} does not match the valid value"

            @allure.title("""Verify that the 'Logo' link on the Start Unauthorized Page 
                             doesn't refresh the current page or lead to other pages after clicking""")
            def test_hp_02_02_verify_clicking_on_logo_link_on_start_unauthorized_page(self, driver, main_page_open):
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
            def test_hp_02_03_verify_clicking_on_logo_link_on_contacts_page(self, driver, contacts_page_open):
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
                assert current_page_url == HeaderData.links_href["logo_link_href"], \
                    "'Logo' link in sections 1 leads to incorrect page after clicking"

            @allure.title("Verify presence, visibility, attributes and sizes of the 'Logo' image")
            def test_hp_02_04_verify_logo_image(self, driver, main_page_open):
                page = HeaderPage(driver)
                image_presence = page.check_logo_image_presence()
                image_visibility = page.check_logo_image_visibility()
                image_xmlns = page.get_xmlns_of_logo_image()
                image_sizes = page.get_sizes_of_logo_image()
                image_sizes_change = page.check_size_changes_of_logo_section()
                assert image_presence, "Image in the 'Logo' link is absent"
                assert image_visibility, "The 'Logo' image is invisible"
                assert image_xmlns, "The 'xmlns' attribute value of the 'Logo' image is empty"
                assert image_xmlns == HeaderData.logo_image_xmlns, \
                    "The 'xmlns' attribute value of the 'Logo' image is unaccurate"
                assert image_sizes != 0, f"The 'Logo' image is invisible due its size = 0, 0"
                assert image_sizes_change, "Checks of changes in image sizes have not carried out"

        class TestHeaderPageSection2:

            @allure.title("Verify presence, visibility, clickability, href, status code "
                          "of the 'About' and the 'Telegram' links in the Section 2 in the Header")
            def test_hp_03_01_verify_links_in_section_2(self, driver, main_page_open):
                page = HeaderPage(driver)
                links_presence = page.get_list_of_links_in_section_2()
                links_visibility = page.check_links_visibility_in_section_2()
                links_clickability = page.check_links_clickability_in_section_2()
                links_href = page.get_links_href_in_section_2()
                links_status_code = page.get_links_status_code_in_section_2()
                assert links_presence, "Links are absent in DOM"
                assert links_visibility, "Links are invisible in the page"
                assert links_clickability, "Links are unclickable"
                assert links_href, "Links href are empty"
                assert links_href == HeaderData.links_href["section 2 links href"], \
                    "The attribute 'href' of the links do not match the valid values"
                assert all(link_status_code ==
                           HeaderData.links_status_code for link_status_code in links_status_code), \
                    "The status code of the links do not match the valid value"

            @allure.title("""Verify if the 'About' and the 'Telegram' links in the Section 2 
                          lead to the correct pages after click""")
            def test_hp_03_02_verify_links_lead_to_the_correct_pages(self, driver, main_page_open):
                page = HeaderPage(driver)
                opened_pages = page.click_on_links_and_return_back()
                assert opened_pages == HeaderData.pages_url_for_navigation_by_links_in_section_2, \
                    "The 'About' and the 'Telegram' links in the Sections 2 lead to incorrect pages after click"

            @allure.title("""Verify values of the text in the 'About' and the 'Telegram' links 
                          in the Section 2 in the Header""")
            def test_hp_03_03_verify_text_in_links(self, driver, main_page_open):
                page = HeaderPage(driver)
                links_text = page.get_text_in_links_in_section_2()
                assert links_text in HeaderData.links_text, "Text in links do not match the valid values"
