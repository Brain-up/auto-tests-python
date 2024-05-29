"""Auto tests for verifying web elements in the Header of the site"""
import allure
from pages.header_page import HeaderPage
from test_data.header_data import HeaderData


@allure.epic("Test Header")
class TestHeaderPage:
    class TestUnauthorizedHeaderPage:
        class TestHeaderPageStructure:

            @allure.title("Verify presence and visibility of content in the Header")
            def test_hp_01_01_verify_header_presence_and_visibility(self, driver, main_page_open):
                page = HeaderPage(driver)
                page_content_presence = page.check_presence_of_header_content()
                page_content_visibility = page.check_visibility_of_header_content()
                assert page_content_presence is not None, "The Header content is absent in DOM"
                assert page_content_visibility, "The Header content is invisible on the page"

            @allure.title("Verify the composition and visibility of elements on the 1-6th levels of the Header")
            def test_hp_01_02_verify_header_structure_and_visibility(self, driver, main_page_open):
                page = HeaderPage(driver)
                structure_of_header = page.get_structure_of_1st_level_in_header()
                visibility_of_elements_on_the_1st_level = page.check_elements_visibility_on_1st_level_in_header()
                structure_of_2nd_level = page.get_structure_of_2nd_level_in_header()
                visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_in_header()
                structure_of_3rd_level = page.get_structure_of_3rd_level_in_header()
                visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level_in_header()
                structure_of_4th_level = page.get_structure_of_4th_level_in_header()
                visibility_of_elements_on_4th_level = page.check_elements_visibility_on_4th_level_in_header()
                structure_of_5th_level = page.get_structure_of_5th_level_in_header()
                visibility_of_elements_on_5th_level = page.check_elements_visibility_on_5th_level_in_header()
                structure_of_6th_level = page.get_structure_of_6th_level_in_header()
                invisibility_of_elements_on_6th_level = page.check_elements_invisibility_on_6th_level_in_header()
                assert structure_of_header, "The Header is empty"
                assert visibility_of_elements_on_the_1st_level, "1th-level elements are invisible on the page"
                assert structure_of_2nd_level, "Elements on the 2nd level in the Header are absent"
                assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible on the page"
                assert structure_of_3rd_level, "Elements on the 3rd level in the Header are absent"
                assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible on the page"
                assert structure_of_4th_level, "Elements on the 4th level in the Header are absent"
                assert visibility_of_elements_on_4th_level, "4th-level elements are invisible on the page"
                assert structure_of_5th_level, "Elements on the 5th level in the Header are absent"
                assert visibility_of_elements_on_5th_level, "5th-level elements are invisible on the page"
                assert structure_of_6th_level, "Elements on the 6th level in the Header are absent"
                assert invisibility_of_elements_on_6th_level, "6th-level elements are visible on the page"

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
                assert link_status_code in HeaderData.links_status_codes, \
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
            def test_hp_02_03_verify_clicking_on_logo_link_on_start_unauthorized_page(self, driver, contacts_page_open):
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
