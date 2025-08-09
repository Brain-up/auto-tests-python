"""Auto tests for verifying web elements on the 'Exercises "Words"' page on the 'ru' local"""
import allure
from pages.exercises_ru_words_page import ExercisesRuWordsPage as erwPage
from test_data.exercises_ru_words_page_data import ExercisesRuWordsPageData as erwPD


@allure.epic("The Exercises 'Words' Page on the 'ru' local")
class TestExercisesRuWordsPage:
    class TestExRuWordsPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_erw_01_01_verify_page_presence_and_visibility(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"

        @allure.title("Verify composition, visibility of elements on the 1st-6th levels of nesting on the page")
        def test_erw_01_02_verify_page_structure_and_visibility(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
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
            structure_of_7th_level = page.get_structure_of_7th_level()
            visibility_of_elements_on_7th_level = page.check_elements_visibility_on_7th_level()
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
            assert structure_of_7th_level, "Elements on the 7th level are absent on the page"
            assert visibility_of_elements_on_7th_level, "7th-level elements are invisible"

        @allure.title("Verify presence, visibility of lists on the page")
        def test_erw_01_03_verify_page_structural_elements(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            list1_on_5th_level = page.get_list1_of_breadcrumbs_links()
            list1_visibility = page.check_list1_visibility()
            list2_on_5th_level = page.get_list2_of_group_links()
            list2_visibility = page.check_list2_visibility()
            list3_on_5th_level = page.get_list3_of_subgroup_links()
            list3_visibility = page.check_list3_visibility()
            list4_on_6th_level = page.get_list4_of_links()
            list4_visibility = page.check_list4_visibility()
            assert list1_on_5th_level, "The list1 on the 5th level is absent on the page"
            assert list1_visibility, "The list1 on the 5th level is invisible"
            assert list2_on_5th_level, "The list2 on the 5th level is absent on the page"
            assert list2_visibility, "The list2 on the 5th level is invisible"
            assert list3_on_5th_level, "The list3 on the 5th level is absent on the page"
            assert list3_visibility, "The list3 on the 5th level is invisible"
            assert list4_on_6th_level, "The list4 on the 6th level is absent on the page"
            assert list4_visibility, "The list4 on the 6th level is invisible"

    class TestExRuWordsPageText:
        @allure.title("Verify value of the title of the tab")
        def test_erw_02_01_verify_tab_title(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            tab_title_value = page.get_value_of_tab_title()
            assert tab_title_value, "The title value of the tab is empty"
            assert tab_title_value in erwPD.tab_title_ru, "The title on the tab doesn't match the valid value"

        @allure.title("Verify value of the breadcrumbs on the page")
        def test_erw_02_02_verify_page_breadcrumbs_text(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            breadcrumbs_text = page.get_value_of_breadcrumbs()
            assert breadcrumbs_text, "The breadcrumbs value on the page are empty"
            assert all(element in erwPD.breadcrumbs_text for element in breadcrumbs_text), \
                "Text in breadcrumbs mismatches valid values"

        @allure.title("Verify text in group links on the page")
        def test_erw_02_03_verify_group_links_text(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            links_text = page.get_group_links_text()
            assert links_text, "Text in group links is absent"
            assert all(element in erwPD.group_links_text for element in links_text), \
                "Text in group links mismatches valid values"

        @allure.title("Verify text in cards on the page")
        def test_erw_02_04_verify_subgroup_links_text(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            subgroup_links_text = page.get_subgroup_links_text()
            assert subgroup_links_text, "Text in cards is absent"
            assert all(element in erwPD.subgroup_links_text for element in subgroup_links_text), \
                "Text in subgroup links mismatches valid values"

    class TestExRuWordsPageLinks:
        @allure.title("Verify clickability, href, status code of links in breadcrumbs on the page")
        def test_erw_03_01_verify_breadcrumbs_links(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            breadcrumbs_clickability = page.check_breadcrumbs_clickability()
            breadcrumbs_links_href = page.get_breadcrumbs_links_href()
            breadcrumbs_link_status_codes = page.get_link_status_codes_in_breadcrumbs()
            assert breadcrumbs_clickability, "Breadcrumbs are unclickable"
            assert all(element in erwPD.breadcrumbs_urls for element in breadcrumbs_links_href), \
                "Attributes 'href' of links in breadcrumbs mismatch valid values"
            assert all(element in erwPD.links_status_code for element in breadcrumbs_link_status_codes), \
                "Status codes of links in breadcrumbs mismatch valid values"

        @allure.title("Verify clickability, titles, attributes of group links on the page")
        def test_erw_03_02_verify_group_links(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            group_links_clickability = page.check_group_links_clickability()
            group_link_titles = page.get_group_link_titles()
            group_link_active_links = page.get_group_link_active_links()
            assert group_links_clickability, "Group links are unclickable"
            assert group_link_titles, "Group link titles values are empty"
            assert all(element in erwPD.group_link_titles for element in group_link_titles), \
                "Group link titles mismatch valid values"
            assert group_link_active_links, "Attributes 'active-link' of links in group links are empty"
            assert all(element in erwPD.group_link_active_links for element in group_link_active_links), \
                "Attributes 'active-link' of links in group links mismatch valid values"

        @allure.title("Verify clickability, titles, href, status code of subgroup links on the page")
        def test_erw_03_03_verify_subgroup_links(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            subgroup_links_clickability = page.check_subgroup_links_clickability()
            subgroup_link_titles = page.get_subgroup_link_titles()
            subgroup_links_href = page.get_subgroup_links_href()
            subgroup_links_status_codes = page.get_subgroup_link_status_codes()
            assert subgroup_links_clickability, "Subgroup links are unclickable"
            assert subgroup_link_titles, "Subgroup link titles values are empty"
            assert all(element in erwPD.subgroup_link_titles for element in subgroup_link_titles), \
                "Subgroup link titles mismatch valid values"
            assert all(element in erwPD.subgroup_link_urls for element in subgroup_links_href), \
                "Attributes 'href' of subgroup links mismatch valid values"
            assert all(element in erwPD.links_status_code for element in subgroup_links_status_codes), \
                "Status codes of subgroup links mismatch valid values"

        @allure.title("Verify if breadcrumbs links lead to correct pages after clicking")
        def test_erw_03_04_verify_breadcrumbs_links_navigation(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            opened_pages = page.click_on_breadcrumbs_links()
            assert opened_pages, "Transitions to pages have not performed"
            assert all(element in erwPD.breadcrumbs_urls for element in opened_pages), "Links lead to incorrect pages"

        @allure.title("Verify if group links lead to correct pages after clicking")
        def test_erw_03_05_verify_group_links_navigation(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            opened_pages = page.click_on_group_links()
            assert opened_pages, "Transitions to pages have not performed"
            assert all(element in erwPD.group_link_urls for element in opened_pages), "Links lead to incorrect pages"

        @allure.title("Verify if subgroup links 1-4 lead to correct pages after clicking")
        def test_erw_03_06_verify_subgroup_links_lead_to_correct_pages(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            opened_page1 = page.click_on_subgroup_link_family()
            opened_pages2_4 = page.click_on_subgroup_link_beloved_home_food_clothes()
            assert opened_page1, "Transition to the page has not performed"
            assert opened_page1 in erwPD.subgroup_link_urls, \
                "The first subgroup link leads to incorrect page after clicking"
            assert opened_pages2_4, "Transitions to pages have not performed"
            assert all(element in erwPD.subgroup_link_urls for element in opened_pages2_4), \
                "Some subgroup links lead to incorrect pages after clicking"

    class TestExRuWordsPageImages:
        @allure.title("Verify attributes of images in links on the page")
        def test_erw_04_01_verify_images_attributes(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            links_style = page.get_links_style()
            assert links_style, "The 'style' attribute value of links is empty"
            assert all(element in erwPD.subgroup_links_style for element in links_style), \
                "The 'style' attribute value of links mismatches valid values"

        @allure.title("Verify sizes of background-images in links on the page")
        def test_erw_04_02_verify_images_sizes(self, driver, exercises_ru_words_page_open):
            page = erwPage(driver)
            images_size = page.get_images_sizes()
            result = page.check_size_changes_of_images()
            assert images_size != 0, "Background-images have not sizes"
            assert len(result['changed']) > 0, "Images have not been resized"
            assert not result['lost'], f"Lost images: {result['lost']}"
