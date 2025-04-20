"""Auto tests for verifying web elements on the 'Used Resources' page"""
import allure
from pages.used_resources_page import UsedResourcesPage
from test_data.used_resources_page_data import UsedResourcesPageData as urPD


@allure.epic("Test Used Resources Page")
class TestUsedResourcesPage:

    class TestUsedResourcesPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_ur_01_01_verify_page_presence_and_visibility(self, driver, used_resources_page_open):
            page = UsedResourcesPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"

        @allure.title("""Verify the composition and visibility of elements 
        on the 1st-4th levels of nesting on the page""")
        def test_ur_01_02_verify_page_structure_and_visibility(self, driver, used_resources_page_open):
            page = UsedResourcesPage(driver)
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

    class TestUsedResourcesPageText:
        @allure.title("Verify value of the title of the tab")
        def test_ur_02_01_verify_tab_title(self, driver, used_resources_page_open):
            page = UsedResourcesPage(driver)
            tab_title_value = page.get_value_of_tab_title()
            assert tab_title_value, "The title value of the tab is empty"
            assert tab_title_value in urPD.tab_title_expected, "The title value of the tab mismatches the valid value"

        @allure.title("Verify value of title with tag 'h1' on the page")
        def test_ur_02_02_verify_page_title(self, driver, used_resources_page_open):
            page = UsedResourcesPage(driver)
            title_value = page.get_value_of_page_title()
            assert title_value, "The title value on the page is empty"
            assert title_value in urPD.page_title, "The title on the page mismatches the valid value"

        @allure.title("Verify content of the text on the page")
        def test_ur_02_03_verify_page_text(self, driver, used_resources_page_open):
            page = UsedResourcesPage(driver)
            text_content = page.get_text_content_on_page()
            assert text_content, "Text content on the page is empty"
            assert text_content in urPD.text_on_page, "Text content mismatches the valid value"

        @allure.title("Verify text in links in sections")
        def test_ur_02_04_verify_text_in_links(self, driver, used_resources_page_open):
            page = UsedResourcesPage(driver)
            links_text = page.get_text_in_links()
            assert links_text, "Text in links is empty"
            assert all(element in urPD.links_text for element in links_text), "Text in links mismatch valid values"

    class TestUsedResourcesPageLinks:
        @allure.title("""Verify presence, visibility, clickability, href, status code of links in sections""")
        def test_ur_03_01_verify_links_in_sections(self, driver, used_resources_page_open):
            page = UsedResourcesPage(driver)
            links_presence = page.get_list_of_links()
            links_visibility = page.check_links_visibility()
            links_clickability = page.check_links_clickability()
            links_href = page.get_links_href()
            link_status_codes = page.get_links_status_codes()
            assert links_presence, "Links are absent on the page"
            assert links_visibility, "Links are invisible"
            assert links_clickability, "Links are unclickable"
            assert links_href, "Links href are empty"
            assert all(element in urPD.links_href for element in links_href), \
                "Attributes 'href' of links mismatch valid values"
            assert all(element in urPD.link_status_codes for element in link_status_codes), \
                "Status codes of links mismatch valid values"

        @allure.title("Verify that links in the sections lead to the correct pages after clicking")
        def test_ur_03_02_verify_links_lead_to_the_correct_pages(self, driver, used_resources_page_open):
            page = UsedResourcesPage(driver)
            new_tabs_urls = page.click_on_links()
            assert all(element in urPD.pages_urls for element in new_tabs_urls), \
                "Links in the sections lead to incorrect pages after clicking"

    class TestUsedResourcesPageIcons:
        @allure.title("Verify presence, visibility and attributes of icons in sections")
        def test_ur_04_01_verify_icons_in_sections(self, driver, used_resources_page_open):
            page = UsedResourcesPage(driver)
            icons_presence = page.get_list_of_icons()
            icons_visibility = page.check_icons_visibility()
            icons_xmlns = page.get_icons_xmlns()
            assert icons_presence, "Icons in sections are absent"
            assert icons_visibility, "Icons in sections are invisible"
            assert icons_xmlns, "The 'xmlns' attribute value of icons in sections are empty"
            assert all(element == urPD.icons_xmlns for element in icons_xmlns), \
                "The 'xmlns' attribute value of some icons is empty or non-accurate"

        @allure.title("Verify sizes of icons in sections")
        def test_ur_04_02_verify_icons_sizes(self, driver, used_resources_page_open):
            page = UsedResourcesPage(driver)
            icons_size = page.get_icons_sizes()
            icons_size_changes = page.check_size_changes_of_icons()
            assert icons_size != 0, "Icons in sections haven't sizes"
            assert icons_size_changes, "Checks of changes of icons sizes have not carried out"
