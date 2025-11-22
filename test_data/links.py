class MainPageLinks:
    URL_MAIN_PAGE = "https://www.brainup.site/"
    # URL_MAIN_PAGE = "https://brainup.site/"
    # URL_MAIN_PAGE = "https://brainup.fun/"
    URL_CONTACTS_PAGE = f"{URL_MAIN_PAGE}contact"
    URL_CONTRIBUTORS_PAGE = f"{URL_MAIN_PAGE}contributors"
    URL_DESCRIPTION_PAGE = f"{URL_MAIN_PAGE}description"
    URL_DONATE_PAGE = "https://opencollective.com/brainup"
    URL_GITHUB = "https://github.com/Brain-up/brn"
    URL_GROUPS_PAGE = f"{URL_MAIN_PAGE}groups"
    URL_LOGIN_PAGE = f"{URL_MAIN_PAGE}login"
    URL_PROFILE_PAGE = f"{URL_MAIN_PAGE}profile"
    URL_REGISTRATION_PAGE = f"{URL_MAIN_PAGE}registration"
    URL_SPECIALISTS_PAGE = f"{URL_MAIN_PAGE}specialists"
    URL_TELEGRAM_PAGE = "https://t.me/BrainUpUsers"
    URL_USED_RESOURCES_PAGE = f"{URL_MAIN_PAGE}used-resources"


class ExercisesUrls:
    STARTING_POINT = MainPageLinks.URL_GROUPS_PAGE
    breadcrumbs_urls_ru = (STARTING_POINT, f"{STARTING_POINT}/2")

    a = f"{STARTING_POINT}/2/series/"
    group_link_urls = (f"{a}1", f"{a}2", f"{a}3", f"{a}4", f"{a}5", f"{a}6", f"{a}17")

    # Speech Exercises RU > Similar Phrases
    URL_EXERCISES_RU_SIMILAR_PHRASES_PAGE = f"{STARTING_POINT}/2/series/2"

    breadcrumbs_urls_ru_similar_phrases = breadcrumbs_urls_ru + (URL_EXERCISES_RU_SIMILAR_PHRASES_PAGE,)

    b = f"{URL_EXERCISES_RU_SIMILAR_PHRASES_PAGE}/subgroup/"
    subgroup_link_urls_ru_similar_phrases = (f"{b}60", f"{b}61", f"{b}62", f"{b}63", f"{b}64", f"{b}65")

    # Speech Exercises RU > Words
    URL_EXERCISES_RU_WORDS_PAGE = f"{STARTING_POINT}/2/series/1"

    breadcrumbs_urls_ru_words = breadcrumbs_urls_ru + (URL_EXERCISES_RU_WORDS_PAGE,)

    c = f"{URL_EXERCISES_RU_WORDS_PAGE}/subgroup/"
    subgroup_link_urls_ru_words = (
        f"{c}1", f"{c}2", f"{c}3", f"{c}4", f"{c}5", f"{c}6", f"{c}7", f"{c}8", f"{c}9", f"{c}10", f"{c}11", f"{c}12",
        f"{c}13", f"{c}14", f"{c}15", f"{c}16", f"{c}17", f"{c}18", f"{c}19", f"{c}20", f"{c}21", f"{c}22", f"{c}23",
        f"{c}24", f"{c}25", f"{c}26", f"{c}27", f"{c}28", f"{c}29", f"{c}30", f"{c}31", f"{c}32", f"{c}33", f"{c}34",
        f"{c}35", f"{c}36", f"{c}37", f"{c}38", f"{c}39", f"{c}40", f"{c}41", f"{c}42", f"{c}43", f"{c}44", f"{c}45",
        f"{c}46")

    # Speech Exercises > Words > Family
    URL_EXERCISE1_MODAL_WINDOW_PAGE = f"{STARTING_POINT}/4/series/9/subgroup/73/exercise/919/task/919"
