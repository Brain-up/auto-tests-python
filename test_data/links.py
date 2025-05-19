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

    # Speech Exercises RU > Similar Phrases
    URL_EXERCISES_RU_SIMILAR_PHRASES_PAGE = f"{STARTING_POINT}/2/series/2"

    # Speech Exercises RU > Words
    URL_EXERCISES_RU_WORDS_PAGE = f"{STARTING_POINT}/2/series/1"

    # Speech Exercises > Words > Family
    URL_EXERCISE1_MODAL_WINDOW_PAGE = f"{STARTING_POINT}/4/series/9/subgroup/73/exercise/919/task/919"
