from selenium.webdriver.common.by import By

class ElementPageLocators():
    DEMOQA_URL = (By.CSS_SELECTOR, '[href="https://demoqa.com"]')
    ELEMENT_LINK = (By.CSS_SELECTOR, '[class="card mt-4 top-card"]:nth-child(1)')
    ELEMENT_PAGE = (By.CSS_SELECTOR, '[class="main-header"]')
    CHECK_BOX_TAB = (By.XPATH, "//span[text()='Check Box']")
    TOGGLE_BUTTON = (By.CSS_SELECTOR, "button[class='rct-collapse rct-collapse-btn']")
    HOME_NODE = (By.CSS_SELECTOR, '[class="rct-node rct-node-parent rct-node-expanded"]')
    DOWNLOAD_COLLAPSE_BUTTON = (By.CSS_SELECTOR, "#tree-node .rct-node-collapsed:nth-child(3) .rct-collapse-btn")
    DOWNLOAD_NODE = (By.CSS_SELECTOR, '[class="rct-node rct-node-parent rct-node-expanded"]:nth-child(3)')
    WORLD_FILE_DOC = (By.CSS_SELECTOR, '[for="tree-node-wordFile"]')
    WORD_TEXT_SUCCESS = (By.XPATH, "//span[text()='wordFile']")