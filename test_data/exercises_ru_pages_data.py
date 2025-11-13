"""Data for verifying web elements on pages with exercises on the 'ru' local"""


class ExercisesRuPagesData:

    # common data
    tab_title_ru = ("Речевые упражнения (готовы для занятий) | BrainUp",)

    links_status_code = (200,)

    # breadcrumbs data
    b1 = ''
    b2 = 'Речевые упражнения (готовы для занятий)'
    breadcrumbs_text_ru_similar_phrases = (b1, b2, 'Похожие фразы')
    breadcrumbs_text_words_ru = (b1, b2, 'Слова')

    # group links data
    group_links_text = ('СЛОВА', 'СЛОВА КОРОЛЁВОЙ', 'ПОХОЖИЕ ФРАЗЫ', 'ГРУППА СЛОВ', 'ПРЕДЛОЖЕНИЯ',
                        'СЛОВА С ЧАСТОТНОЙ ГРУППИРОВКОЙ')

    group_link_titles = ('Распознавание слов',
                         'Слова по методическому пособию Инны Васильевны Королевой Учусь слушать и говорить',
                         'Распознавание похожих фраз', 'Распознавание последовательности слов',
                         'Распознавание предложений', 'Слова с частотной группировкой')

    group_link_active_links = ('Слова', 'Слова Королёвой', 'Похожие фразы', 'Группа слов', 'Предложения',
                               'Слова с частотной группировкой')

    # subgroup links data
    s = 'background-image: url("https://brnup.s3.eu-north-1.amazonaws.com/pictures/theme/'
    e = '.svg");'

    subgroup_links_style_similar_phrases_ru = (
        f"{s}longShortPhrases{e}", f"{s}noPhrases{e}", f"{s}similarPhrases{e}", f"{s}differentEndPhrases{e}",
        f"{s}shortWords{e}", f"{s}prepositionPhrases{e}")

    subgroup_links_style_words_ru = (
        f"{s}family{e}", f"{s}home{e}", f"{s}food{e}", f"{s}clothes{e}", f"{s}school{e}", f"{s}math{e}", f"{s}pets{e}",
        f"{s}animals{e}", f"{s}transport{e}", f"{s}colors{e}", f"{s}city{e}", f"{s}country{e}", f"{s}walk{e}",
        f"{s}weather{e}", f"{s}future{e}", f"{s}body{e}", f"{s}game{e}", f"{s}adventure{e}", f"{s}hospital{e}",
        f"{s}feelings{e}", f"{s}toys{e}", f"{s}insects{e}", f"{s}interior{e}", f"{s}kitchen{e}", f"{s}music{e}",
        f"{s}musical_instruments{e}", f"{s}birds{e}", f"{s}jewelry{e}", f"{s}history{e}", f"{s}actions{e}",
        f"{s}audible_actions{e}", f"{s}more_transport{e}", f"{s}special_transport{e}", f"{s}fruit_trees{e}",
        f"{s}plants{e}", f"{s}trees{e}", f"{s}sport{e}", f"{s}shop{e}", f"{s}artiodactyls{e}", f"{s}dogs{e}",
        f"{s}stationery{e}", f"{s}flowers{e}", f"{s}literature{e}", f"{s}physics{e}", f"{s}biology{e}",
        f"{s}instruments{e}")

    subgroup_links_text_similar_phrases_ru = (
        'Разной длительности', 'С частицей Не', 'Похожие', 'С разным окончанием', 'Из коротких слов',
        'С разными предлогами')

    subgroup_links_text_words_ru = (
        'Семья', 'Любимый дом', 'Что я ем', 'Одежда', 'В школе', 'Математика', 'Домашние питомцы', 'Мир животных',
        'Транспорт', 'Цвета и форма', 'В городе', 'В деревне', 'На прогулке', 'Погода', 'Стану кем хочу',
        'Тело человека', 'Развлечения', 'Путешествия', 'В больнице', 'Что я чувствую', 'Игрушки', 'Насекомые',
        'Интерьер', 'На кухне', 'Музыка', 'Музыкальные инструменты', 'Птицы', 'Украшения', 'История', 'Действия',
        'Действия(слышимые)', 'Транспорт Дополнение', 'Транспорт (спецтехника)', 'Плодовые деревья и кусты',
        'Растения', 'Деревья и кустарники', 'Спорт', 'В магазине', 'Парнокопытные', 'Породы собак',
        'Канцелярские принадлежности', 'Цветы', 'Русский язык и литература', 'Физика', 'Биология', 'Инструменты')
