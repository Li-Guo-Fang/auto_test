import os
import logging.config
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CHROME_PATH = os.path.join(BASE_DIR, 'lib', 'chromedriver.exe')
TIME_NOW = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_%H%M%S')

UI_DESCRIPTION = "百度搜索测试"
API_DESCRIPTION = "vote接口测试"
UI_REPORT_PATH = os.path.join(BASE_DIR, 'report', f'{UI_DESCRIPTION}_{TIME_NOW}.html')
API_REPORT_PATH = os.path.join(BASE_DIR, 'report', f'{API_DESCRIPTION}_{TIME_NOW}.html')
UI_DISCOVER_PATH = os.path.join(BASE_DIR, 'testcases', 'ui')
API_DISCOVER_PATH = os.path.join(BASE_DIR, 'testcases', 'api')

TIMEOUT = 5
IMPLICITLY_TIME = 15
debug_flag = True


class RequireDebugTrue(logging.Filter):
    # 实现filter方法
    def filter(self, record):
        return debug_flag


logging_config = {
    # 必选项，其值是一个整数值，表示配置格式的版本，当前唯一可用的值就是1  'DEBUG INFO WARNING ERROR CRITICAL'
    'version': 1,
    # 是否禁用现有的记录器
    'disable_existing_loggers': False,

    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': RequireDebugTrue,  # 在开发环境，我设置DEBUG为True；在客户端，我设置DEBUG为False。从而控制是否需要使用某些处理器。
        }
    },

    # 日志格式集合,https://blog.csdn.net/claroja/article/details/102601920
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },

    # 处理器集合
    'handlers': {
        # 输出到控制台
        'console': {
            'level': 'INFO',  # 输出信息的最低级别
            'class': 'logging.StreamHandler',
            'formatter': 'simple',  # 使用standard格式
            'filters': ['require_debug_true', ],  # 仅当 DEBUG = True 该处理器才生效
        },
        # 输出到文件
        'log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': os.path.join(BASE_DIR, 'logs', 'debug.log'),  # 输出位置
            'maxBytes': 1024 * 1024 * 5,  # 文件大小 5M
            'backupCount': 5,  # 备份份数
            'encoding': 'utf8',  # 文件编码
        },
        'log1': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': os.path.join(BASE_DIR, 'logs', 'info.log'),  # 输出位置
            'maxBytes': 1024 * 1024 * 5,  # 文件大小 5M
            'backupCount': 5,  # 备份份数
            'encoding': 'utf8',  # 文件编码
        },
    },

    # 日志管理器集合
    'loggers': {
        'root': {
            'handlers': ['console', 'log', 'log1'],
            'level': 'DEBUG',
            'propagate': True,  # 是否传递给父记录器
        },
        'simple': {
            'handlers': ['log1'],
            'level': 'WARNING',
            'propagate': True,  # 是否传递给父记录器,
        },
        'serious': {
            'handlers': ['log'],
            'level': 'ERROR',
            'propagate': True,  # 是否传递给父记录器,
        }
    }
}

logging.config.dictConfig(logging_config)
logger = logging.getLogger('roo')
