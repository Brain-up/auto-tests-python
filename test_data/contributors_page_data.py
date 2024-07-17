"""Data for verifying web elements on the 'Contributors' page"""


class ContributorsPageData:
    amount_of_sections_on_page = 1
    card_count = 67
    description_count = 67
    image_count = 67
    link_count = 66
    subsection_count = 5

    page_title = ["Наша команда", "Our Team"]

    page_subtitles = [
        "Разработчики", "Тестировщики автоматизаторы", "Тестировщики",
        "Developers", "Developers in test", "Quality Assurance"
    ]

    slogan_text = ["Мы собрались все вместе, чтобы сделать вашу жизнь проще!",
                   "We are all here to make your life easier!"]

    all_team_link_href = "https://brainup.site/contributors#"
    all_team_link_status_code = 200
    all_team_link_text = ["Вся Команда", "All Team"]

    images_alt = "user avatar"
    images_src_start = "https://avatars.githubusercontent"
