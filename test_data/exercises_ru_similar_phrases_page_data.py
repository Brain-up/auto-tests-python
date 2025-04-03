"""Data for verifying web elements on the 'Exercises "Similar phrases"' page on the 'ru' local"""
from test_data.links import MainPageLinks as Links


class ExercisesRuSimilarPhrasesPageData:
    tab_title_ru = "Речевые упражнения (готовы для занятий) | BrainUp"

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

    breadcrumbs_urls = (f"{Links.URL_GROUPS_PAGE}",
                        f"{Links.URL_GROUPS_PAGE}/2",
                        f"{Links.URL_GROUPS_PAGE}/2/series/2")

    links_status_code = (200,)
