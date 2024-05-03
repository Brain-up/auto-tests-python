"""Data for verifying web elements on the 'Contacts' page"""


class ContactsPageData:
    amount_of_sections_with_content_on_page = 2

    page_title = ["Контакты", "Contacts"]

    page_subtitles = [
        ["Для пользователей:", "Для разработчиков:"],
        ["For users:", "For developers:"]
    ]

    text_on_page = [
        ["Telegram чат для пользователей https://t.me/BrainUpUsers",
         "По любым вопросам, идеям, пожалуйста, пишите на электронную почту проекта brainupproject@yandex.ru",
         "Основатель проекта и технический руководитель Telegram Елена Мошникова https://t.me/ElenaLovesSpb"],
        ["Telegram chat for users https://t.me/BrainUpUsers",
         "In any questions, ideas please write to project email brainupproject@yandex.ru",
         "project founder and tech lead in Telegram Elena Moshnikova https://t.me/ElenaLovesSpb"]
    ]

    links_href = [
        "https://t.me/BrainUpUsers",
        "mailto:brainupproject@yandex.ru",
        "https://t.me/ElenaLovesSpb"
    ]

    links_text = [
        "https://t.me/BrainUpUsers",
        "brainupproject@yandex.ru",
        "https://t.me/ElenaLovesSpb"
    ]
