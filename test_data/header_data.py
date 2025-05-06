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

    s = Links.URL_MAIN_PAGE
    s1 = f"{s}contact"
    s2 = f"{s}contributors"
    s3 = f"{s}description"
    s4 = f"{s}groups?locale=ru-ru"
    s5 = f"{s}groups?locale=en-us"
    s6 = f"{s}profile"
    s7 = f"{s}profile/statistics"
    s8 = f"{s}registration"
    s9 = f"{s}specialists"
    s10 = f"{s}used-resources"
    s11 = "https://github.com/Brain-up/brn"
    s12 = "https://opencollective.com/brainup"
    s13 = "https://t.me/BrainUpUsers"

    set_auth = (s, s1, s2, s3, s4, s5, s6, s7, s9, s10, s11, s12, s13)
    set_unauth = (s, s1, s2, s3, s8, s9, s10, s11, s12, s13)

    link_status_codes = (200,)

    icons_xmlns = ("http://www.w3.org/2000/svg",)
    logo_image_xmlns = "http://www.w3.org/2000/svg"

    profile_avatar_src = f"{s}pictures/avatars/avatar%201.png"
    profile_avatar_alt = "user avatar"
