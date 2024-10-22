"""Auto tests for verifying web elements on the 'Groups' page"""
import allure
from pages.groups_page import GroupsPage
from test_data.groups_page_data import GroupsPageData


# @pytest.mark.skip(reason="unsupported preconditions")
@allure.epic("The Groups Page")
class TestGroupsPage:
    class TestGroupsPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_gp_01_01_verify_page_presence_and_visibility(self, driver, auto_test_user_authorized):
            page = GroupsPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence is not None, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"

        @allure.title("Verify composition, visibility of elements on the 1st-6th levels of nesting on the page")
        def test_gp_01_02_verify_page_structure_and_visibility(self, driver, auto_test_user_authorized):
            page = GroupsPage(driver)
            structure_of_1st_level = page.get_structure_of_1st_level()
            visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level()
            structure_of_2nd_level = page.get_structure_of_2nd_level()
            visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level()
            structure_of_3rd_level = page.get_structure_of_3rd_level()
            visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level()
            structure_of_4th_level = page.get_structure_of_4th_level()
            visibility_of_elements_on_4th_level = page.check_elements_visibility_on_4th_level()
            structure_of_5th_level = page.get_structure_of_5th_level()
            visibility_of_elements_on_5th_level = page.check_elements_visibility_on_5th_level()
            structure_of_6th_level = page.get_structure_of_6th_level()
            visibility_of_elements_on_6th_level = page.check_elements_visibility_on_6th_level()
            assert structure_of_1st_level, "The page is empty"
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
            assert visibility_of_elements_on_6th_level, "6th-level elements are invisible"

        @allure.title("Verify presence, visibility of the title, tiles, links, images, subtitles on the page")
        def test_gp_01_03_verify_page_structural_elements(self, driver, auto_test_user_authorized):
            page = GroupsPage(driver)
            title_on_2nd_level = page.check_title_presence()
            title_visibility = page.check_title_visibility()
            tiles_on_2nd_level = page.get_list_of_tiles()
            tiles_visibility = page.check_visibility_of_tiles()
            links_on_3rd_level = page.get_list_of_links()
            links_visibility = page.check_visibility_of_links()
            images_on_6th_level = page.get_list_of_images()
            images_visibility = page.check_visibility_of_images()
            subtitles_on_6th_level = page.get_list_of_subtitles()
            subtitles_visibility = page.check_visibility_of_subtitles()
            assert title_on_2nd_level, "The title on the 2nd level is absent on the page"
            assert title_visibility, "The title on the 2nd level is invisible"
            assert tiles_on_2nd_level, "Tiles on the 2nd level are absent on the page"
            assert tiles_visibility, "Tiles on the 2nd level are invisible"
            assert links_on_3rd_level, "Links on the 3rd level are absent on the page"
            assert links_visibility, "Links on the 3rd level are invisible"
            assert images_on_6th_level, "Images on the 6th level are absent on the page"
            assert images_visibility, "Images on the 6th level are invisible"
            assert subtitles_on_6th_level, "Subtitles on the 6th level are absent on the page"
            assert subtitles_visibility, "Subtitles on the 6th level are invisible"

    class TestGroupsPageText:
        @allure.title("Verify value of the title of the tab")
        def test_gp_02_01_verify_tab_title(self, driver, auto_test_user_authorized):
            page = GroupsPage(driver)
            tab_title_value = page.get_value_of_tab_title()
            assert tab_title_value, "The title value of the tab is empty"
            assert tab_title_value in GroupsPageData.tab_title, "The title on the tab doesn't match the valid value"

        @allure.title("Verify value of the title and subtitles on the page")
        def test_gp_02_02_verify_page_title_and_subtitles(self, driver, auto_test_user_authorized):
            page = GroupsPage(driver)
            title_value = page.get_value_of_page_title()
            subtitle_values = page.get_values_of_subtitles()
            assert title_value, "The title value on the page is empty"
            assert title_value in GroupsPageData.page_title, "The title on the page mismatches the valid value"
            assert subtitle_values, "Subtitle values on the page are empty"
            assert all(subtitle_value in GroupsPageData.page_subtitles for subtitle_value in subtitle_values), \
                "Subtitles mismatch any valid values"

    class TestGroupsPageLinks:
        @allure.title("Verify clickability, href, status code of links on the page")
        def test_gp_03_01_verify_links(self, driver, auto_test_user_authorized):
            page = GroupsPage(driver)
            links_clickability = page.check_links_clickability()
            links_href = page.get_links_href()
            link_status_codes = page.get_links_status_codes()
            assert links_clickability, "Links are unclickable"
            assert links_href, "Links href are empty"
            assert all(link_href.startswith(GroupsPageData.link_href_first_part) for link_href in links_href), \
                "Attributes 'href' of links mismatch valid values"
            assert all(element == GroupsPageData.links_status_code for element in link_status_codes), \
                "Status codes of links mismatch valid values"

        @allure.title("""Verify if links on the page lead to correct pages after clicking""")
        def test_gp_03_02_verify_links_lead_to_proper_pages(self, driver, auto_test_user_authorized):
            page = GroupsPage(driver)
            opened_pages = page.click_on_links()
            assert opened_pages, "Transitions to exercises pages have not performed"
            assert all(page in GroupsPageData.pages_urls for page in opened_pages), \
                "Some of links lead to incorrect pages after clicking"
