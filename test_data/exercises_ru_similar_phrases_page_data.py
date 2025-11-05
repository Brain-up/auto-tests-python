"""Data for verifying web elements on the 'Exercises "Similar phrases"' page on the 'ru' local"""
from test_data.links import ExercisesUrls as ExUrls


class ExercisesRuSimilarPhrasesPageData:

    subgroup_links_text = ('Разной длительности', 'С частицей Не', 'Похожие',
                           'С разным окончанием', 'Из коротких слов', 'С разными предлогами')

    breadcrumbs_urls = (ExUrls.STARTING_POINT, f"{ExUrls.STARTING_POINT}/2",
                        ExUrls.URL_EXERCISES_RU_SIMILAR_PHRASES_PAGE)

    links_status_code = (200,)
