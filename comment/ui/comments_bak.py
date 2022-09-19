from selenium import webdriver

from settings.config import *
from logging import log


class Driver:
    driver = None
    def __init__(self):
        if self.driver is None:
            self.driver = self.open_browser()

    @classmethod
    def open_browser(cls,browser='chrome'):
        if cls.driver is None:
            if browser == 'chrome':
                cls.driver = webdriver.Chrome(executable_path=chome_path)
                logger.info("打开chrome浏览器成功")
            elif browser == 'firefox':
                ...
            else:
                ...
            cls.driver.implicitly_wait(implicitly_wait_time)
            logger.info(f"设置隐式等待时间： {implicitly_wait_time}s")
            cls.driver.maximize_window()
        return cls.driver

    @classmethod
    def close_browser(cls):
        cls.driver.quit()
        logger.info("关闭浏览器成功")

    def get_url(self,url):
        self.driver.get(url)
        logger.info(f"打开网页成功: {url}")

    def send_keys(self,method,element,value):
        el = self.driver.find_element(method, element)
        el.send_keys(value)
        logger.info(f'输入文本成功 method: {method} element: {element} value: {value}')


    def element_click(self,method,element):
        ele = self.driver.find_element(method,element)
        ele.click()
        logger.info(f"点击 method: {method} element: {element}")

    def get_text(self,method,value):
        element = self.driver.find_element(method, value)
        logger.info(f"获取文本成功 method: {method} value: {value}")
        return element.text
