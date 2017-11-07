import unittest
from base.api import logger


class LoginPage(unittest.TestCase):
    """登录页"""

    def __init__(self, dirver=None):
        super(LoginPage, self).__init__()
        self.driver = dirver

    # 商户密码登录标签
    shop_pwd_title = 'com.huimin.ordersystem:id/login_switch_shop'

    def click_shop_pwd_title(self, verify=True):
        logger.info('点击"商户密码登录"标签')
        self.driver.click(self.shop_pwd_title)
        self.assertTrue(
            self.driver.element_is_show(self.remember_pwd),
            "记住密码按钮未显示"
        ) if verify else None

    # 用户名输入框
    login_name = 'com.huimin.ordersystem:id/login_name'

    def send_keys_login_name(self, username='xxxxxxx'):
        logger.info('用户名输入框输入{}'.format(username))
        self.driver.send_keys(self.login_name, username)

    # 密码输入框
    login_pwd = 'com.huimin.ordersystem:id/login_pwd'

    def send_keys_login_pwd(self, pwd='xxxxxx'):
        logger.info('密码输入框输入{}'.format(pwd))
        self.driver.send_keys(self.login_pwd, pwd)

    # 立即登录按钮
    login_btn = 'com.huimin.ordersystem:id/login_btlogin'

    def click_login_btn(self, verify=True):
        logger.info('点击"立即登录"')
        self.driver.click(self.login_btn)
        # self.assertTrue(
        #     self.driver.element_in_time(
        #         first_page.FirstPage.sign_in
        #     ),
        #     "签到按钮未找到"
        # ) if verify else None

    # 记住密码
    remember_pwd = 'com.huimin.ordersystem:id/login_rempwd'

    def check_rem_pwd_checked(self):
        status = self.driver.get_attribute(self.remember_pwd, 'checked')
        logger.info('记住密码框勾选:{}'.format(status))
        return status

    def click_rem_pwd(self):
        logger.info('点击"记住密码"')
        self.driver.click(self.remember_pwd)

    # 手机验证码登录标签
    phone_code_title = 'com.huimin.ordersystem:id/login_switch_num'

    def click_phone_code_title(self, verify=True):
        logger.info('点击"手机验证码登录"标签')
        self.driver.click(self.phone_code_title)
        self.assertTrue(
            self.driver.element_is_show(self.phone_code),
            "获取验证码按钮未显示"
        ) if verify else None

    # 手机号输入框
    phone_name = 'com.huimin.ordersystem:id/phone_name'

    def send_keys_phone_name(self, phone_number):
        logger.info('手机号输入框输入{}'.format(phone_number))
        self.driver.send_keys(self.phone_name, phone_number)

    # 验证码输入框
    phone_pwd = 'com.huimin.ordersystem:id/phone_pwd'

    def send_keys_phone_pwd(self, pwd):
        logger.info('验证码输入框输入{}'.format(pwd))
        self.driver.send_keys(self.phone_pwd, pwd)

    # 获取验证码
    phone_code = 'com.huimin.ordersystem:id/phone_code'

    def click_phone_code(self):
        logger.info('点击"获取验证码"')
        self.driver.click(self.phone_code)