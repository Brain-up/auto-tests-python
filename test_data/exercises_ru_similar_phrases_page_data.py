"""Data for verifying web elements on the 'Exercises "Similar phrases"' page on the 'ru' local"""
from test_data.links import ExercisesUrls as ExUrls


class ExercisesRuSimilarPhrasesPageData:
    tab_title_ru = ("Речевые упражнения (готовы для занятий) | BrainUp",)

    breadcrumbs_text = ('', 'Речевые упражнения (готовы для занятий)', 'Похожие фразы')

    group_links_text = ('СЛОВА', 'СЛОВА КОРОЛЁВОЙ', 'ПОХОЖИЕ ФРАЗЫ', 'ГРУППА СЛОВ', 'ПРЕДЛОЖЕНИЯ',
                        'ДИХОТИЧЕСКОЕ СЛУШАНИЕ', 'СЛОВА С ЧАСТОТНОЙ ГРУППИРОВКОЙ')

    group_link_titles = ('Распознавание слов',
                         'Слова по методическому пособию Инны Васильевны Королевой Учусь слушать и говорить',
                         'Распознавание похожих фраз', 'Распознавание последовательности слов',
                         'Распознавание предложений', 'Дихотическое слушание', 'Слова с частотной группировкой')

    group_link_active_links = ('Слова', 'Слова Королёвой', 'Похожие фразы', 'Группа слов', 'Предложения',
                               'Дихотическое слушание', 'Слова с частотной группировкой')

    subgroup_links_text = ('Разной длительности', 'С частицей Не', 'Похожие',
                           'С разным окончанием', 'Из коротких слов', 'С разными предлогами')

    breadcrumbs_urls = (ExUrls.STARTING_POINT, f"{ExUrls.STARTING_POINT}/2",
                        ExUrls.URL_EXERCISES_RU_SIMILAR_PHRASES_PAGE)

    # p = f"{ExUrls.STARTING_POINT}/2/series/"
    # group_link_urls = (f"{p}1", f"{p}2", f"{p}3", f"{p}4", f"{p}5", f"{p}6", f"{p}17")

    q = f"{ExUrls.URL_EXERCISES_RU_SIMILAR_PHRASES_PAGE}/subgroup/"
    subgroup_link_urls = (f"{q}60", f"{q}61", f"{q}62", f"{q}63", f"{q}64", f"{q}65")

    links_status_code = (200,)

    s = 'background-image: url("https://brnup.s3.eu-north-1.amazonaws.com/pictures/theme/'
    e = '.svg");'
    subgroup_links_style = (f"{s}longShortPhrases{e}", f"{s}noPhrases{e}", f"{s}similarPhrases{e}",
                            f"{s}differentEndPhrases{e}", f"{s}shortWords{e}", f"{s}prepositionPhrases{e}")
