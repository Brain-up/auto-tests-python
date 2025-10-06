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
    p = f"{STARTING_POINT}/2/series/"
    group_link_urls = (f"{p}1", f"{p}2", f"{p}3", f"{p}4", f"{p}5", f"{p}6", f"{p}17")

    # Speech Exercises RU > Similar Phrases
    URL_EXERCISES_RU_SIMILAR_PHRASES_PAGE = f"{STARTING_POINT}/2/series/2"
    q = f"{URL_EXERCISES_RU_SIMILAR_PHRASES_PAGE}/subgroup/"
    subgroup_link_urls = (f"{q}60", f"{q}61", f"{q}62", f"{q}63", f"{q}64", f"{q}65")

    # Speech Exercises RU > Words
    URL_EXERCISES_RU_WORDS_PAGE = f"{STARTING_POINT}/2/series/1"

    # Speech Exercises > Words > Family
    URL_EXERCISE1_MODAL_WINDOW_PAGE = f"{STARTING_POINT}/4/series/9/subgroup/73/exercise/919/task/919"
