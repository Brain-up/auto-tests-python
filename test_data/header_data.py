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

    links_text_auth = ("УПРАЖНЕНИЯ", "Упражнения", "GROUPS",
                       "СТАТИСТИКА", "Статистика", "STATISTICS",
                       "ОПИСАНИЕ", "Описание", "ABOUT",
                       "TELEGRAM", "Telegram",
                       "Пожертвовать", "Donate",
                       "GitHub",
                       "Контакты", "Contacts",
                       "Специалисты", "Specialists",
                       "Наша команда", "Contributors",
                       "Используемые ресурсы", "Used Resources",
                       "Аудиометрия", "Audiometry")

    buttons_text = ('RU', 'EN', 'ЕЩЕ...', 'MORE...')

    ru_en_buttons_text = "RU / EN"

    title_text_ru_unauth = "Преимущества"
    title_text_en_unauth = "Advantages"
    titles_text_unauth = ("Преимущества", "Advantages")

    title_text_ru_auth = "Давайте выберем, какие упражнения будем делать сегодня?"
    title_text_en_auth = "Let's choose what exercises we do today?"

    link_titles = "Телеграм чат для пользователей"

    s = Links.URL_MAIN_PAGE                         #
    s0 = f"{s}audiometry"                           # dropdown
    s1 = f"{s}contact"                              # dropdown
    s2 = f"{s}contributors"                         # dropdown
    s3 = f"{s}description"                          #, # dropdown
    s4 = f"{s}groups?locale=ru-ru"                  #, # dropdown
    s5 = f"{s}groups?locale=en-us"
    s6 = f"{s}profile"                              # icon
    s7 = f"{s}profile/statistics"                   #, # dropdown, # icon
    s8 = f"{s}registration"
    s9 = f"{s}specialists"                          # dropdown
    s10 = f"{s}used-resources"                      # dropdown
    s11 = "https://github.com/Brain-up/brn"         # dropdown
    s12 = "https://opencollective.com/brainup"      # dropdown
    s13 = "https://t.me/BrainUpUsers"               #, # dropdown

    set_auth = (s, s0, s1, s2, s3, s4, s5, s6, s7, s9, s10, s11, s12, s13)
    set_unauth = (s, s1, s2, s3, s8, s9, s10, s11, s12, s13)

    link_status_codes = (200,)

    icons_xmlns = ("http://www.w3.org/2000/svg",)
    logo_image_xmlns = "http://www.w3.org/2000/svg"

    profile_avatar_src = f"{s}pictures/avatars/avatar%201.png"
    profile_avatar_alt = "user avatar"
