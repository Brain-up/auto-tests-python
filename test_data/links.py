class MainPageLinks:
    URL_MAIN_PAGE = "https://brainup.site/"
    # URL_MAIN_PAGE = 'https://brainup.fun/'
    URL_DESCRIPTION_PAGE = f"{URL_MAIN_PAGE}description"
    URL_TELEGRAM_PAGE = "https://t.me/BrainUpUsers"
    URL_DONATE_PAGE = "https://opencollective.com/brainup"
    URL_CONTACTS_PAGE = f"{URL_MAIN_PAGE}contact"
    URL_SPECIALISTS_PAGE = f"{URL_MAIN_PAGE}specialists"
    URL_GITHUB = "https://github.com/Brain-up/brn"
    URL_CONTRIBUTORS_PAGE = f"{URL_MAIN_PAGE}contributors"
    URL_USED_RESOURCES_PAGE = f"{URL_MAIN_PAGE}used-resources"
    URL_LOGIN_PAGE = f"{URL_MAIN_PAGE}login"
    URL_GROUPS_PAGE = f"{URL_MAIN_PAGE}groups"
    URL_PROFILE_PAGE = f"{URL_MAIN_PAGE}profile"
    URL_REGISTRATION_PAGE = f"{URL_MAIN_PAGE}registration"


class SpecificExercisesUrls:
    STARTING_POINT = MainPageLinks.URL_GROUPS_PAGE

    # Speech Exercises > Words > Family
    URL_OF_EXERCISE_1_MODAL_WINDOW_PAGE = f"{STARTING_POINT}/4/series/9/subgroup/73/exercise/919/task/919"
