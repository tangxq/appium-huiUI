from parameterized import parameterized
from base.api import *
from testcase.common import Meta


class TestLogin(Meta):
    """登录"""

    @classmethod
    def setUpClass(cls):
        super(TestLogin, cls).setUpClass()
        cls.public_page.click_b_center()
        cls.common.logout()

    @screen_shot
    def setUp(self):
        """初始化进入到登录页"""
        if not self.uiHelper.element_is_show(
                self.login_page.remember_pwd
        ):
            self.login_page.click_shop_pwd_title()

    @screen_shot
    def tearDown(self):
        """初始化进入登录页"""
        self.common.coming_login_page()

    @case(Case.level1)
    def test_no_remember_pwd(self):
        """[登录]未记住密码功能验证"""
        self.login_page.send_keys_login_name()
        self.login_page.send_keys_login_pwd()
        if self.login_page.check_rem_pwd_checked() == 'true':
            self.login_page.click_rem_pwd()
        self.login_page.click_login_btn()
        self.public_page.click_b_center()
        self.common.logout()
        time.sleep(3)  # 这个页面会弹检查新版本的toast提示所以等待3s再点击
        self.login_page.click_login_btn(verify=False)
        self.assertTrue(
            self.uiHelper.find_toast('用户ID或者密码不能为空'),
            "toast提示未找到"
        )

    @case(Case.level1)
    def test_remember_pwd(self):
        """[登录]记住密码功能验证"""
        self.login_page.send_keys_login_name()
        self.login_page.send_keys_login_pwd()
        if self.login_page.check_rem_pwd_checked() == 'false':
            self.login_page.click_rem_pwd()
        self.login_page.click_login_btn()
        self.public_page.click_b_center()
        self.common.logout()
        self.login_page.click_login_btn()

    @parameterized.expand([
        ("01", '15000000000', '111111'),
        ("02", '1500291xxxx', '111111')
    ])
    @case(Case.level1)
    def test_username_pwd_error(self, name, username, pwd):
        """[登录]账号密码错误登陆验证"""
        self.common.login(username, pwd, verify=False)
        self.assertTrue(
            self.uiHelper.find_toast('用户名或密码错误'),
            "toast提示未找到"
        )

    @case(Case.level2)
    def test_phone_invalid(self):
        """[登录]手机号无效验证"""
        self.login_page.click_phone_code_title()
        self.login_page.send_keys_phone_name('11111111111')
        self.login_page.send_keys_phone_pwd('11111')
        self.login_page.click_login_btn(verify=False)
        self.assertTrue(
            self.uiHelper.find_toast('请输入正确的手机号'),
            "toast提示未找到"
        )


if __name__ == "__main__":
    unittest.main()
