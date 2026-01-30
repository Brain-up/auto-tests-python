"""Auto tests for verifying web elements on the exercises subgroup "Family" page
in the series "Words" on the "ru" local"""
import allure
from pages.exercises_ru_words_family_page import ExercisesRuWordsFamilyPage as erwfPage


@allure.epic("The exercises subgroup 'Family' page in the series 'Words' on the 'ru' local")
class TestExercisesRuWordsFamilyPage:
    class TestExRuWordsFamilyPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_erwf_01_01_verify_page_presence_and_visibility(self, driver, exercises_ru_words_family_page_open):
            page = erwfPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"

        @allure.title("Verify composition, visibility of elements on the 1st-13th levels of nesting on the page")
        def test_erwf_01_02_verify_page_structure_and_visibility(self, driver, exercises_ru_words_family_page_open):
            page = erwfPage(driver)
            structure_of_1st_level = page.get_structure_of_1st_level()
            visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level()
            structure_of_2nd_level = page.get_structure_of_2nd_level()
            visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level()
            structure_of_3rd_level = page.get_structure_of_3rd_level()
            visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level()
            structure_of_4th_level = page.get_structure_of_4th_level()
            structure_of_5th_level = page.get_structure_of_5th_level()
            visibility_of_elements_on_5th_level = page.check_elements_visibility_on_5th_level()
            structure_of_6th_level = page.get_structure_of_6th_level()
            visibility_of_elements_on_6th_level = page.check_elements_visibility_on_6th_level()
            structure_of_7th_level = page.get_structure_of_7th_level()
            visibility_of_elements_on_7th_level = page.check_elements_visibility_on_7th_level()
            structure_of_8th_level = page.get_structure_of_8th_level()
            visibility_of_elements_on_8th_level = page.check_elements_visibility_on_8th_level()
            structure_of_9th_level = page.get_structure_of_9th_level()
            visibility_of_elements_on_9th_level = page.check_elements_visibility_on_9th_level()
            structure_of_10th_level = page.get_structure_of_10th_level()
            visibility_of_elements_on_10th_level = page.check_elements_visibility_on_10th_level()
            structure_of_11th_level = page.get_structure_of_11th_level()
            visibility_of_elements_on_11th_level = page.check_elements_visibility_on_11th_level()
            structure_of_12th_level = page.get_structure_of_12th_level()
            visibility_of_elements_on_12th_level = page.check_elements_visibility_on_12th_level()
            structure_of_13th_level = page.get_structure_of_13th_level()
            visibility_of_elements_on_13th_level = page.check_elements_visibility_on_13th_level()
            assert structure_of_1st_level, "The page is empty"
            assert visibility_of_elements_on_1st_level, "1th-level elements are invisible"
            assert structure_of_2nd_level, "Elements on the 2nd level are absent on the page"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
            assert structure_of_3rd_level, "Elements on the 3rd level are absent on the page"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible"
            assert structure_of_4th_level, "Elements on the 4th level are absent on the page"
            assert structure_of_5th_level, "Elements on the 5th level are absent on the page"
            assert visibility_of_elements_on_5th_level, "5th-level elements are invisible"
            assert structure_of_6th_level, "Elements on the 6th level are absent on the page"
            assert visibility_of_elements_on_6th_level, "6th-level elements are invisible"
            assert structure_of_7th_level, "Elements on the 7th level are absent on the page"
            assert visibility_of_elements_on_7th_level, "7th-level elements are invisible"
            assert structure_of_8th_level, "Elements on the 8th level are absent on the page"
            assert not visibility_of_elements_on_8th_level, "8th-level elements are visible"
            assert structure_of_9th_level, "Elements on the 9th level are absent on the page"
            assert not visibility_of_elements_on_9th_level, "9th-level elements are visible"
            assert structure_of_10th_level, "Elements on the 10th level are absent on the page"
            assert visibility_of_elements_on_10th_level, "10th-level elements are invisible"
            assert structure_of_11th_level, "Elements on the 11th level are absent on the page"
            assert visibility_of_elements_on_11th_level, "11th-level elements are invisible"
            assert structure_of_12th_level, "Elements on the 12th level are absent on the page"
            assert visibility_of_elements_on_12th_level, "12th-level elements are invisible"
            assert structure_of_13th_level, "Elements on the 13th level are absent on the page"
            assert visibility_of_elements_on_13th_level, "13th-level elements are invisible"
