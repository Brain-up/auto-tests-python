"""Data for verifying web elements on the 'Groups' page"""


class GroupsPageData:
    tab_title_ru = "Группы | BrainUp"
    tab_title_en = "Groups | BrainUp"

    page_title_ru = "Давайте выберем, какие упражнения будем делать сегодня?"
    page_title_en = "Let's choose what exercises we do today?"

    page_subtitles_ru = ["НЕРЕЧЕВЫЕ УПРАЖНЕНИЯ (СИГНАЛЫ ЕЩЁ В РАЗРАБОТКЕ)", "РЕЧЕВЫЕ УПРАЖНЕНИЯ (ГОТОВЫ ДЛЯ ЗАНЯТИЙ)"]
    page_subtitles_en = ["NON-SPEECH EXERCISES (NOT IMPLEMENTED YET)", "SPEECH EXERCISES"]

    link_titles_ru = ["Неречевые упражнения", "Речевые упражнения"]
    link_titles_en = ["Non-Speech", "Speech"]

    links_href = [
        "https://brainup.site/groups/1", "https://brainup.site/groups/2",
        "https://brainup.site/groups/3", "https://brainup.site/groups/4",
    ]
    link_href_first_part = "https://brainup.site/groups/"

    links_status_code = 200

    pages_urls = [
        "https://www.brainup.site/groups/1/series/18", "https://www.brainup.site/groups/2/series/1",
        "https://www.brainup.site/groups/3/series/14", "https://www.brainup.site/groups/4/series/10"
    ]

    images_src = [
        "https://brainup.site/pictures/exercise-type/speech-exercises.svg",
        "https://brainup.site/pictures/exercise-type/non-speech-exercises.svg"
    ]

    images_alt_ru = ["Неречевые упражнения (сигналы ещё в разработке)", "Речевые упражнения (готовы для занятий)"]
    images_alt_en = ["Non-Speech exercises (not implemented yet)", "Speech exercises"]
