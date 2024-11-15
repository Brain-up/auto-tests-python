"""Data for verifying web elements on the 'Contributors' page"""
from test_data.links import MainPageLinks as Links


class ContributorsPageData:
    description_count = 68
    link_count = 67

    tab_title = ["Наша команда | BrainUp", "Contributors | BrainUp"]

    page_title = ["Наша команда", "Our Team"]

    page_subtitles = [
        "Разработчики", "Тестировщики автоматизаторы", "Тестировщики",
        "Developers", "Developers in test", "Quality Assurance"
    ]

    text_on_page = [
        "Мы собрались все вместе, чтобы сделать вашу жизнь проще!",
        "We are all here to make your life easier!"
    ]

    all_team_link_href = f"{Links.URL_MAIN_PAGE}contributors#"
    all_team_link_status_code = 200
    all_team_link_text = ["Вся Команда", "All Team"]

    images_alt = "user avatar"
    images_src_start = "https://avatars.githubusercontent"
