from selenium.webdriver.common.by import By

PAGE_URL = "https://www.baidu.com/"
SEARCH_TEXT = (By.ID, 'kw')
SETTINGS_BTN = (By.XPATH, "//span[text()='设置']")
SEARCH_BTN = (By.ID, 'su')
REAL_ELEMENT = (By.CSS_SELECTOR, '.hint_PIwZX.c_font_2AD7M')
