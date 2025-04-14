"""Data for verifying web elements in the Header on web pages"""
from test_data.links import MainPageLinks as Links


class HeaderData:
    links_text_unauth = ("ОПИСАНИЕ", "ABOUT",
                         "TELEGRAM",
                         "Пожертвовать", "Donate",
                         "GitHub",
                         "Контакты", "Contacts",
                         "Специалисты", "Specialists",
                         "Наша команда", "Contributors",
                         "Используемые ресурсы", "Used Resources",
                         "Регистрация", "Registration")

    links_text_auth = ("УПРАЖНЕНИЯ", "GROUPS",
                       "СТАТИСТИКА", "STATISTICS",
                       "ОПИСАНИЕ", "ABOUT",
                       "TELEGRAM",
                       "Пожертвовать", "Donate",
                       "GitHub",
                       "Контакты", "Contacts",
                       "Специалисты", "Specialists",
                       "Наша команда", "Contributors",
                       "Используемые ресурсы", "Used Resources")

    buttons_text = ('RU', 'EN', 'ЕЩЕ...', 'MORE...')

    ru_en_buttons_text = "RU / EN"

    title_text_ru_unauth = "Преимущества"
    title_text_en_unauth = "Advantages"
    titles_text_unauth = ("Преимущества", "Advantages")

    title_text_ru_auth = "Давайте выберем, какие упражнения будем делать сегодня?"
    title_text_en_auth = "Let's choose what exercises we do today?"

    link_titles = "Телеграм чат для пользователей"

    links_href_unauth = (f"{Links.URL_MAIN_PAGE}",
                         f"{Links.URL_MAIN_PAGE}description",
                         "https://t.me/BrainUpUsers",
                         "https://opencollective.com/brainup",
                         "https://github.com/Brain-up/brn",
                         f"{Links.URL_MAIN_PAGE}contact",
                         f"{Links.URL_MAIN_PAGE}specialists",
                         f"{Links.URL_MAIN_PAGE}contributors",
                         f"{Links.URL_MAIN_PAGE}used-resources",
                         f"{Links.URL_MAIN_PAGE}registration")

    links_href_auth = (f"{Links.URL_MAIN_PAGE}",
                       f"{Links.URL_MAIN_PAGE}groups?locale=ru-ru",
                       f"{Links.URL_MAIN_PAGE}groups?locale=en-us",
                       f"{Links.URL_MAIN_PAGE}profile/statistics",
                       f"{Links.URL_MAIN_PAGE}description",
                       "https://t.me/BrainUpUsers",
                       "https://opencollective.com/brainup",
                       "https://github.com/Brain-up/brn",
                       f"{Links.URL_MAIN_PAGE}contact",
                       f"{Links.URL_MAIN_PAGE}specialists",
                       f"{Links.URL_MAIN_PAGE}contributors",
                       f"{Links.URL_MAIN_PAGE}used-resources",
                       f"{Links.URL_MAIN_PAGE}profile")

    link_status_codes = (200,)

    pages_urls_unauth = (f"{Links.URL_MAIN_PAGE}description",
                         "https://t.me/BrainUpUsers",
                         f"{Links.URL_MAIN_PAGE}registration",
                         f"{Links.URL_MAIN_PAGE}contact",
                         f"{Links.URL_MAIN_PAGE}specialists",
                         f"{Links.URL_MAIN_PAGE}contributors",
                         f"{Links.URL_MAIN_PAGE}used-resources",
                         "https://opencollective.com/brainup",
                         "https://github.com/Brain-up/brn",
                         f"{Links.URL_MAIN_PAGE}")

    pages_urls_auth = (f"{Links.URL_MAIN_PAGE}groups?locale=ru-ru",
                       f"{Links.URL_MAIN_PAGE}groups?locale=en-us",
                       f"{Links.URL_MAIN_PAGE}profile/statistics",
                       f"{Links.URL_MAIN_PAGE}description",
                       "https://t.me/BrainUpUsers",
                       f"{Links.URL_MAIN_PAGE}profile",
                       f"{Links.URL_MAIN_PAGE}contact",
                       f"{Links.URL_MAIN_PAGE}specialists",
                       f"{Links.URL_MAIN_PAGE}contributors",
                       f"{Links.URL_MAIN_PAGE}used-resources",
                       "https://opencollective.com/brainup",
                       "https://github.com/Brain-up/brn",
                       f"{Links.URL_MAIN_PAGE}")

    icons_xmlns = ("http://www.w3.org/2000/svg",)
    logo_image_xmlns = "http://www.w3.org/2000/svg"

    profile_avatar_src = f"{Links.URL_MAIN_PAGE}pictures/avatars/avatar%201.png"
    profile_avatar_alt = "user avatar"
