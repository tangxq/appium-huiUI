__author__ = 'Administrator'
import unittest, HTMLTestRunner, time, BSTestRunner
from appium import webdriver
from po.firstpage import FirstPage
from po.orderpage import Orderpage
from po.shopcarpage import ShopCarPage
from po.business_center_page import Business_center_page
from po.public import Public
from po.basepage import Action
from assection.assection import Assect

class TestBusinessCenter(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''设置启动appium所需参数，启动一个appium session'''
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = 'oppo'
        # desired_caps['app'] = 'G:/huipeitongUI/package/HPT_V1.3.9.apk'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        #desired_caps['noSign'] = 'true'
        desired_caps['appPackage'] = 'com.huimin.ordersystem'
        desired_caps['appActivity'] = 'com.huimin.ordersystem.activity.WelcomeActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        self.first = FirstPage(self.driver)
        self.order = Orderpage(self.driver)
        self.shopcar = ShopCarPage(self.driver)
        self.business = Business_center_page(self.driver)
        self.public = Public(self.driver)
        self.myassert = Assect(self.driver)
        self.base = Action(self.driver)

    @classmethod
    def tearDownClass(self):
        '''这个class的所有case测试完成退出driver，等待3s,切断session'''
        # self.driver.remove_app()
        self.driver.quit()
        time.sleep(3)

    def setUp(self):
        '''判断首页是否成功启动，成功启动之后再去进入对应模块'''
        self.myassert.assertEw(self.first.first_pge, '首页加载失败')
        self.business.click_business_center()
        self.myassert.assertEw(self.business.order_manage, '商户中心加载失败')


    def tearDown(self):
        '''每次测试完成启动app，进入首页'''
        self.driver.start_activity('com.huimin.ordersystem', 'com.huimin.ordersystem.activity.WelcomeActivity')

    def test_OrderManage(self):
        '''订单管理'''
        self.business.click_order_manage()
        self.myassert.assertEw(self.business.evaluate, '已完成订单页面加载失败')
        self.business.click_history_order()
        self.myassert.assertEw(self.business.canceled, '历史订单页面加载失败')
        self.business.click_check_detail()
        self.myassert.assertEw(self.business.order_detail_goods_name, '订单详情页面加载失败')

    @unittest.skip
    def test_mycollect(self):
        '''我的收藏-取消收藏'''
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '惠民订货页面加载失败')
        self.order.click_goods_img()
        self.myassert.assertEw(self.first.storenum, '商品详情页加载失败')
        goods_name=self.first.get_goods_detail_name()
        self.first.click_collect()
        self.myassert.assertEw(self.first.collected, '收藏商品失败')
        self.first.click_backup()
        self.business.click_business_center()
        self.myassert.assertEw(self.business.my_collect, '商户中心页面加载失败')
        self.business.click_my_lollect()
        self.myassert.assertEw(('name', goods_name), '收藏商品未添加至我的收藏')
        self.business.click_edit()
        time.sleep(1)
        self.business.click_select_goods()
        time.sleep(1)
        self.shopcar.click_finish()
        self.shopcar.click_ok()
        self.myassert.assertEw(self.order.right_shopcar, '删除收藏的商品失败')
        self.myassert.assertt(self.base.isElementExist(('name', goods_name)), '收藏的商品未成功删除')

    def test_mycollect_shopcaradd(self):
        '''我的收藏页面加入购物车'''
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.shopcar, '购物车页面加载失败')
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '惠民订货页面加载失败')
        self.order.click_goods_img()
        self.myassert.assertEw(self.first.storenum, '商品详情页加载失败')
        goods_name=self.first.get_goods_detail_name()
        self.first.click_collect()
        self.myassert.assertEw(self.first.collected, '收藏商品失败')
        self.first.click_backup()
        self.business.click_business_center()
        self.myassert.assertEw(self.business.my_collect, '商户中心页面加载失败')
        self.business.click_my_lollect()
        self.myassert.assertEw(('name', goods_name), '收藏商品未添加至我的收藏')
        self.first.click_add()
        time.sleep(1)
        num=int(self.first.get_buy_less())
        self.first.click_add()
        self.shopcar.click_ok()
        self.myassert.assertEw(('name', str(num)), '添加购物车失败,购物车角标未增加')
        self.business.click_goods_name()
        self.myassert.assertEw(self.first.collected, '进入详情页失败')
        self.first.click_collected()



    def test_mycollect_goodsdetail(self):
        '''我的收藏页面--商品详情页'''
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '惠民订货页面加载失败')
        self.order.click_goods_img()
        self.myassert.assertEw(self.first.storenum, '商品详情页加载失败')
        goods_name=self.first.get_goods_detail_name()
        self.first.click_collect()
        self.myassert.assertEw(self.first.collected, '收藏商品失败')
        self.first.click_backup()
        self.business.click_business_center()
        self.myassert.assertEw(self.business.my_collect, '商户中心页面加载失败')
        self.business.click_my_lollect()
        self.myassert.assertEw(('name', goods_name), '收藏商品未添加至我的收藏')
        self.business.click_goods_name()
        self.myassert.assertEw(self.first.storenum, '商品详情页加载失败')
        self.first.click_collected()


    def test_prepaidWX(self):
        '''进入账户余额-微信充值页面'''
        self.business.click_account()
        self.myassert.assertEw(self.business.recharge, '账户余额页面加载失败')
        self.business.click_recharge()
        time.sleep(1)
        self.business.sendkeys_credit('1')
        self.shopcar.click_wx_pay()
        self.shopcar.click_pay()
        self.myassert.assertEw(('name', '登录'), '进入微信充值页面失败')




    def test_PrepaidZFB(self):
        '''进入账户余额-支付宝充值页面'''
        self.business.click_account()
        self.myassert.assertEw(self.business.recharge, '账户余额页面加载失败')
        self.business.click_recharge()
        time.sleep(1)
        self.business.sendkeys_credit('1')
        self.business.click_zfb_pay()
        self.shopcar.click_pay()
        self.myassert.assertEw(('name', '登录'), '进入微信充值页面失败')

    def test_prepaid_detail(self):
        '''账户余额-余额明细页面'''
        self.business.click_account()
        self.myassert.assertEw(self.business.recharge, '账户余额页面加载失败')
        self.business.click_yue_detail()
        self.myassert.assertEw(self.business.yue, '余额记录页面加载失败')

    def test_reward_detail(self):
        '''账户余额-奖励明细'''
        self.business.click_account()
        self.myassert.assertEw(self.business.recharge, '账户余额页面加载失败')
        self.business.click_detail_button()
        self.myassert.assertEw(self.business.yue_reward, '奖励明细页面加载失败')
        self.business.click_reward_mouth()
        self.myassert.assertEw(self.business.order_goods, '进入月奖励页面失败')
        self.business.click_reward_year()
        self.myassert.assertEw(self.business.order_goods, '进入年奖励页面失败')

    def test_getcoupon(self):
        '''账户余额——领卷'''
        self.business.click_account()
        self.myassert.assertEw(self.business.recharge, '账户余额页面加载失败')
        self.business.click_getcoupon()
        self.myassert.assertEw(self.first.my_coupon, '余额返卷页面加载失败')



    def test_Coupon(self):
        '''进入优惠卷页面'''
        self.business.click_couppon()
        self.myassert.assertEw(self.first.see_home_coupon, '进入优惠卷页面失败')

    def test_MemberPoints(self):
        '''进入积分查询页面'''
        self.business.click_integral()
        cont = self.driver.contexts
        self.driver.switch_to.context(cont[1])
        self.myassert.assertEw(self.first.myintegral, '我的积分元素不存在')
        self.driver.switch_to.context(cont[0])


    def test_TradingRecord(self):
        '''进入交易记录页面'''
        self.business.click_trading_record()
        self.myassert.assertEw(self.business.history_price, '进入交易记录页面失败')

    def test_MsgCenter(self):
        '''进入消息中心页面'''
        self.business.click_msg_center()
        self.myassert.assertEw(self.first.message_item, '消息中心无消息')
        self.first.click_message_item()
        self.myassert.assertEw(self.first.message_info, '进入消息详情页面失败')


    def test_SettingUp(self):
        '''进入设置页面'''
        self.business.swipeUp(1000)
        self.business.click_set()
        self.myassert.assertEw(self.business.check_update, '进入设置页面失败')
        self.myassert.assertEw(self.business.about_us, '进入设置页面失败')
        self.myassert.assertEw(self.business.log_out, '进入设置页面失败')
        self.business.click_about_us()
        time.sleep(1)
        self.myassert.assertEw(self.business.huipt, '进入关于我们页面失败')


    def test_LogOut(self):
        '''退出登录'''
        self.business.swipeUp(1000)
        self.business.click_set()
        self.myassert.assertEw(self.business.log_out, '进入设置页面失败')
        self.business.click_log_out()
        self.myassert.assertEw(self.first.login_btlogin, '退出登录失败')
        self.public.login()

    def test_JoinStore(self):
        '''合作店铺'''
        # self.current.swipeUp(1000)
        # self.driver.find_element('name', '合作店铺').click()
        # self.assertTrue(self.current.elementwait('name', '下一步'), self.driver, '进入合作店铺页面失败')
        # self.driver.find_element('name', 'A类:7200.00/年').click()
        # self.driver.find_element('name', '下一步').click()
        # self.assertTrue(self.current.elementwait('name', '去支付'), self.driver, '进入选择设备页面失败')
        # self.driver.find_element('name', '去支付').click()
        # self.assertTrue(self.current.elementwait('name', '支付方式:'), self.driver, '进入支付页面失败')
        self.business.swipeUp(1000)
        self.business.click_partner()
        self.myassert.assertEw(self.business.next_step, '进入合作店铺页面失败')
        # self.business.click_A()
        # self.business.click_next_step()
        # self.myassert.assertEw(self.shopcar.pay, '进入选择设备页面失败')
        # self.shopcar.click_pay()
        # self.myassert.assertEw(self.shopcar.yue_pay, '进入支付页面失败')


    def test_ServiceTel(self):
        '''客服电话'''
        self.business.swipeUp(1000)
        self.business.click_phone()
        self.myassert.assertEw(self.business.call, '客服电话未显示')
        self.business.click_cancel()
        self.myassert.assertIsEn(self.business.call, '取消客服电话弹框失败')



if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestBusinessCenter('test_MemberPoints'))
    # suite.addTest(TestBusinessCenter('test_reward_detail'))
    # suite.addTest(TestBusinessCenter('test_getcoupon'))
    # suite.addTest(TestBusinessCenter('test_payOrder'))
    # suite.addTest(TestBusinessCenter('test_CommingImport'))

    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    now = time.strftime('%y-%m-%d_%H_%M_%S')
    filename = 'G:/huipeitongUI/report/' + now + '_result.html'
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestBusinessCenter)
    suite = unittest.TestSuite(suite1)
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            verbosity=2,
            title='惠配通Android App回归测试报告',
            description='惠配通Android App 测试报告'
        )
        runner.run(suite)
