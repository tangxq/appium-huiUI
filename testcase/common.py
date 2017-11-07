from selenium.common.exceptions import NoSuchElementException
from base.api import *
from base.testbase import TestBase
from pageobject.login_page import LoginPage
from pageobject.public_page import PublicPage
from pageobject.first_page import FirstPage
from pageobject.center_page import CenterPage
from pageobject.shopcar_page import ShopCarPage


class Meta(TestBase):

    w_name = 'WEBVIEW_com.huimin.ordersystem'

    @classmethod
    def setUpClass(cls):
        super(Meta, cls).setUpClass()
        cls.common = Common(cls.uiHelper)
        cls.login_page = LoginPage(cls.uiHelper)
        cls.public_page = PublicPage(cls.uiHelper)
        cls.first_page = FirstPage(cls.uiHelper)
        cls.center_page = CenterPage(cls.uiHelper)
        cls.shopcar_page = ShopCarPage(cls.uiHelper)
        logger.info('开始查找获取权限的"允许"按钮')
        time.sleep(2)
        while cls.uiHelper.element_is_show(
                '//*[@text="允许"]', period=1
        ):
            logger.info('找到"允许"按钮')
            cls.uiHelper.click('//*[@text="允许"]')
            logger.info('点击"允许"按钮')
            time.sleep(2)
        logger.info("进入引导页")
        cls.uiHelper.swipe_up()
        cls.assertTrue(
            cls.uiHelper.element_in_time(
                cls.first_page.sign_in, retry=6
            ),
            "签到奖励按钮未显示"
        )
        logger.info("进入到首页")
        cls.public_page.click_b_center()
        cls.center_page.click_no_login_btn()
        cls.common.login()

    @screen_shot
    def setUp(self):
        """初始化进入到登录页面"""
        if not self.uiHelper.element_in_time(
                self.first_page.sign_in
        ):
            logger.info('首页加载失败')
            self.uiHelper.start_activity(
                'com.huimin.ordersystem.activity.MainActivity'
            )
            logger.info('重新打开首页')
        self.assertTrue(
            self.uiHelper.element_in_time(
                self.first_page.sign_in
            ),
            "首页加载失败"
        )
        logger.info('进入到首页')

    @screen_shot
    def tearDown(self):
        """初始化进入首页"""
        self.uiHelper.start_activity(
            'com.huimin.ordersystem.activity.MainActivity'
        )


class Common:
    """
    测试case中常用方法
    """
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.public_page = PublicPage(driver)
        self.first_page = FirstPage(driver)
        self.center_page = CenterPage(driver)
        self.shopcar_page = ShopCarPage(driver)

    def login(self, username='xxxxxxx', pwd='xxxxxx', verify=True):
        """
        登录
        """
        self.login_page.send_keys_login_name(username)
        self.login_page.send_keys_login_pwd(pwd)
        self.login_page.click_login_btn(verify)

    def logout(self):
        """
        退出登录
        """
        self.center_page.click_setting_btn()
        self.setting_page.click_logout_btn()

    def coming_login_page(self):
        """
        判断当前页面是否在登录页，若不在进入登录页面
        """
        try:
            logger.info('判断当前是否在登录页')
            self.driver.find_element(
                self.login_page.login_btn, period=3
            )
        except NoSuchElementException:
            try:
                logger.info('当前不在登录页')
                logger.info('查看当前页面是否存在返回按钮')
                while self.driver.find_element(
                        self.public_page.backup_btn, period=2
                ):
                    logger.info('当前页面存在返回按钮')
                    self.public_page.click_backup_btn()
                self.public_page.click_b_center()
                self.logout()
            except NoSuchElementException:
                logger.info('当前页面不存在返回按钮')
                self.public_page.click_b_center()
                self.logout()

    def shop_car_clear(self, verify=True):
        """
        清空购物车
        """
        self.shopCar_page.click_del_goods()
        while self.driver.element_in_time(self.shopCar_page.clear_shopCar, retry=5):
            if self.shopCar_page.get_category_num() == 1:
                self.shopCar_page.click_clear_shopCar()
                self.shopCar_page.click_ok_btn(verify=verify)
            else:
                self.shopCar_page.click_clear_shopCar()
                self.shopCar_page.click_ok_btn(verify=False)
