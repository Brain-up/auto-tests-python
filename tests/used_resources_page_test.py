"""Auto tests for verifying web elements on the 'Used Resources' page"""
import allure
from pages.used_resources_page import UsedResourcesPage
from test_data.used_resources_page_data import UsedResourcesPageData


@allure.epic("Test Used Resources Page")
class TestUsedResourcesPage:
    data = UsedResourcesPageData

    class TestUsedResourcesPageForAuthorizedUser:
        class TestUsedResourcesPageForAuthorizedUserStructure:

            @allure.title("Verify presence and visibility of content on the page")
            def test_ur_01_01_verify_page_presence_and_visibility(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                page_content_presence = page.check_presence_of_page_content()
                page_content_visibility = page.check_visibility_of_page_content()
                assert page_content_presence is not None, "The page content is absent in DOM"
                assert page_content_visibility, "The page content is invisible"

            @allure.title("""Verify the composition and visibility of elements 
            on the 1st-4th levels of nesting on the page""")
            def test_ur_01_02_verify_page_structure_and_visibility(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                structure_of_1st_level = page.get_structure_of_1st_level()
                visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level_on_page()
                structure_of_2nd_level = page.get_structure_of_2nd_level()
                visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_on_page()
                structure_of_3rd_level = page.get_structure_of_3rd_level()
                visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level_on_page()
                structure_of_4th_level = page.get_structure_of_4th_level()
                visibility_of_elements_on_4th_level = page.check_elements_visibility_on_4th_level_on_page()
                assert structure_of_1st_level, "The page is empty"
                assert visibility_of_elements_on_1st_level, "1st-level elements are invisible"
                assert structure_of_2nd_level, "Elements on the 2nd level are absent on the page"
                assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
                assert structure_of_3rd_level, "Elements on the 3rd level are absent on the page"
                assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible"
                assert structure_of_4th_level, "Elements on the 4th level are absent on the page"
                assert visibility_of_elements_on_4th_level, "4th-level elements are invisible"

        class TestUsedResourcesPageForAuthorizedText:
            @allure.title("Verify value of the title of the tab")
            def test_ur_02_01_verify_tab_title(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                tab_title_value = page.get_value_of_tab_title()
                assert tab_title_value, "The title value of the tab is empty"
                assert tab_title_value == UsedResourcesPageData.tab_title_current, \
                    "The title value of the tab doesn't match the valid value"

            @allure.title("Verify value of title with tag 'h1' on the page")
            def test_ur_02_02_verify_page_title(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                title_value = page.get_value_of_page_title()
                assert title_value, "The title value on the page is empty"
                assert title_value in UsedResourcesPageData.page_title, \
                    "The title on the page doesn't match the valid value"

            @allure.title("Verify content of the text on the page")
            def test_ur_02_03_verify_page_text(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                text_content = page.get_text_content_on_page()
                assert text_content, "The text content on the page is empty"
                assert text_content in UsedResourcesPageData.text_on_page, \
                    "The text content does not match the valid value"

            @allure.title("Verify text in links in the sections")
            def test_ur_02_04_verify_text_in_links(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                links_text = page.get_text_in_links()
                assert links_text, "Text in links is empty"
                assert all(link_text in UsedResourcesPageData.links_text for link_text in links_text), \
                    "Text in links does not match the valid values"

        class TestUsedResourcesPageForAuthorizedUserLinks:
            @allure.title("""Verify presence, visibility, clickability, href, status code of links in the sections""")
            def test_ur_03_01_verify_links_in_sections(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                links_presence = page.get_list_of_links()
                links_visibility = page.check_links_visibility()
                links_clickability = page.check_links_clickability()
                links_href = page.get_links_href()
                links_status_codes = page.get_links_status_codes()
                assert links_presence, "Links are absent on the page"
                assert links_visibility, "Links are invisible"
                assert links_clickability, "Links are unclickable"
                assert links_href, "Links href are empty"
                assert all(link_href in UsedResourcesPageData.links_href for link_href in links_href), \
                    "Attributes 'href' of links do not match the valid values"
                assert all(link_status_code in UsedResourcesPageData.links_status_codes
                           for link_status_code in links_status_codes), \
                    "Status codes of links do not match the valid values"

            @allure.title("Verify that links in the sections lead to the correct pages after clicking")
            def test_ur_03_02_verify_links_lead_to_the_correct_pages(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                new_tabs_urls = page.click_on_links()
                assert all(tab_url in UsedResourcesPageData.pages_urls for tab_url in new_tabs_urls), \
                    "Links in the sections lead to incorrect pages after clicking"

        class TestUsedResourcesPageForAuthorizedUserIcons:
            @allure.title("Verify presence, visibility and attributes of icons in the sections")
            def test_ur_04_01_verify_icons_in_sections(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                icons_presence = page.get_list_of_icons()
                icons_visibility = page.check_icons_visibility()
                icons_xmlns = page.get_icons_xmlns()
                assert icons_presence, "The icons in the sections are absent"
                assert icons_visibility, "The icons in the sections are invisible"
                assert icons_xmlns, "The 'xmlns' attribute value of the icons in the sections is empty"
                assert all(icon_xmlns == UsedResourcesPageData.icons_xmlns for icon_xmlns in icons_xmlns), \
                    "The 'xmlns' attribute value of some icons is empty or non-accurate"

            @allure.title("Verify sizes of icons in the sections")
            def test_ur_04_02_verify_icons_sizes(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                icons_size = page.get_icons_sizes()
                icons_size_changes = page.check_size_changes_of_icons()
                assert icons_size != 0, "The icons in the sections hasn't sizes"
                assert icons_size_changes, "Checks of changes of icons sizes have not carried out"
