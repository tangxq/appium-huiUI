__author__ = 'Administrator'
import unittest, HTMLTestRunner, time,BSTestRunner
from appium import webdriver
from po.firstpage import FirstPage
from po.orderpage import Orderpage
from po.shopcarpage import ShopCarPage
from po.business_center_page import Business_center_page
from po.public import Public
from po.basepage import Action
from assection.assection import Assect


class TestFirstPage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''设置启动appium所需参数，启动一个appium session'''
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = 'oppo'
        desired_caps['app'] = 'G:/huipeitongUI/package/0926_2033.apk'
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
        self.driver.quit()
        time.sleep(3)

    def setUp(self):
        '''因为启动之后直接进入的是首页所以这里什么也不做'''
        pass

    def tearDown(self):
        '''每次测试完成启动app，进入首页'''
        self.driver.start_activity('com.huimin.ordersystem', 'com.huimin.ordersystem.activity.WelcomeActivity')

    #@unittest.skip
    def test_1Login(self):
        '''使用手机号密码登录'''
        time.sleep(3)
        self.first.swipeLeft()
        self.driver.find_element('name', '立即体验').click()
        time.sleep(1)
        self.first.sendkeys_login_name()
        time.sleep(1)
        self.first.sendkeys_login_pwd()
        time.sleep(1)
        self.first.click_btlogin()
        self.myassert.assertEw(self.first.first_pge, '首页元素不存在')
        #点掉首页的引导页
        self.first.click_first()


    def test_first_search(self):
        '''从首页进入搜索页面'''
        self.myassert.assertEw(self.first.first_pge, '首页加载失败')
        self.first.click_first_search()
        self.myassert.assertEw(self.order.search_result_text, '进入搜索页面失败')

    def test_msg_center(self):
        '''点击消息中心按钮进入消息中心'''
        self.myassert.assertEw(self.first.msg_button, '消息中心无消息')
        self.first.click_msg_button()
        self.myassert.assertEw(self.first.good_notice, '进入消息中心失败')

    def test_first_recharge(self):
        '''从首页进入充值页面'''
        self.myassert.assertEw(self.first.first_pge, '首页加载失败')
        self.first.click_recharge()
        self.myassert.assertEw(self.shopcar.pay, '进入账户充值页面失败')

    def test_drink(self):
        '''从首页进入饮料分类列表'''
        self.myassert.assertEw(self.first.first_pge, '首页加载失败')
        self.first.click_drink()
        self.myassert.assertEw(self.order.goods_name, '进入饮料分类失败')

    def test_fast_food(self):
        '''从首页进入方便速食分类列表'''
        self.myassert.assertEw(self.first.first_pge, '首页加载失败')
        self.first.click_fast_food()
        self.myassert.assertEw(self.order.goods_name, '进入方便速食分类失败')

    def test_RollCenterH5(self):
        '''查看领卷中心--品牌现金卷'''
        self.myassert.assertEw(self.first.first_pge, '首页加载失败')
        self.first.click_home_cupon()
        self.myassert.assertEw(self.first.my_coupon, '领卷中心页面加载失败')
        cont = self.driver.contexts
        self.driver.switch_to.context(cont[1])
        self.myassert.assertEw(self.first.pp_coupon, '领卷中心-品牌现金卷页加载失败')
        self.driver.switch_to.context(cont[0])


    def test_CommingRollCenter(self):
        '''进入领卷中心--我的优惠卷页面'''
        self.myassert.assertEw(self.first.home_coupon, '首页加载失败')
        self.first.click_home_cupon()
        self.myassert.assertEw(self.first.my_coupon, '领卷中心页面加载失败')
        self.first.click_my_cuppon()
        self.myassert.assertEw(self.first.see_home_coupon, '优惠卷页面加载失败')
        self.first.click_see_home_cuppon()
        self.myassert.assertEw(self.first.my_coupon, '领卷中心页面加载失败')




    # def test_CommingRollCenterWx(self):
    #     '''进入领卷中心--微信活动卷页面'''
    #     self.myassert.assertEw(self.first.first_pge, '首页加载失败')
    #     self.first.click_home_cupon()
    #     self.myassert.assertEw(self.first.yue_coupon, '余额返卷页面加载失败')
    #     self.first.click_wx_cuppon()
    #     self.myassert.assertEw(self.first.wx_coupon_price, '微信活动页面没有卷')
    #     self.first.click_my_cuppon()
    #     self.myassert.assertEw(self.first.see_home_coupon, '优惠卷页面加载失败')
    #     self.first.click_see_home_cuppon()
    #     self.myassert.assertEw(self.first.yue_coupon, '余额返卷页面加载失败')




    def test_CommingMsgCenter(self):
        '''进入消息中心页面-商品通知'''
        self.myassert.assertEw(self.first.first_pge, '首页元素不存在')
        self.first.click_home_message()
        self.myassert.assertEw(self.first.good_notice, '进入消息中心失败')
        if self.base.isElementExist(self.first.message_item):
            self.first.click_message_item()
            self.myassert.assertEw(self.first.message_info, '进入商品通知-消息详情页面失败')

    def test_CommingMsgCenter_sysnotice(self):
        '''进入消息中心页面-系统通知'''
        self.myassert.assertEw(self.first.first_pge, '首页元素不存在')
        self.first.click_home_message()
        self.myassert.assertEw(self.first.good_notice, '进入消息中心失败')
        self.first.click_system_notice()
        self.myassert.assertEw(self.first.good_notice, '系统通知页面加载失败')
        if self.base.isElementExist(self.first.message_item):
            self.first.click_click_view()
            self.myassert.assertEw(self.first.message_info, '进入系统通知-消息详情页面失败')

    def test_newgood_detail(self):
        '''从新品上市推荐商品中进入商品详情'''
        self.myassert.assertEw(self.first.first_pge, '首页元素不存在')
        self.first.click_new_good()
        self.myassert.assertEw(self.first.classify, '厂商周商品详情加载失败')

    def test_new_good_more(self):
        '''新品上市-查看更多'''
        self.myassert.assertEw(self.first.first_pge, '首页元素不存在')
        self.first.click_new_good_more()
        self.myassert.assertEw(self.first.new_good_tittle, '进入新品上市-查看更多失败')
        self.myassert.assertEw(self.first.goods_name_id, '新品上市页面无商品')
        self.first.click_goods_image()
        self.myassert.assertEw(self.first.classify, '厂商周商品详情加载失败')


    # def test_CommingHuiminDays(self):
    #     '''进入厂商周bannner'''
    #     self.myassert.assertEw(self.first.first_pge, '首页元素不存在')
    #     self.myassert.assertEw(self.first.csz, '无厂商周banner')
    #     self.first.click_csz()
    #     self.myassert.assertEw(self.first.csz_title, '进入厂商周页面失败')
    #     self.myassert.assertEw(self.first.buy_now, '厂商周列表无商品')
    #     self.first.click_goods_image()
    #     self.myassert.assertEw(self.first.classify, '厂商周商品详情加载失败')
    #
    #
    # def test_AddShopCarCsz(self):
    #     '''添加厂商周商品至购物车'''
    #     self.myassert.assertEw(self.first.first_pge, '首页元素不存在')
    #     self.shopcar.click_shopcar()
    #     self.public.shopCarClear()
    #     self.first.click_first()
    #     self.myassert.assertEw(self.first.csz, '惠民日图片加载失败')
    #     self.first.click_csz()
    #     self.myassert.assertEw(self.first.csz_title, '进入厂商周页面失败')
    #     self.myassert.assertEw(self.first.buy_now, '厂商周列表无商品')
    #     self.public.addshopcar_banner()
    #
    #
    # def test_CollectCsz(self):
    #     '''收藏厂商周商品'''
    #     self.myassert.assertEw(self.first.first_pge, '首页加载失败')
    #     self.myassert.assertEw(self.first.csz, '无厂商周banner')
    #     self.first.click_csz()
    #     self.myassert.assertEw(self.first.csz_title, '进入厂商周页面失败')
    #     self.myassert.assertEw(self.first.buy_now, '厂商周列表无商品')
    #     goods_name=self.first.get_good_name()
    #     self.first.click_goods_image()
    #     self.myassert.assertEw(self.first.classify, '厂商周商品详情页加载失败')
    #     self.first.click_collect()
    #     self.myassert.assertEw(self.first.collected, '收藏商品失败')
    #     self.first.click_backup()
    #     self.first.click_backup()
    #     self.business.click_business_center()
    #     self.myassert.assertEw(self.business.my_collect, '商户中心页面加载失败')
    #     self.business.click_my_lollect()
    #     self.myassert.assertEw(('name', goods_name), '收藏商品未添加至我的收藏')
    #     self.business.click_goods_name()
    #     self.myassert.assertEw(self.first.collected, '进入商品详情页失败')
    #     self.first.click_collected()
    #     self.myassert.assertEw(self.first.collect, '取消收藏失败')
    #     self.first.click_backup()
    #     self.myassert.assertEw(self.business.my_collect, '收藏夹不为空')
    #
    # def test_CommingRecommended(self):
    #     '''进入首页专题推荐商品列表'''
    #     self.myassert.assertEw(self.first.csz, '惠民日图片加载失败')
    #     self.first.swipeUp(2000)
    #     self.first.click_special1()
    #     self.myassert.assertEw(self.first.buy_now, '1专题推荐商品列表无商品')
    #     self.first.get_goods_list()[3].click()
    #     self.myassert.assertEw(self.first.classify, '首页专题推荐商品详情页失败')
    #     self.first.click_backup()
    #     self.first.click_backup()
    #     self.first.click_special2()
    #     self.myassert.assertEw(self.first.buy_now, '2专题推荐商品列表无商品')
    #     self.first.click_backup()
    #     self.first.click_special3()
    #     self.myassert.assertEw(self.first.buy_now, '3专题推荐商品列表无商品')
    #     self.first.click_backup()
    #     self.first.click_special4()
    #     self.myassert.assertEw(self.first.buy_now, '4专题推荐商品列表无商品')
    #     self.first.click_backup()
    #     self.first.click_special5()
    #     self.myassert.assertEw(self.first.buy_now, '5专题推荐商品列表无商品')
    #     self.first.click_backup()
    #     self.first.click_special6()
    #     self.myassert.assertEw(self.first.buy_now, '6专题推荐商品列表无商品')
    #
    # def test_AddShopCarZt(self):
    #     '''添加专题推荐商品至购物车'''
    #     self.myassert.assertEw(self.first.csz, '惠民日图片加载失败')
    #     self.shopcar.click_shopcar()
    #     self.public.shopCarClear()
    #     self.first.click_first()
    #     self.myassert.assertEw(self.first.csz, '惠民日图片加载失败')
    #     self.first.swipeUp(2000)
    #     self.first.click_special2()
    #     self.myassert.assertEw(self.first.buy_now, '推荐商品列表无商品')
    #     self.public.addshopcar_banner()


    # def test_CommingTaoCan(self):
    #     '''进入套餐列表页面'''
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.current.swipeUp(510)
    #     # self.current.swipeUp()
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element('xpath', '//android.widget.LinearLayout[2]/android.widget.ImageView').click()
    #     self.assertTrue(self.current.elementwait('name', '套餐专区'), self.driver, '进入套餐列表页面失败')
    #     self.assertTrue(self.current.elementwait('name', '立即购买'), self.driver, '套餐列表页面无商品')
    #     self.driver.find_element('id', 'com.huimin.ordersystem:id/subject_item_image').click()
    #     self.assertTrue(self.current.elementwait('id', 'com.huimin.ordersystem:id/taocan_name'), self.driver, '套餐商品详情页加载失败')
    #
    # def test_AddShopCarTc(self):
    #     '''添加套餐至购物车'''
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.driver.find_element('name', '购物车').click()
    #     self.huicom.shopCarClear()
    #     self.driver.find_element('name','首页').click()
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.current.swipeUp(510)
    #     # self.current.swipeUp()
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element('xpath', '//android.widget.LinearLayout[2]/android.widget.ImageView').click()
    #     self.assertTrue(self.current.elementwait('name', '套餐专区'), self.driver, '进入套餐列表页面失败')
    #     self.assertTrue(self.current.elementwait('name', '立即购买'), self.driver, '套餐列表页面无商品')
    #     self.current.swipeUp()
    #     self.driver.find_element('name', '立即购买').click()
    #     goods_name = self.driver.find_element('id', 'com.huimin.ordersystem:id/shop_history_name').get_attribute('name')
    #     # num=self.driver.find_element('id', 'com.huimin.ordersystem:id/shop_dialog_Purchase').get_attribute('name')
    #     self.driver.find_element('id', 'com.huimin.ordersystem:id/inclde_goods_add').click()
    #     self.driver.find_element('name', '确定').click()
    #     self.assertTrue(self.current.elementwait('name', '1'), self.driver, '购物车角标未增加')
    #     self.driver.find_element('id', 'com.huimin.ordersystem:id/float_shopcar_layout').click()
    #     self.assertTrue(self.current.elementwait('name', goods_name), self.driver, '添加购物车失败')
    #     self.huicom.shopCarClear()
    #
    # def test_CommingSpecial(self):
    #     '''进入特价专区列表'''
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.current.swipeUp(510)
    #     # self.current.swipeUp()
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element('xpath', '//android.widget.LinearLayout[3]/android.widget.ImageView').click()
    #     self.assertTrue(self.current.elementwait('name', '特价专区'), self.driver, '进入特价专区页面失败')
    #     self.assertTrue(self.current.elementwait('name', '立即购买'), self.driver, '特价专区页面无商品')
    #     self.driver.find_element('id', 'com.huimin.ordersystem:id/subject_item_image').click()
    #     self.assertTrue(self.current.elementwait('id', 'com.huimin.ordersystem:id/taocan_name'), self.driver, '特价专区商品详情页加载失败')
    #
    # def test_AddShopCarTj(self):
    #     '''添加特价商品至购物车'''
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.driver.find_element('name', '购物车').click()
    #     self.huicom.shopCarClear()
    #     self.driver.find_element('name','首页').click()
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.current.swipeUp(510)
    #     # self.current.swipeUp()
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element('xpath', '//android.widget.LinearLayout[3]/android.widget.ImageView').click()
    #     self.assertTrue(self.current.elementwait('name', '特价专区'), self.driver, '进入特价专区页面失败')
    #     self.assertTrue(self.current.elementwait('name', '立即购买'), self.driver, '特价专区页面无商品')
    #     self.huicom.addshopcar_banner()
    #
    # def test_CommingImport(self):
    #     '''进入进口馆列表'''
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.current.swipeUp(510)
    #     # self.current.swipeUp()
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element('xpath', '//android.widget.LinearLayout[4]/android.widget.ImageView').click()
    #     self.assertTrue(self.current.elementwait('name', '进口馆'), self.driver, '进入进口馆专区页面失败')
    #     self.assertTrue(self.current.elementwait('name', '立即购买'), self.driver, '进口馆页面无商品')
    #     self.driver.find_element('id', 'com.huimin.ordersystem:id/subject_item_image').click()
    #     self.assertTrue(self.current.elementwait('id', 'com.huimin.ordersystem:id/good_detail_name'),self.driver, '进口馆商品详情页加载失败')
    #
    #
    # def test_AddShopCarJk(self):
    #     '''添加进口馆商品至购物车'''
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.driver.find_element('name', '购物车').click()
    #     self.huicom.shopCarClear()
    #     self.driver.find_element('name','首页').click()
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.current.swipeUp(450)
    #     # self.current.swipeUp()
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element('xpath', '//android.widget.LinearLayout[4]/android.widget.ImageView').click()
    #     self.assertTrue(self.current.elementwait('name', '进口馆'), self.driver, '进入进口馆专区页面失败')
    #     self.assertTrue(self.current.elementwait('name', '立即购买'), self.driver, '进口馆页面无商品')
    #     self.huicom.addshopcar_banner()
    #
    # def test_Purchase(self):
    #     '''套餐——限购数量验证'''
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.driver.find_element('name', '购物车').click()
    #     self.huicom.shopCarClear()
    #     self.driver.find_element('name','首页').click()
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.current.swipeUp(510)
    #     # self.current.swipeUp()
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element('xpath', '//android.widget.LinearLayout[2]/android.widget.ImageView').click()
    #     self.assertTrue(self.current.elementwait('name', '套餐专区'), self.driver, '进入套餐列表页面失败')
    #     self.assertTrue(self.current.elementwait('name', '立即购买'), self.driver, '套餐列表页面无商品')
    #     self.driver.find_element('name', '立即购买').click()
    #     num = self.driver.find_element('id', 'com.huimin.ordersystem:id/shop_dialog_Purchase').get_attribute('name')
    #     for i in range(int(num) + 1):
    #         self.driver.find_element('id', 'com.huimin.ordersystem:id/inclde_goods_add').click()
    #     nums = self.driver.find_element('id', 'com.huimin.ordersystem:id/inclde_goods_size').get_attribute('name')
    #     # self.assertEqual(num, nums, '添加商品数量超过限购数量')
    #     self.assertTrue(num==nums,self.driver,'添加商品数量超过限购数量')
    #
    # def test_NoEnough(self):
    #     '''套餐—未满足满够金额订购'''
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.driver.find_element('name', '购物车').click()
    #     self.huicom.shopCarClear()
    #     self.driver.find_element('name','首页').click()
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.current.swipeUp(510)
    #     # self.current.swipeUp()
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element('xpath', '//android.widget.LinearLayout[2]/android.widget.ImageView').click()
    #     self.assertTrue(self.current.elementwait('name', '套餐专区'), self.driver, '进入套餐列表页面失败')
    #     self.assertTrue(self.current.elementwait('name', '立即购买'), self.driver, '套餐列表页面无商品')
    #     if self.current.isElementExist('name', '满购'):
    #         self.driver.find_element('name', '立即购买').click()
    #         num = self.driver.find_element('id', 'com.huimin.ordersystem:id/shop_dialog_Purchase').get_attribute('name')
    #         self.driver.find_element('id', 'com.huimin.ordersystem:id/inclde_goods_add').click()
    #         self.driver.find_element('name', '确定').click()
    #         self.assertTrue(self.current.elementwait('name', '立即购买'), self.driver, '套餐专区页面加载失败')
    #         self.assertTrue(not self.current.isElementExist('name', num), self.driver, '未满足满够金额添加至购物车')
    #
    # def test_Enough(self):
    #     '''套餐—满足满够金额订购'''
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.driver.find_element('name', '购物车').click()
    #     self.huicom.shopCarClear()
    #     self.driver.find_element('name','首页').click()
    #     self.assertTrue(self.current.elementwait('xpath',
    #                                              '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView'), self.driver,
    #                     '惠民日图片加载失败')
    #     self.current.swipeUp(510)
    #     # self.current.swipeUp()
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element('xpath', '//android.widget.LinearLayout[2]/android.widget.ImageView').click()
    #     self.assertTrue(self.current.elementwait('name', '套餐专区'), self.driver, '进入套餐列表页面失败')
    #     self.assertTrue(self.current.elementwait('name', '立即购买'), self.driver, '套餐列表页面无商品')
    #     if self.current.isElementExist('name', '满购'):
    #         self.driver.find_element('name', '立即购买').click()
    #         price = self.driver.find_element('id', 'com.huimin.ordersystem:id/shop_dialog_price').get_attribute('name')
    #         price = int(price[1:])
    #         self.driver.find_element('id', 'com.huimin.ordersystem:id/cecle').click()
    #         num = 0
    #         while True:
    #             self.current.swipeUp(1000)
    #             goods_list = self.driver.find_elements('name', '立即购买')
    #             for i in goods_list:
    #                 i.click()
    #                 if self.current.isElementExist('id', 'com.huimin.ordersystem:id/shop_dialog_Purchase'):
    #                     num1 = self.driver.find_element('id',
    #                                                     'com.huimin.ordersystem:id/shop_dialog_Purchase').get_attribute(
    #                         'name')
    #                     self.driver.find_element('id', 'com.huimin.ordersystem:id/inclde_goods_size').send_keys(num1)
    #                 else:
    #                     pri = self.driver.find_element('id',
    #                                                    'com.huimin.ordersystem:id/shop_history_price').get_attribute(
    #                         'name')[1:]
    #                     num1 = (1200 // int(pri)) + 1
    #                     self.driver.find_element('id', 'com.huimin.ordersystem:id/inclde_goods_size').send_keys(
    #                         str(num1))
    #                 num += int(num1)
    #                 self.driver.find_element('name', '确定').click()
    #                 self.assertTrue(self.current.elementwait('name', '立即购买'), self.driver, '套餐专区页面加载失败')
    #                 self.assertTrue(self.current.isElementExist('name', str(num)), self.driver, '添加购物车失败')
    #                 self.driver.find_element('id', 'com.huimin.ordersystem:id/float_shopcar_layout').click()
    #                 self.assertTrue(self.current.elementwait('name', '去结算'), self.driver, '购物车页面加载失败')
    #                 price1 = \
    #                 self.driver.find_element('id', 'com.huimin.ordersystem:id/shop_car_total_money').get_attribute(
    #                     'name').split('品')[1][:-1]
    #                 self.driver.find_element('id', 'com.huimin.ordersystem:id/title_left_img').click()
    #                 if float(price1) >= price:
    #                     break
    #             if float(price1) >= price:
    #                 break
    #         self.current.swipeDown()
    #         self.current.swipeDown()
    #         self.assertTrue(self.current.elementwait('name', '立即购买'), self.driver, '套餐页面刷新失败')
    #         self.driver.find_element('name', '立即购买').click()
    #         self.driver.find_element('id', 'com.huimin.ordersystem:id/inclde_goods_add').click()
    #         self.driver.find_element('name', '确定').click()
    #         self.assertTrue(self.current.elementwait('name', '立即购买'),self.driver, '套餐页面加载失败')
    #         self.assertTrue(self.current.isElementExist('name', str(num + 1)), self.driver, '满足满够金额添加购物车失败')
    #         self.driver.find_element('id', 'com.huimin.ordersystem:id/float_shopcar_layout').click()
    #         self.huicom.shopCarClear()


if __name__ == '__main__':
    # unittest.main()
    # suite.addTest(TestFirstPage('test_Enough'))
    # suite.addTest(TestFirstPage('test_AddShopCarJk'))
    # suite.addTest(TestFirstPage('test_CommingImport'))

    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    now = time.strftime('%y-%m-%d_%H_%M_%S')
    filename = 'G:/huipeitongUI/report/' + now + '_result.html'
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestFirstPage)
    # suite = unittest.TestSuite(suite1)
    suite = unittest.TestSuite()
    suite.addTest(TestFirstPage('test_1Login'))
    suite.addTest(TestFirstPage('test_first_search'))
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                verbosity=2,
                title='惠配通Android App测试报告',
                description='惠配通Android App测试报告'
            )
        runner.run(suite)
