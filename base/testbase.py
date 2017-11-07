"""与appium建立连接和断开连接"""
from .uiHelper import UiHelper
from base.api import *


class Meta(type):
    """用例级别划分执行"""
    @staticmethod
    def __new__(cls, *args):
        """
        得到case中定义的case_level 如果case没有定义case_level设定级别为0默认执行，
        如果case定义的case_level小于配置文件中的设置的level使用pop删除该case.
        """
        new_func_dict = dict()
        for i in args[-1]:
            if i.startswith('test_'):
                if getattr(args[-1][i], 'case_level', 0) <= CASE_LEVEL:
                    new_func_dict[i] = args[-1][i]
            else:
                new_func_dict[i] = args[-1][i]
        new_more = (args[0], args[1], new_func_dict)
        return super(Meta, cls).__new__(cls, *new_more)


class TestBase(unittest.TestCase, metaclass=Meta):
        """初始化driver"""
        uiHelper = UiHelper()

        @classmethod
        def setUpClass(cls):
            try:
                logger.info('开始初始化 appium driver.')
                cls.uiHelper.init_driver()
                logger.info('appium driver 初始化完毕.')
            except Exception:
                error = traceback.format_exc()
                logger.error(error)
                logger.error('appium driver初始化失败.')

        @classmethod
        def tearDownClass(cls):
            try:
                cls.uiHelper.quit_driver()
                time.sleep(5)
            except Exception:
                raise
