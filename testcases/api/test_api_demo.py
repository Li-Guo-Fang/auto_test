import unittest
import ddt

from comment.api.vote import VoteApi

from util.csv_handler import csv_handler
from settings.config import logger

"""本文件只做数据处理:测试用例的断言"""


@ddt.ddt
class VoteApiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api = VoteApi()

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    @classmethod
    def tearDownClass(cls) -> None:
        ...


    @ddt.data({'expect_data': '登陆成功', 'data': {'username': 'test', 'password': '123456'}})  # 常用
    # @ddt.data(*csv_handler.get_test_cases())
    @ddt.unpack
    # @unittest.skip
    def test_vote_login(self, expect_data, data):
        # logger.info(f"执行的测试用例为 {search_world}")
        real_value = self.api.login(data)
        self.assertEqual(expect_data, real_value.get('msg'))


    @ddt.data({'expect_data': 200})  # 常用
    # @ddt.data(*csv_handler.get_test_cases())
    @ddt.unpack
    def test_vote_subject(self, expect_data):
        # logger.info(f"执行的测试用例为 {search_world}")
        real_value = self.api.subject()
        self.assertEqual(expect_data, real_value.get('code'))

    @ddt.data({'expect_data': 200, 'data': {'sno': '2'}})  # 常用
    # @ddt.data(*csv_handler.get_test_cases())
    @ddt.unpack
    def test_vote_teacher(self, expect_data, data):
        # logger.info(f"执行的测试用例为 {search_world}")
        real_value = self.api.teacher(data)
        self.assertEqual(expect_data, real_value.get('code'))

    @ddt.data({'expect_data': '投票成功', 'data': {'tno': '4', 'is_good': '1'}})  # 常用
    # @ddt.data(*csv_handler.get_test_cases())
    @ddt.unpack
    def test_vote_praise(self, expect_data, data):
        # logger.info(f"执行的测试用例为 {search_world}")
        real_value = self.api.praise(data)
        self.assertEqual(expect_data, real_value.get('msg'))

    @ddt.data({'expect_data': '注销成功', 'data': {'uid': '1'}})  # 常用
    # @ddt.data(*csv_handler.get_test_cases())
    @ddt.unpack
    def test_vote_logout(self, expect_data, data):
        # logger.info(f"执行的测试用例为 {search_world}")
        real_value = self.api.logout(data)
        self.assertEqual(expect_data, real_value.get('msg'))


if __name__ == '__main__':
    unittest.main()
