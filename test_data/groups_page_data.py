"""Data for verifying web elements on the 'Groups' page"""


class GroupsPageData:
    tab_title = ["Группы | BrainUp", "Groups | BrainUp"]

    page_title = ["Давайте выберем, какие упражнения будем делать сегодня?", "Let's choose what exercises we do today?"]

    page_subtitles = [
        "НЕРЕЧЕВЫЕ УПРАЖНЕНИЯ (СИГНАЛЫ ЕЩЁ В РАЗРАБОТКЕ)", "РЕЧЕВЫЕ УПРАЖНЕНИЯ (ГОТОВЫ ДЛЯ ЗАНЯТИЙ)",
        "NON-SPEECH EXERCISES (NOT IMPLEMENTED YET)", "SPEECH EXERCISES"
    ]

    links_href = [
        "https://brainup.site/groups/1", "https://brainup.site/groups/2",
        "https://brainup.site/groups/3", "https://brainup.site/groups/4",
    ]
    link_href_first_part = "https://brainup.site/groups/"

    links_status_code = 200

    pages_urls = [
        "https://brainup.site/groups/1/series/18", "https://brainup.site/groups/2/series/1",
        "https://brainup.site/groups/3/series/14", "https://brainup.site/groups/4/series/10"
    ]

    images_src = [
        "https://brainup.site/pictures/exercise-type/speech-exercises.svg",
        "https://brainup.site/pictures/exercise-type/non-speech-exercises.svg"
    ]

    images_alt_ru = [
        "Неречевые упражнения (сигналы ещё в разработке)", "Речевые упражнения (готовы для занятий)"
    ]

    images_alt_en = [
        "Non-Speech exercises (not implemented yet)", "Speech exercises"
    ]
