"""Data for verifying web elements on the starting page for unauthorized users"""
from test_data.links import MainPageLinks as Links


class StartUnauthorizedPageData:
    amount_of_sections_with_content_on_page = 2

    tab_title = "BrainUp"

    page_titles = ("BrainUP - онлайн занятия для детей и взрослых", "Преимущества",
                   "BrainUP - online classes for children and adults", "Advantages")

    page_subtitles = ("BRAINUP", "ОНЛАЙН ЗАНЯТИЯ", "РАЗВИТИЕ")

    text_on_page = {
        "text_in_section1": (
            "Наш сайт - это платформа интерактивных упражнений для взрослых и детей от семи лет с когнитивными "
            "проблемами восприятия речи, которая помогает тренировать способности слушать и понимать",
            "Our site is a platform of interactive exercises for adults and children from the age of seven with "
            "cognitive speech perception problems, which helps to train the ability to listen and understand."),

        "text_in_section2": (
            "Тренируйтесь всего от 30 минут в день для развития и получения результата",

            "Первая бесплатная онлайн программа для взрослых и детей с когнитивными проблемами восприятия речи. "
            "Все наши занятия рассчитаны на возраст детей от 7 лет и старше. "
            "Уже сейчас программа насчитывает более 20 разных тем по которым вы можете начать заниматься уже сейчас. "
            "А дальше будет еще больше - мы планируем постоянно расширять список наших тем.",

            "Мы хотели чтобы формат обучения был максимально удобным для каждого нашего пользователя. "
            "Именно поэтому наши уроки доступны в любое время. "
            "Вы ожете сами выбрать в какое время вам заниматься и сформировать собственное расписание занятий.",

            "Занимаясь по нашей программе, вы сможете, развивать слух в различных акустических ситуациях; "
            "тренировать слуховую память, прослушивая упражнения столько раз, сколько необходимо именно вам. "
            "А также, расширить словарный запас в интересной игровой форме и в дальшейшем использовать новые слова "
            "в общении с друзьями и знакомыми.")
    }

    login_link_text = ("Начать", "Login")

    login_link_href = f"{Links.URL_MAIN_PAGE}login"

    login_link_status_code = (200,)

    page_url = Links.URL_MAIN_PAGE

    image_src_in_section1 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAyAAAAGICAYAAAC5"

    image_alt_in_section1 = "girl with book"
