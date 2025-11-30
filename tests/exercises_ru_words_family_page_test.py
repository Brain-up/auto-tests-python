"""Auto tests for verifying web elements on the exercises subgroup "Family" page
in the series "Words" on the "ru" local"""
import allure
from pages.exercises_ru_words_family_page import ExercisesRuWordsFamilyPage as erwfPage


@allure.epic("The exercises subgroup 'Family' page in the series 'Words' on the 'ru' local")
class TestExercisesRuWordsFamilyPage:
    class TestExRuWordsFamilyPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_erwf_01_01_verify_page_presence(self, driver, exercises_ru_words_family_page_open):
            page = erwfPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            assert page_content_presence, "The page content is absent in DOM"
