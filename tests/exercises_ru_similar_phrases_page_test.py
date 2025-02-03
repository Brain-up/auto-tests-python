"""Auto tests for verifying web elements on the 'Exercises "Similar phrases"' page on the 'ru' local"""
import allure
from pages.exercises_ru_similar_phrases_page import ExercisesRuSimilarPhrasesPage


@allure.epic("The Exercises 'Similar phrases' Page on the 'ru' local")
class TestExercisesRuSimilarPhrasesPage:
    class TestExercisesRuSimilarPhrasesPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_ersp_01_01_verify_page_presence_and_visibility(self, driver, exercises_ru_similar_phrases_page_open):
            page = ExercisesRuSimilarPhrasesPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"
