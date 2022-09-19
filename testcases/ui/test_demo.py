import unittest
import ddt
from comment.ui.baidu_search import BaiduSearch

from util.csv_handler import csv_handler
from settings.config import logger

"""本文件只做数据处理:测试用例的断言"""


@ddt.ddt
class BaiduUintTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 调登录流程
        cls.baidu = BaiduSearch()

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    # @ddt.data({'expect': '百度为您找到相关结果约', 'kw_value': 'liguofang'}, {'expect': '百度为您找到相关结果约', 'kw_value': 'lisi'})  # 常用
    @ddt.data(*csv_handler.get_test_cases())
    @ddt.unpack
    def test_baidu3(self, search_world, expect_data):
        logger.info(f"执行的测试用例为 {search_world}")
        data = self.baidu.search(search_world)
        self.assertIn(expect_data, data)


if __name__ == '__main__':
    unittest.main()
