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
            "в общении с друзьями и знакомыми.",

            "Train for just 30 minutes a day to develop and achieve results",

            "The first free online program for adults and children with cognitive speech perception problems. "
            "All our lessons are designed for children aged 7 and older. "
            "Currently, the program includes more than 20 different topics that you can start working on right away. "
            "And there will be even more — we plan to constantly expand our list of topics.",

            "We wanted the learning format to be as convenient as possible for each of our users. "
            "That is why our lessons are available at any time. "
            "You can choose when to study and create your own lesson schedule.",

            "By following our program, you will be able to develop your hearing in various acoustic situations; "
            "train your auditory memory by listening to exercises as many times as you need. "
            "Additionally, you can expand your vocabulary in an engaging, "
            "game-like format and later use new words in conversations with friends and acquaintances."
        )
    }

    login_link_text = ("Начать", "Login")

    login_link_href = f"{Links.URL_MAIN_PAGE}login"

    login_link_status_code = (200,)

    page_url = Links.URL_MAIN_PAGE

    image_src_in_section1 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAyAAAAGICAYAAAC5"

    image_alt_in_section1 = "girl with book"
