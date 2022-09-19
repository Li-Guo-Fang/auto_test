import random
import time
import threading

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings.config import *
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])    #屏蔽selenium自带log信息

class SingletonType(type):
    _instance_lock = threading.Lock()
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._instance_lock:
                if cls._instance is None:
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Driver():
    driver = None
    TIMEOUT = TIMEOUT
    IMPLICITLY_TIME = IMPLICITLY_TIME

    def __init__(self, browser='chrome'):
        if self.driver is None:
            self.driver = self.open_browser(browser)

    @classmethod
    def open_browser(cls, browser):
        if cls.driver is None:
            if browser == 'chrome':
                cls.driver = webdriver.Chrome(executable_path=CHROME_PATH,options=chrome_options)
            elif browser == 'firefox':
                ...
            else:
                ...
            cls.driver.implicitly_wait(IMPLICITLY_TIME)
            logger.debug(f"设置隐式等待时间： {IMPLICITLY_TIME}s")
            cls.driver.maximize_window()
        return cls.driver

    @classmethod
    def close_browser(cls):
        cls.driver.quit()
        logger.debug("关闭浏览器成功")

    def get_url(self, url):
        self.driver.get(url)
        logger.debug(f"打开网页成功: {url}")

    def locator_element(self, locator):
        WebDriverWait(self.driver, timeout=self.TIMEOUT).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def send_keys(self, element, value):
        self.locator_element(element).send_keys(value)
        logger.debug(f'输入文本成功 element: {element} value: {value}')

    @staticmethod
    def random_wait():
        time.sleep(random.randint(1, 3))

    def element_click(self, element):
        self.locator_element(element).click()
        logger.debug(f"点击 element: {element}")

    def get_text(self, element):
        # self.random_wait()
        ele = self.locator_element(element)
        logger.debug(f"获取文本成功 value: {element}")
        return ele.text
