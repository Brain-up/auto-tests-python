"""Data for verifying web elements on the 'Contacts' page"""


class ContactsPageData:
    amount_of_sections = 2

    tab_title = ("Контакты | BrainUp", "Contacts | BrainUp")

    page_title = ("Контакты", "Contacts")

    page_subtitles = ("Для пользователей:", "Для разработчиков:",
                      "For users:", "For developers:")

    text_on_page = ("Telegram чат для пользователей https://t.me/BrainUpUsers",
                    "По любым вопросам, идеям, пожалуйста, пишите на электронную почту проекта brainupproject@yandex.ru",
                    "Основатель проекта и технический руководитель Telegram Елена Мошникова https://t.me/ElenaLovesSpb",
                    "Telegram chat for users https://t.me/BrainUpUsers",
                    "In any questions, ideas please write to project email brainupproject@yandex.ru",
                    "project founder and tech lead in Telegram Elena Moshnikova https://t.me/ElenaLovesSpb")

    links_text = ("https://t.me/BrainUpUsers",
                  "brainupproject@yandex.ru",
                  "https://t.me/ElenaLovesSpb")

    links_href = ("https://t.me/BrainUpUsers",
                  "mailto:brainupproject@yandex.ru",
                  "https://t.me/ElenaLovesSpb")

    links_status_code = (200,)

    # Related web pages urls
    pages_urls = ("https://t.me/BrainUpUsers",
                  "https://t.me/ElenaLovesSpb")
