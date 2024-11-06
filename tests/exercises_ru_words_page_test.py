"""Auto tests for verifying web elements on the 'Exercises "Words"' page on the 'ru' local"""
import allure
from pages.exercises_ru_words_page import ExercisesRuWordsPage


@allure.epic("The Exercises 'Words' Page on the 'ru' local")
class TestExercisesRuWordsPage:
    class TestExercisesRuWordsPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_erw_01_01_verify_page_presence_and_visibility(self, driver, exercises_ru_words_page_open):
            page = ExercisesRuWordsPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            assert page_content_presence is not None, "The page content is absent in DOM"
