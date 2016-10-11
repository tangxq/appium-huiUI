__author__ = 'Administrator'
import unittest, HTMLTestRunner, time, BSTestRunner
from appium import webdriver
from po.firstpage import FirstPage
from po.orderpage import Orderpage
from po.shopcarpage import ShopCarPage
from po.business_center_page import Business_center_page
from po.public import Public
from assection.assection import Assect


class TestShoppingCar(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        '''设置启动appium所需参数，启动一个appium session'''
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = 'oppo'
        #desired_caps['app'] = 'G:/huipeitongUI/package/'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        #desired_caps['noSign'] = 'true'
        desired_caps['appPackage'] = 'com.huimin.ordersystem'
        desired_caps['appActivity'] = 'com.huimin.ordersystem.activity.WelcomeActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        self.first = FirstPage(self.driver)
        self.shopcar = ShopCarPage(self.driver)
        self.order = Orderpage(self.driver)
        self.business = Business_center_page(self.driver)
        self.public = Public(self.driver)
        self.myassert = Assect(self.driver)

    @classmethod
    def tearDownClass(self):
        '''这个class的所有case测试完成退出driver，等待3s,切断session'''
        self.driver.quit()
        time.sleep(3)


    def setUp(self):
        '''判断首页是否成功启动，成功启动之后再去进入对应模块'''
        self.myassert.assertEw(self.first.first_pge, '首页元素不存在')
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.shopcar, '进入购物车页面失败')


    def tearDown(self):
        '''每次测试完成启动app，进入首页'''
        self.driver.start_activity('com.huimin.ordersystem', 'com.huimin.ordersystem.activity.WelcomeActivity')


    def test_shopGoodsDelone(self):
        ''''-'号删除商品'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.first.click_add()
        time.sleep(1)
        self.first.click_add()
        self.shopcar.click_ok()
        self.myassert.assertEw(self.order.hmorder, '添加商品至购物车失败')
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.shopcar, '购物车页面加载失败')
        self.first.click_minus()
        self.myassert.assertEw(self.shopcar.ok, '未弹出删除商品提示框')
        self.shopcar.click_ok()
        self.myassert.assertEw(self.shopcar.null_shopcar, '商品未被删除')

    def test_shopGoodsDel(self):
        '''删除商品'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name,'商品列表加载失败')
        self.public.shopCarAdd()
        self.shopcar.click_shopcar()
        num=self.shopcar.get_goods_num()
        self.shopcar.click_del_goods()
        self.shopcar.click_del_goods()
        self.shopcar.click_ok()
        self.shopcar.click_finish()
        self.shopcar.is_disappeared(self.shopcar.del_goods)
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.hmorder, '惠民订货页面加载失败')
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车页面加载失败')
        delnum=self.shopcar.get_goods_num()
        self.myassert.assertt(int(num)==int(delnum)+1, '删除商品失败')


    def test_shopCarUpdate(self):
        '''增加、减少购物车中商品数量'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name,'商品列表加载失败')
        self.first.click_add()
        time.sleep(1)
        self.first.click_add()
        self.first.click_add()
        self.shopcar.click_ok()
        self.myassert.assertEw(self.shopcar.shopcar, '添加购物车失败')
        nums=len(self.shopcar.find_elements(('name', '2')))
        self.myassert.assertt(nums==2, '添加购物车失败')
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.shopcar, '购物车加载失败')
        self.first.click_add()
        self.myassert.assertIsE(('name', '3'), '购物车角标未增加')
        self.first.click_minus()
        self.myassert.assertIsE(('name', '2'), '购物车角标未增加')




    def test_payOrder(self):
        '''余额支付订单'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name,'商品列表加载失败')
        self.public.shopCarAdd()
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车加载失败')
        self.shopcar.click_commit()
        self.myassert.assertEw(self.shopcar.pay, '提交订单页面加载失败')
        self.shopcar.click_pay()
        time.sleep(1)
        self.myassert.assertIsE(self.shopcar.pay_select, '进入支付选择页面失败')
        self.shopcar.click_yue_pay()
        self.shopcar.click_makesure_pay()
        self.first.sendkeys_login_pwd()
        self.shopcar.click_commit_order()
        self.myassert.assertEw(self.shopcar.konw, '使用余额支付失败')
        self.shopcar.click_know()
        self.myassert.assertEw(self.shopcar.null_shopcar, '支付后购物车未清空')
        self.business.click_business_center()
        self.myassert.assertEw(self.business.order_manage, '商户中心页面加载失败')
        self.public.cancelOrder()




    def test_payOrderzfb(self):
        '''进入支付宝支付页面'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name,'商品列表加载失败')
        self.public.shopCarAdd()
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车加载失败')
        self.shopcar.click_commit()
        self.myassert.assertEw(self.shopcar.pay, '提交订单页面加载失败')
        self.shopcar.click_pay()
        time.sleep(1)
        self.myassert.assertIsE(self.shopcar.pay_select, '进入支付选择页面失败')
        self.shopcar.click_zfb_pay()
        self.shopcar.click_makesure_pay()
        self.myassert.assertEw(('name', '登录'), '进入支付宝页面失败')



    def test_payOrderwx(self):
        '''进入微信支付页面'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name,'商品列表加载失败')
        self.public.shopCarAdd()
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车加载失败')
        self.shopcar.click_commit()
        self.myassert.assertEw(self.shopcar.pay, '提交订单页面加载失败')
        self.shopcar.click_pay()
        time.sleep(1)
        self.myassert.assertIsE(self.shopcar.pay_select, '进入支付选择页面失败')
        self.shopcar.click_wx_pay()
        self.shopcar.click_makesure_pay()
        self.myassert.assertEw(('name', '登录'), '进入支付宝页面失败')


    def test_payOrderhdf(self):
        '''货到付款'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name,'商品列表加载失败')
        self.public.shopCarAdd()
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车加载失败')
        self.shopcar.click_commit()
        self.myassert.assertEw(self.shopcar.pay, '提交订单页面加载失败')
        self.shopcar.click_pay()
        time.sleep(1)
        self.myassert.assertIsE(self.shopcar.pay_select, '进入支付选择页面失败')
        self.shopcar.click_hdf_pay()
        self.shopcar.click_makesure_pay()
        self.myassert.assertEw(self.shopcar.konw, '货到付失败')
        self.shopcar.click_know()
        self.myassert.assertEw(self.shopcar.null_shopcar, '支付后购物车未清空')
        self.business.click_business_center()
        self.myassert.assertEw(self.business.order_manage, '商户中心页面加载失败')
        self.public.cancelOrder()


    def test_shopCarGoodsdetails(self):
        '''从购物车页面进入商品详情页'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.public.shopCarAdd()
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车加载失败')
        self.shopcar.click_goods_name()
        self.myassert.assertEw(self.first.shop_car_add, '进入商品详情页失败')

    def test_shopCarRecommend(self):
        '''进入购物车推荐商品详情页'''
        self.public.shopCarClear()
        self.first.click_goods_image()
        self.myassert.assertEw(self.first.shop_car_add, '进入商品详情页失败')

    def test_CommitOrder_shw_tickets(self):
        '''提交订单页面点击实物卷'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name,'商品列表加载失败')
        self.public.shopCarAdd()
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车加载失败')
        self.shopcar.click_commit()
        self.myassert.assertEw(self.shopcar.pay, '提交订单页面加载失败')
        self.shopcar.click_shw_tickets()
        self.myassert.assertEw(self.shopcar.tittle, '实物卷页面加载失败')
        name=self.shopcar.get_tittle_name()
        self.myassert.assertt(name=='实物券', '进入实物卷页面失败')
        self.first.click_backup()
        self.myassert.assertEw(self.shopcar.pay, '实物卷返回至提交订单页面失败')

    def test_CommitOrder_pp_tickets(self):
        '''提交订单页面点击品牌现金卷'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name,'商品列表加载失败')
        self.public.shopCarAdd()
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车加载失败')
        self.shopcar.click_commit()
        self.myassert.assertEw(self.shopcar.pay, '提交订单页面加载失败')
        self.shopcar.click_pp_tickets()
        self.myassert.assertEw(self.shopcar.tittle, '品牌现金卷页面加载失败')
        name=self.shopcar.get_tittle_name()
        self.myassert.assertt(name=='品牌现金券', '进入品牌现金卷页面失败')
        self.first.click_backup()
        self.myassert.assertEw(self.shopcar.pay, '品牌现金卷返回至提交订单页面失败')

    def test_CommitOrder_wx_tickets(self):
        '''提交订单页面点击品牌现金卷'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name,'商品列表加载失败')
        self.public.shopCarAdd()
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车加载失败')
        self.shopcar.click_commit()
        self.myassert.assertEw(self.shopcar.pay, '提交订单页面加载失败')
        self.shopcar.swipeUp()
        self.shopcar.click_wx_tickets()
        self.myassert.assertEw(self.shopcar.tittle, '微信活动卷页面加载失败')
        name=self.shopcar.get_tittle_name()
        self.myassert.assertt(name=='微信活动券', '进入微信活动卷页面失败')
        self.first.click_backup()
        self.myassert.assertEw(self.shopcar.pay, '微信活动卷返回至提交订单页面失败')

    def test_CommitOrder_xj_tickets(self):
        '''提交订单页面点击品牌现金卷'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name,'商品列表加载失败')
        self.public.shopCarAdd()
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车加载失败')
        self.shopcar.click_commit()
        self.myassert.assertEw(self.shopcar.pay, '提交订单页面加载失败')
        self.shopcar.swipeUp()
        self.shopcar.click_xj_tickets()
        self.myassert.assertEw(self.shopcar.tittle, '现金卷页面加载失败')
        name=self.shopcar.get_tittle_name()
        self.myassert.assertt(name=='现金券', '进入现金卷页面失败')
        self.first.click_backup()
        self.myassert.assertEw(self.shopcar.pay, '现金卷返回至提交订单页面失败')

    def test_payorder_comment(self):
        '''提交订单页面填写备注支付'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name,'商品列表加载失败')
        self.public.shopCarAdd()
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车加载失败')
        self.shopcar.click_commit()
        self.myassert.assertEw(self.shopcar.pay, '提交订单页面加载失败')
        self.shopcar.swipeUp()
        self.shopcar.sendkeys_commment('一路向北')
        self.shopcar.click_pay()
        time.sleep(1)
        self.myassert.assertIsE(self.shopcar.pay_select, '进入支付选择页面失败')
        self.shopcar.click_hdf_pay()
        self.shopcar.click_makesure_pay()
        self.myassert.assertEw(self.shopcar.konw, '货到付失败')
        self.shopcar.click_know()
        self.myassert.assertEw(self.shopcar.null_shopcar, '支付后购物车未清空')
        self.business.click_business_center()
        self.myassert.assertEw(self.business.order_manage, '商户中心页面加载失败')
        self.public.cancelOrder()

    def test_commitOrder_backup_shopcar(self):
        '''提交订单页面返回至购物车页面'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name,'商品列表加载失败')
        self.public.shopCarAdd()
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车加载失败')
        self.shopcar.click_commit()
        self.myassert.assertEw(self.shopcar.pay, '提交订单页面加载失败')
        self.first.click_backup()
        self.myassert.assertEw(self.shopcar.shopcar, '返回购物车页面失败')


    def test_payorder_backup_shopcar(self):
        '''支付选择页面返回至购物车页面'''
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name,'商品列表加载失败')
        self.public.shopCarAdd()
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车加载失败')
        self.shopcar.click_commit()
        self.myassert.assertEw(self.shopcar.pay, '提交订单页面加载失败')
        self.shopcar.click_pay()
        time.sleep(1)
        self.myassert.assertIsE(self.shopcar.pay_select, '进入支付选择页面失败')
        self.first.click_backup()
        self.myassert.assertEw(self.shopcar.shopcar, '返回购物车页面失败')


if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestShoppingCar('test_shopGoodsDelone'))
    # suite.addTest(TestShoppingCar('test_payorder_backup_shopcar'))
    # suite.addTest(TestShoppingCar('test_CommitOrder_wx_tickets'))
    # suite.addTest(TestShoppingCar('test_CommitOrder_xj_tickets'))
    # suite.addTest(TestShoppingCar('test_payorder_comment'))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    now = time.strftime('%y-%m-%d_%H_%M_%S')
    filename = 'G:/huipeitongUI/report/' + now + '_result.html'
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestShoppingCar)
    suite = unittest.TestSuite(suite1)
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            verbosity=2,
            title='惠配通Android App回归测试报告',
            description='惠配通Android App回归测试报告'
        )
        runner.run(suite)




