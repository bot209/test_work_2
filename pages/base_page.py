from selenium.webdriver.support.ui import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)
        
    def element_is_visible(self, who, im):
        return WD(self.browser, timeout=5).until(EC.visibility_of_element_located((who, im)))
