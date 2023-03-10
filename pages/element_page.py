from .base_page import BasePage
from .locators import ElementPageLocators

class ElementPage(BasePage):

    #1
    def check_demoqa_site(self):
        link = self.element_is_visible(*ElementPageLocators.DEMOQA_URL)
        assert link, 'Сайт DEMOQA не открылся'
    
    #2
    def go_to_element_page(self):
        self.element_is_visible(*ElementPageLocators.ELEMENT_LINK).click()
        text = self.element_is_visible(*ElementPageLocators.ELEMENT_PAGE).text
        assert text == 'Elements', 'Страница Elements не открылась'

    #3
    def open_checkbox_tab(self):
        tab = self.element_is_visible(*ElementPageLocators.CHECK_BOX_TAB)
        tab.click()
        tab_text = tab.text
        assert tab_text == 'Check Box', 'Страница Check Box не открылась'

    #4
    def open_home_dir(self):
        self.element_is_visible(*ElementPageLocators.TOGGLE_BUTTON).click()
        home_node = self.element_is_visible(*ElementPageLocators.HOME_NODE)
        assert home_node, 'Директория Home не раскрылась'
    
    #5
    def open_download_dir(self):
        self.element_is_visible(*ElementPageLocators.DOWNLOAD_COLLAPSE_BUTTON).click()
        download_node = self.element_is_visible(*ElementPageLocators.DOWNLOAD_NODE)
        assert download_node, 'Директория Downloads не раскрылась'
    
    #6
    def choose_word_file(self):
        self.element_is_visible(*ElementPageLocators.WORLD_FILE_DOC).click()
        word_text = self.element_is_visible(*ElementPageLocators.WORD_TEXT_SUCCESS).text
        text = f'You have selected:{word_text}'
        assert word_text, 'Чекбокс файла WordFile, не выбран'
        assert text == 'You have selected:wordFile', 'Сообщение о успешном выборе WordFile не появилось'
