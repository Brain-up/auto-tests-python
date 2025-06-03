"""Auto tests for verifying web elements on the 'Groups' page"""
import allure
from pages.groups_page import GroupsPage as gPage
from test_data.groups_page_data import GroupsPageData as gPD


@allure.epic("The Groups Page")
class TestGroupsPage:
    class TestGroupsPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_gp_01_01_verify_page_presence_and_visibility(self, driver, groups_ru_page_open):
            page = gPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"

        @allure.title("Verify composition, visibility of elements on the 1st-6th levels of nesting on the page")
        def test_gp_01_02_verify_page_structure_and_visibility(self, driver, groups_ru_page_open):
            page = gPage(driver)
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
        def test_gp_01_03_verify_page_structural_elements(self, driver, groups_ru_page_open):
            page = gPage(driver)
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
        @allure.title("Verify value of the 'ru' title of the tab")
        def test_gp_02_01_verify_ru_tab_title(self, driver, groups_ru_page_open):
            page = gPage(driver)
            tab_title_value_ru = page.get_value_of_tab_title_ru()
            assert tab_title_value_ru, "The title value of the tab is empty on the 'ru' local"
            assert tab_title_value_ru == gPD.tab_title_ru, "The tab title mismatches the valid value on the 'ru' local"

        @allure.title("Verify value of the 'en' title of the tab")
        def test_gp_02_02_verify_en_tab_title(self, driver, groups_en_page_open):
            page = gPage(driver)
            tab_title_value_en = page.get_value_of_tab_title_en()
            assert tab_title_value_en, "The title value of the tab is empty on the 'en' local"
            assert tab_title_value_en == gPD.tab_title_en, "The tab title mismatches the valid value on the 'en' local"

        @allure.title("Verify value of the 'ru' title on the page")
        def test_gp_02_03_verify_ru_page_title(self, driver, groups_ru_page_open):
            page = gPage(driver)
            title_value_ru = page.get_value_of_page_title_ru()
            assert title_value_ru, "The title value on the page is empty on the 'ru' local"
            assert title_value_ru == gPD.page_title_ru, "The page title mismatches the valid value on the 'ru' local"

        @allure.title("Verify value of the 'en' title on the page")
        def test_gp_02_04_verify_en_page_title(self, driver, groups_en_page_open):
            page = gPage(driver)
            title_value_en = page.get_value_of_page_title_en()
            assert title_value_en, "The title value on the page is empty on the 'en' local"
            assert title_value_en == gPD.page_title_en, "The page title mismatches the valid value on the 'en' local"

        @allure.title("Verify value of the 'ru' subtitles on the page")
        def test_gp_02_05_verify_ru_page_subtitles(self, driver, groups_ru_page_open):
            page = gPage(driver)
            subtitle_values_ru = page.get_values_of_subtitles_ru()
            assert subtitle_values_ru, "Subtitle values are empty on the 'ru' local"
            assert all(element in gPD.page_subtitles_ru for element in subtitle_values_ru), \
                "Subtitles mismatch any valid values on the 'ru' local"

        @allure.title("Verify value of the 'en' subtitles on the page")
        def test_gp_02_06_verify_en_page_subtitles(self, driver, groups_en_page_open):
            page = gPage(driver)
            subtitle_values_en = page.get_values_of_subtitles_en()
            assert subtitle_values_en, "Subtitle values are empty on the 'en' local"
            assert all(element in gPD.page_subtitles_en for element in subtitle_values_en), \
                "Subtitles mismatch any valid values on the 'en' local"

    class TestGroupsPageLinks:
        @allure.title("Verify clickability, status code of links on the page")
        def test_gp_03_01_verify_links(self, driver, groups_ru_page_open):
            page = gPage(driver)
            links_clickability = page.check_links_clickability()
            link_status_codes = page.get_links_status_codes()
            assert links_clickability, "Links are unclickable"
            assert all(element in gPD.links_status_code for element in link_status_codes), \
                "Status codes of links mismatch valid values"

        @allure.title("Verify title of links on the 'ru' local")
        def test_gp_03_02_01_verify_links_ru_title(self, driver, groups_ru_page_open):
            page = gPage(driver)
            link_titles_ru = page.get_links_titles_ru()
            print("Found alt attributes:", link_titles_ru)  # temporarily for debugging
            print("Expected alt attributes:", gPD.link_titles_ru)
            assert link_titles_ru, "Link titles values are empty on the 'ru' local"
            assert all(element in gPD.link_titles_ru for element in link_titles_ru), \
                "Link titles mismatch any valid values on the 'ru' local"

        @allure.title("Verify href of links on the 'ru' local")
        def test_gp_03_02_02_verify_links_ru_href(self, driver, groups_ru_page_open):
            page = gPage(driver)
            links_href_ru = page.get_links_href_ru()
            assert links_href_ru, "Links href are empty on the 'ru' local"
            assert all(element.startswith(gPD.link_href_first_part) for element in links_href_ru), \
                "Attributes 'href' of links on the 'ru' local mismatch valid values"

        @allure.title("Verify title, href of links on the 'en' local")
        def test_gp_03_03_verify_links_en(self, driver, groups_en_page_open):
            page = gPage(driver)
            link_titles_en = page.get_links_titles_en()
            links_href_en = page.get_links_href_en()
            assert link_titles_en, "Link titles values are empty on the 'en' local"
            assert all(element in gPD.link_titles_en for element in link_titles_en), \
                "Link titles mismatch any valid values on the 'en' local"
            assert links_href_en, "Links href are empty on the 'en' local"
            assert all(element.startswith(gPD.link_href_first_part) for element in links_href_en), \
                "Attributes 'href' of links on the 'en' local mismatch valid values"

        @allure.title("""Verify if links on the 'ru' local lead to correct pages after clicking""")
        def test_gp_03_04_verify_ru_links_lead_to_proper_pages(self, driver, groups_ru_page_open):
            page = gPage(driver)
            opened_pages = page.click_on_links_on_ru_local()
            assert opened_pages, "Transitions to exercises pages have not performed"
            assert all(element in gPD.pages_urls for element in opened_pages), \
                "Some links lead to incorrect pages after clicking"

        @allure.title("""Verify if links on the 'en' local lead to correct pages after clicking""")
        def test_gp_03_05_verify_en_links_lead_to_proper_pages(self, driver, groups_en_page_open):
            page = gPage(driver)
            opened_pages = page.click_on_links_on_en_local()
            assert opened_pages, "Transitions to exercises pages have not performed"
            assert all(element in gPD.pages_urls for element in opened_pages), \
                "Some links lead to incorrect pages after clicking"

    class TestGroupsPageImages:
        @allure.title("Verify attribute 'src' of images in links on the page")
        def test_gp_04_01_verify_images_src(self, driver, groups_ru_page_open):
            page = gPage(driver)
            images_src = page.get_images_src()
            assert images_src, "The 'src' attribute value of images is empty"
            assert all(element in gPD.images_src for element in images_src), \
                "The 'src' attribute of some images mismatches valid values"

        @allure.title("Verify attribute 'alt' of images in links on the 'ru' local")
        def test_gp_04_02_verify_images_alt_ru(self, driver, groups_ru_page_open):
            page = gPage(driver)
            images_alt_ru = page.get_images_alt_ru()
            print("Found alt attributes:", images_alt_ru)  # temporarily for debugging
            print("Expected alt attributes:", gPD.images_alt_ru)
            assert images_alt_ru, "The 'alt' attribute value of some images is empty on the 'ru' local"
            assert all(element in gPD.images_alt_ru for element in images_alt_ru), \
                "The 'alt' attribute value of some images is empty or mismatches valid values on the 'ru' local"

        def test_gp_04_03_verify_images_alt_en(self, driver, groups_en_page_open):
            page = gPage(driver)
            images_alt_en = page.get_images_alt_en()
            assert images_alt_en, "The 'alt' attribute value of some images is empty on the 'en' local"
            assert all(element in gPD.images_alt_en for element in images_alt_en), \
                "The 'alt' attribute value of some images is empty or mismatches valid values on the 'en' local"

        @allure.title("Verify sizes of images in links on the page")
        def test_gp_04_04_verify_images_sizes(self, driver, groups_ru_page_open):
            page = gPage(driver)
            images_size = page.get_images_sizes()
            images_size_changed = page.check_size_changes_of_images()
            assert images_size != 0, "Images in links have not sizes"
            assert len(images_size_changed) == len(gPD.images_src), "Not all images in links have changed sizes"
