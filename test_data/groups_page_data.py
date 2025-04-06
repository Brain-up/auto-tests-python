"""Data for verifying web elements on the 'Groups' page"""
from test_data.links import MainPageLinks as Links


class GroupsPageData:
    tab_title_ru = "Группы | BrainUp"
    tab_title_en = "Groups | BrainUp"

    page_title_ru = "Давайте выберем, какие упражнения будем делать сегодня?"
    page_title_en = "Let's choose what exercises we do today?"

    page_subtitles_ru = ("НЕРЕЧЕВЫЕ УПРАЖНЕНИЯ (СИГНАЛЫ ЕЩЁ В РАЗРАБОТКЕ)", "РЕЧЕВЫЕ УПРАЖНЕНИЯ (ГОТОВЫ ДЛЯ ЗАНЯТИЙ)")
    page_subtitles_en = ("NON-SPEECH EXERCISES (NOT IMPLEMENTED YET)", "SPEECH EXERCISES")

    link_titles_ru = ("Неречевые упражнения", "Речевые упражнения")
    link_titles_en = ("Non-Speech", "Speech")

    links_href = (f"{Links.URL_MAIN_PAGE}groups/1", f"{Links.URL_MAIN_PAGE}groups/2",
                  f"{Links.URL_MAIN_PAGE}groups/3", f"{Links.URL_MAIN_PAGE}groups/4")
    link_href_first_part = f"{Links.URL_MAIN_PAGE}groups/"

    links_status_code = (200,)

    pages_urls = (f"{Links.URL_MAIN_PAGE}groups/1/series/18", f"{Links.URL_MAIN_PAGE}groups/2/series/1",
                  f"{Links.URL_MAIN_PAGE}groups/3/series/14", f"{Links.URL_MAIN_PAGE}groups/4/series/10")

    images_src = (f"{Links.URL_MAIN_PAGE}pictures/exercise-type/speech-exercises.svg",
                  f"{Links.URL_MAIN_PAGE}pictures/exercise-type/non-speech-exercises.svg")

    images_alt_ru = ("Неречевые упражнения (сигналы ещё в разработке)", "Речевые упражнения (готовы для занятий)")
    images_alt_en = ("Non-Speech exercises (not implemented yet)", "Speech exercises")
