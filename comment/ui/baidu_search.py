from comment.ui.comments import Driver
from comment.ui.baidu_elements import *


class BaiduSearch(Driver):
    def search(self, kw_value):
        self.get_url(PAGE_URL)
        self.send_keys(SEARCH_TEXT, kw_value)
        self.element_click(SEARCH_BTN)
        data = self.get_text(REAL_ELEMENT)

        return data
