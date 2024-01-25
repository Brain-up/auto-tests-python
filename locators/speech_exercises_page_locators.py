import random

from selenium.webdriver.common.by import By


class AuthorizedUserHomePageLocators:
    """
    link: https://brainup.site/groups
    """
    # Header
    EN_BUTTON = (By.XPATH, "//*[contains(text(),'EN')]")
    RU_BUTTON = (By.XPATH, "//*[contains(text(),'RU')]")
    PROFILE_USER = (By.XPATH, '//a[@href="/profile"]')

    SPEECH_EXERCISES_RU = (By.XPATH, '//a[@title="Речевые упражнения"]')
    SPEECH_EXERCISES_EN = (By.XPATH, '//a[@title="Speech"]')

    # Speech exercises_EN Header
    WORDS_BUTTON_EN = (By.XPATH, '//button[@data-test-active-link = "Words"]')

    # Speech exercises_RU Header
    WORDS_BUTTON_RU = (By.XPATH, '//button[@data-test-active-link="Слова"]')
    WORDS_BY_KOROLEVA_BUTTON = (By.XPATH, '//button[@data-test-active-link="Слова Королёвой"]')
    WORDS_SIMILAR_PHRASES_RU = (By.XPATH, '//button[@title="Распознавание похожих фраз"]')


class SpeechExercisesPageLocators:
    """
    link: https://brainup.site/groups/2/series/1
    """
    BUTTON_INTERACT = (By.XPATH, '//*[text()="Interact"]')
    BUTTON_SOLVE = (By.XPATH, '//*[text()="Solve"]')
    BUTTON_START_EN = (By.XPATH, '//button[@aria-label="Start exercise"]')
    BUTTON_START_RU = (By.XPATH, '//button[@aria-label="Начать выполнение упражнения"]')
    LIST_WORDS_IN_CARD = (By.XPATH, '//li[@class="task-player__option flex"]')
    PROGRESS_BAR = (By.XPATH, '//div[@class="progress-bar"]')

    FAMILY_CARD_RU = (By.XPATH, '//a[@title="Слова про семью"]')
    FAMILY_CARD_EN = (By.XPATH, '//a[@title="Family words"]')
    WORD_1_GROUP = (By.XPATH, '//a[@title="1я группа слов: по одному"]')
    DIV_SIMILAR_PHRASE_RU = (By.XPATH, '//div[@class="series-page--canvas flex justify-center flex-grow"]')

    # SubGroups
    SENTENCES = (By.ID, 'ember315')
    SIMILAR_PHRASES = (By.ID, 'ember313')
    SIMILAR_PHRASES_GROUP = (By.XPATH, '(//aside//li)[1]')
    WORDS_EN = (By.XPATH, '//button[@data-test-active-link="Words"]')
    WORDS_GROUP = (By.ID, 'ember314')
    WORDS_GROUP_BY_FREQUENCY = (By.ID, 'ember316')

    # WORDS
    LIST_OF_CARD_FROM_WORDS = (
        By.XPATH,
        '//div[@class="sm:tracking-normal sm:leading-normal sm:text-base '
        'text-xs leading-none tracking-tighter text-center"]')

    RANDOM_CARD_FROM_WORDS = (By.XPATH,
                              f'//div[@class="sm:tracking-normal sm:leading-normal '
                              f'sm:text-base text-xs leading-none tracking-tighter text-center"]'
                              f'[{str(random.randint(1, len(LIST_OF_CARD_FROM_WORDS)))}]')

    LIST_CARDS_ID = (By.XPATH, '//div[@class="flex"]')
    RANDOM_CARDS_FROM_SIMILAR = (By.XPATH, f'//div[@class="flex"][{str(random.randint(1, len(LIST_CARDS_ID)))}]')

    # Слова
    LIST_OF_CARD_FROM_WORDS_RU = (By.XPATH,
                                  '//div[@class ="sm:grid-cols-4 gap-y-2 sm:gap-y-3 grid grid-cols-3 mx-2 mb-4"] / a')

    # Cards in the SIMILAR PHRASES GROUP
    CARDS_LIST_IN_SIMILAR_PHRASES = (By.XPATH, '//div[contains(@class, "series-container")]//a')

