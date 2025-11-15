"""Data for verifying web elements on the 'Exercises "Words"' page on the 'ru' local"""
from test_data.links import ExercisesUrls as ExUrls


class ExercisesRuWordsPageData:
    # tab_title = ("Речевые упражнения (готовы для занятий) | BrainUp", "Speech exercises | BrainUp")

    breadcrumbs_urls = (ExUrls.STARTING_POINT, f"{ExUrls.STARTING_POINT}/2", ExUrls.URL_EXERCISES_RU_WORDS_PAGE)
