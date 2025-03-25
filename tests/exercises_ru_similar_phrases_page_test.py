"""Auto tests for verifying web elements on the 'Exercises "Similar phrases"' page on the 'ru' local"""
import allure
from pages.exercises_ru_similar_phrases_page import ExercisesRuSimilarPhrasesPage
from test_data.exercises_ru_similar_phrases_page_data import ExercisesRuSimilarPhrasesPageData as ExRuSimPhrPaData


@allure.epic("The Exercises 'Similar phrases' Page on the 'ru' local")
class TestExercisesRuSimilarPhrasesPage:
    class TestExRuSimPhrPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_ersp_01_01_verify_page_presence_and_visibility(self, driver, exercises_ru_similar_phrases_page_open):
            page = ExercisesRuSimilarPhrasesPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"

        @allure.title("Verify composition, visibility of elements on the 1st-7th levels of nesting on the page")
        def test_ersp_01_02_verify_page_structure_and_visibility(self, driver, exercises_ru_similar_phrases_page_open):
            page = ExercisesRuSimilarPhrasesPage(driver)
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
        def test_ersp_01_03_verify_page_structural_elements(self, driver, exercises_ru_similar_phrases_page_open):
            page = ExercisesRuSimilarPhrasesPage(driver)
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

    class TestExRuSimPhrPageText:
        @allure.title("Verify value of the title of the tab")
        def test_ersp_02_01_verify_tab_title(self, driver, exercises_ru_similar_phrases_page_open):
            page = ExercisesRuSimilarPhrasesPage(driver)
            tab_title_value = page.get_value_of_tab_title()
            assert tab_title_value, "The title value of the tab is empty"
            assert tab_title_value == ExRuSimPhrPaData.tab_title_ru, "The tab title doesn't match the valid value"

        @allure.title("Verify value of the breadcrumbs on the page")
        def test_ersp_02_02_verify_page_breadcrumbs_text(self, driver, exercises_ru_similar_phrases_page_open):
            page = ExercisesRuSimilarPhrasesPage(driver)
            breadcrumbs_text = page.get_value_of_breadcrumbs()
            assert breadcrumbs_text, "The breadcrumbs value on the page are empty"
            assert all(text in ExRuSimPhrPaData.breadcrumbs for text in breadcrumbs_text), \
                "Text in breadcrumbs mismatches valid values"

        @allure.title("Verify text in group links on the page")
        def test_ersp_02_03_verify_group_links_text(self, driver, exercises_ru_similar_phrases_page_open):
            page = ExercisesRuSimilarPhrasesPage(driver)
            links_text = page.get_group_links_text()
            assert links_text, "Text in group links is absent"
            assert all(text in ExRuSimPhrPaData.group_links_text for text in links_text), \
                "Text in group links mismatches valid values"

        @allure.title("Verify text in cards on the page")
        def test_ersp_02_04_verify_subgroup_links_text(self, driver, exercises_ru_similar_phrases_page_open):
            page = ExercisesRuSimilarPhrasesPage(driver)
            subgroup_links_text = page.get_subgroup_links_text()
            assert subgroup_links_text, "Text in cards is absent"
            assert all(text in ExRuSimPhrPaData.subgroup_links_text for text in subgroup_links_text), \
                "Text in subgroup links mismatches valid values"

    class TestExRuSimPhrPageLinks:
        @allure.title("Verify clickability, href of links in breadcrumbs on the page")
        def test_ersp_03_01_verify_breadcrumbs_links(self, driver, exercises_ru_similar_phrases_page_open):
            page = ExercisesRuSimilarPhrasesPage(driver)
            breadcrumbs_clickability = page.check_breadcrumbs_clickability()
            breadcrumbs_links_href = page.get_breadcrumbs_links_href()
            breadcrumbs_link_status_codes = page.get_link_status_codes_in_breadcrumbs()
            assert breadcrumbs_clickability, "Breadcrumbs are unclickable"
            assert all(href in ExRuSimPhrPaData.breadcrumbs_urls for href in breadcrumbs_links_href), \
                "Attributes 'href' of links in breadcrumbs mismatch valid values"
            assert all(element == ExRuSimPhrPaData.links_status_code for element in breadcrumbs_link_status_codes), \
                "Status codes of links in breadcrumbs mismatch valid values"
