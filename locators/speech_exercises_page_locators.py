from selenium.webdriver.common.by import By


class SpeechExercisesPageLocators:
    """
    link: https://brainup.site/groups/2/series/1
    """
    BUTTON_START = (By.XPATH, '//button[@aria-label="Start exercise"]')
    LIST_CARD_WORDS_WE = (By.XPATH, '//li[@class="task-player__option flex"]')
    PROGRESS_BAR = (By.XPATH, '//div[@class="progress-bar"]')
    BUTTON_SOLVE = (By.XPATH, '//*[text()="Solve"]')
    BUTTON_INTERACT = (By.XPATH, '//*[text()="Interact"]')

    # Language
    FAMILY_CARD_RU = (By.XPATH, '//a[@title="Слова про семью"]')
    FAMILY_CARD_EN = (By.XPATH, '//a[@title="Family words"]')

    # SubGroups
    SIMILAR_PHRASES = (By.ID, 'ember313')
    WORDS_GROUP = (By.ID, 'ember314')
    SENTENCES = (By.ID, 'ember315')
    WORDS_GROUP_BY_FREQUENCY = (By.ID, 'ember316')
    WORDS = (By.ID, 'ember317')

    LIST_CARDS_ID = (By.XPATH, '//div[@class="flex"]')
