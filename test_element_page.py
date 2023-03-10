from pages.element_page import ElementPage

url = 'https://demoqa.com/'

def test_element_page(browser):
    page = ElementPage(browser, url)
    page.open()
    page.check_demoqa_site()
    page.go_to_element_page()
    page.open_checkbox_tab()
    page.open_home_dir()
    page.open_download_dir()
    page.choose_word_file()