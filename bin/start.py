import os
import sys
import unittest
from BeautifulReport import BeautifulReport

# 将工作目录添加到环境变量（运行start.py文件--重要必加）
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from comment.ui.comments import Driver
from settings.config import logger

from settings.config import UI_REPORT_PATH, UI_DESCRIPTION, UI_DISCOVER_PATH, API_REPORT_PATH, API_DESCRIPTION, \
    API_DISCOVER_PATH


def run(DISCOVER_PATH, DESCRIPTION, REPORT_PATH):
    '''全部测试集执行完后退出浏览器'''

    # 可以放登录流程（使用需要登录使用的测试步骤）
    suite = unittest.TestLoader().discover(DISCOVER_PATH)

    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # 如果在windows中BeautifulReport.py中409行"with open(override_path + self.filename, 'w', encoding='utf-8', newline='\n') as write_file:"去掉"override_path + "
    # 其他系统不变
    reports = BeautifulReport(suites=suite)
    reports.report(description=DESCRIPTION, filename=REPORT_PATH)


def apirun():
    run(API_DISCOVER_PATH, API_DESCRIPTION, API_REPORT_PATH)


def uirun():
    driver = Driver()
    run(UI_DISCOVER_PATH, UI_DESCRIPTION, UI_REPORT_PATH)
    driver.close_browser()


if __name__ == '__main__':
    if sys.argv[1] == 'api':
        apirun()
    elif sys.argv[1] == 'ui':
        uirun()
    else:
        uirun()
        apirun()
