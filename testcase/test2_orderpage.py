__author__ = 'Administrator'
import unittest, HTMLTestRunner, time, BSTestRunner
from appium import webdriver
from po.firstpage import FirstPage
from po.orderpage import Orderpage
from po.shopcarpage import ShopCarPage
from po.business_center_page import Business_center_page
from po.public import Public
from assection.assection import Assect


class TestOrderPage(unittest.TestCase):

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
        # self.current = Mymethod(self.driver)
        # self.huicom = Huicommon(self.driver)
        self.first = FirstPage(self.driver)
        self.shopcar = ShopCarPage(self.driver)
        self.order = Orderpage(self.driver)
        self.business = Business_center_page(self.driver)
        self.public = Public(self.driver)
        self.myassert = Assect(self.driver)

    @classmethod
    def tearDownClass(self):
        '''这个class的所有case测试完成退出driver，切断session,等待3s'''
        self.driver.quit()
        time.sleep(3)

    def setUp(self):
        '''判断首页是否成功启动，成功启动之后再去进入对应模块'''
        self.myassert.assertEw(self.first.first_pge, '首页元素不存在')
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.goods_name, '惠民订货页面加载失败')



    def tearDown(self):
        '''每次测试完成启动app，进入首页'''
        self.driver.start_activity('com.huimin.ordersystem', 'com.huimin.ordersystem.activity.WelcomeActivity')


    def test_CheckLeftView(self):
        '''查看左侧分类列表有无商品'''
        left_list=self.order.get_list_view()
        for i in left_list:
            i.click()
            name=i.get_attribute('name')
            self.myassert.assertEw(self.order.goods_name, name+'列表加载失败')
        element=self.order.get_left_window()
        self.order.swipeOnEmelent(element, 'Up')
        left_list=self.order.get_list_view()[-5:]
        for i in left_list:
            i.click()
            name=i.get_attribute('name')
            self.myassert.assertEw(self.order.goods_name, name+'列表加载失败')


    def test_CheckGoodsDetails(self):
        '''从商品列表进入商品详情页面'''
        left_list=self.order.get_list_view()
        for i in left_list:
            i.click()
            name=i.get_attribute('name')
            self.myassert.assertEw(self.order.goods_name, name+'列表加载失败')
            self.order.click_goods_img()
            self.myassert.assertEw(self.first.storenum, '商品详情页加载失败')
            self.first.click_backup()
            time.sleep(1)
        element=self.order.get_left_window()
        self.order.swipeOnEmelent(element, 'Up')
        left_list=self.order.get_list_view()[-5:]
        for i in left_list:
            i.click()
            name=i.get_attribute('name')
            self.myassert.assertEw(self.order.goods_name, name+'列表加载失败')
            self.order.click_goods_img()
            self.myassert.assertEw(self.first.storenum, '商品详情页加载失败')
            self.first.click_backup()
            time.sleep(1)



    def test_Search(self):
        '''进入搜索商品页面'''
        self.order.click_search_inpu()
        time.sleep(1)
        self.myassert.assertEw(self.order.search_result_text, '进入搜索页面失败')

    def test_SearchGoods(self):
        '''搜索商品-"统一"'''
        self.order.click_search_inpu()
        time.sleep(1)
        self.myassert.assertEw(self.order.search_result_text, '进入搜索页面失败')
        self.order.sendkeys_search_input('统一')
        self.order.click_search_button()
        self.myassert.assertEw(self.order.search_goods_name, '搜索商品加载失败')
        goods_name=self.order.get_search_goods_name()
        self.myassert.assertI('统一', goods_name, '搜索条件与结果不一致')

    def test_SearchGoodsNull(self):
        '''搜索商品—“%@！”'''
        self.order.click_search_inpu()
        time.sleep(1)
        self.myassert.assertEw(self.order.search_result_text, '进入搜索页面失败')
        self.order.sendkeys_search_input('%@!')
        self.order.click_search_button()
        self.myassert.assertEw(self.order.search_button, '搜索商品加载失败')
        self.myassert.assertIsEn(self.order.search_goods_name, '输入特殊字符搜索商品加载失败')


    def test_SearchGoodsDetails(self):
        '''从搜索结果页进入商品详情'''
        self.order.click_search_inpu()
        time.sleep(1)
        self.myassert.assertEw(self.order.search_result_text, '进入搜索页面失败')
        self.order.sendkeys_search_input('统一')
        self.order.click_search_button()
        self.myassert.assertEw(self.order.search_goods_name, '搜索商品加载失败')
        self.order.click_search_goods_name()
        self.myassert.assertEw(self.first.storenum, '商品详情页加载失败')


    def test_GoodsDetailsBackSearch(self):
        '''从搜索商品详情页返回至搜索列表页'''
        self.order.click_search_inpu()
        time.sleep(1)
        self.myassert.assertEw(self.order.search_result_text, '进入搜索页面失败')
        self.order.sendkeys_search_input('统一')
        self.order.click_search_button()
        self.myassert.assertEw(self.order.search_goods_name, '搜索商品加载失败')
        self.order.click_search_goods_name()
        self.myassert.assertEw(self.first.storenum, '商品详情页加载失败')
        self.first.click_backup()
        self.myassert.assertEw(self.order.search_goods_name, '返回搜索列表页失败')


    def test_SearchBackOrderPage(self):
        '''从搜索页面返回至惠民订货页面'''
        self.order.click_search_inpu()
        time.sleep(1)
        self.myassert.assertEw(self.order.search_result_text, '进入搜索页面失败')
        self.order.click_backup()
        self.myassert.assertEw(self.order.hotlist, '返回至惠民订货页面失败')


    def test_SearchGoodsAddShopCar(self):
        '''从搜索结果页加入购物车'''
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.shopcar, '购物车页面加载失败')
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.hmorder, '惠民订货页面加载失败')
        self.order.click_search_inpu()
        time.sleep(1)
        self.myassert.assertEw(self.order.search_result_text, '进入搜索页面失败')
        self.order.sendkeys_search_input('统一')
        self.order.click_search_button()
        self.myassert.assertEw(self.order.search_goods_name, '搜索商品加载失败')
        if self.order.isElementExist(self.first.add):
            self.first.click_add()
            num=self.first.get_buy_less()
            self.first.click_add()
            self.shopcar.click_ok()
            self.myassert.assertEw(('name', num), '添加商品至购物车失败')
            self.order.click_search_backup()
            self.myassert.assertEw(self.order.hmorder, '惠民订货页面加载失败')
            self.shopcar.click_shopcar()
            self.myassert.assertEw(('name', num), '购物车角标未增加')




    def test_SearchGoodsHotBuy(self):
        '''搜索页面——火热购买——商品详情'''
        self.order.click_search_inpu()
        self.myassert.assertEw(self.order.hot_goods_name, '火热购买商品未显示')
        self.order.click_hot_goodsname()
        self.myassert.assertEw(self.first.storenum, '商品详情页加载失败')

    def test_SearchGoodsHotBuySwipe(self):
        '''搜索页面——滑动火热购买商品'''
        self.order.click_search_inpu()
        self.myassert.assertEw(self.order.hot_goods_name, '火热购买商品未显示')
        element=self.order.get_hot_goods_swipe_window()
        name=self.order.get_hot_goodsname()
        self.order.swipeOnEmelent(element, 'Left')
        name2=self.order.get_hot_goodsname()
        self.myassert.assertt(name!=name2, '搜索页面滑动失败')




    def test_ShopCarUpdateGoods(self):
        '''惠民订货页面增加、减少购物车商品数量(+-)'''
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.shopcar, '购物车页面加载失败')
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.hmorder, '惠民订货页面加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.first.click_add()
        time.sleep(1)
        self.first.click_add()
        self.first.click_add()
        self.shopcar.click_ok()
        num_add=len(self.order.find_elements(('name', '2')))
        self.assertEqual(num_add, 2, '增加购物车商品数量失败')
        self.first.click_add()
        time.sleep(1)
        self.first.click_minus()
        self.shopcar.click_ok()
        num_minus=len(self.order.find_elements(('name', '1')))
        self.assertEqual(num_minus, 2, '减少购物车商品数量失败')




    def test_ShopCarAdd(self):
        '''惠民订货页添加商品至购物车(输入数字)'''
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.shopcar, '购物车页面加载失败')
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.hmorder, '惠民订货页面加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.first.click_add()
        time.sleep(1)
        self.first.sendkeys_goods_size('2')
        self.shopcar.click_ok()
        num_add=len(self.order.find_elements(('name', '2')))
        self.assertEqual(num_add, 2, '增加购物车商品数量失败')



    def test_GoodsDetailsPicture(self):
        '''商品详情页——图文详情'''
        self.order.click_goods_img()
        self.myassert.assertEw(self.first.storenum, '商品详情页加载失败')
        self.order.swipeUp()
        self.order.swipeUp()
        self.myassert.assertIsEn(self.first.storenum, '商品详情图文详情页面未显示')


    def test_filter_classify(self):
        '''分类筛选'''
        self.first.click_drink()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_tea_drink()
        self.myassert.assertEw(self.order.goods_name, '筛选页面加载失败')
        name=self.order.get_huimin_goods_name()
        self.myassert.assertt(('茶' in name), '筛选未生效')


    def test_filter_brand(self):
        '''品牌筛选'''
        self.first.click_drink()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_filter_brand()
        time.sleep(1)
        self.order.click_wanglj()
        self.myassert.assertEw(self.order.goods_name, '筛选页面加载失败')
        name=self.order.get_huimin_goods_name()
        self.myassert.assertt(('王老吉' in name), '筛选未生效')

    def test_filter_sort(self):
        '''排序筛选'''
        self.first.click_drink()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        name=self.order.get_huimin_goods_name()
        self.order.click_filter_sort()
        time.sleep(1)
        self.order.click_price_low()
        name1=self.order.get_huimin_goods_name()
        self.myassert.assertt((name != name1), '排序筛选未生效')


    def test_filter_back(self):
        '''点击筛选标签自动收回'''
        self.first.click_drink()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        num=self.order.get_huimin_goodsnum()
        self.order.click_filter_brand()
        time.sleep(1)
        self.order.click_filter_brand()
        time.sleep(1)
        num1=self.order.get_huimin_goodsnum()
        self.myassert.assertt((num1>num), '筛选标签未收回')

    def test_GoodsDetailsCollect(self):
        '''商品详情页收藏商品'''
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
        self.myassert.assertEw(self.first.collected, '进入商品详情页失败')
        self.first.click_collected()
        self.myassert.assertEw(self.first.collect, '取消收藏失败')
        self.first.click_backup()
        self.myassert.assertIsEn(('name', goods_name), '收藏夹不为空')

    @unittest.skip
    def test_GoodsdetailsShopCarAdd(self):
        '''从商品详情页添加商品至加入购物车'''
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.shopcar, '购物车页面加载失败')
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.hmorder, '惠民订货页面加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_goods_img()
        self.myassert.assertEw(self.first.storenum, '商品详情页加载失败')
        num=self.first.get_detail_buy_less()
        self.first.click_shop_car_add()
        time.sleep(1)
        self.first.click_add()
        self.shopcar.click_ok()
        self.first.click_backup()
        self.myassert.assertEw(self.order.hmorder, '惠民订货页面加载失败')
        self.shopcar.click_shopcar()
        self.myassert.assertIsE(('name', num), '购物车角标未增加')


    def test_GoodsDetailsShopCar(self):
        '''从商品详情页进入购物车页面(购物车为空)'''
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.shopcar, '购物车页面加载失败')
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.hmorder, '惠民订货页面加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_goods_img()
        self.myassert.assertEw(self.first.storenum, '商品详情页加载失败')
        self.first.click_detail_shopcar_button()
        self.myassert.assertEw(self.shopcar.hot_goods_name, '购物车页面加载失败')

    @unittest.skip
    def test_GoodsDetailsShopCarAdds(self):
        '''从商品详情页进入购物车页面(购物车不为空)'''
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.shopcar, '购物车页面加载失败')
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.hmorder, '惠民订货页面加载失败')
        self.order.click_wine()
        self.myassert.assertEw(self.order.goods_name, '商品列表加载失败')
        self.order.click_goods_img()
        self.myassert.assertEw(self.first.storenum, '商品详情页加载失败')
        self.first.click_shop_car_add()
        time.sleep(1)
        self.first.click_add()
        self.shopcar.click_ok()
        self.first.click_detail_shopcar_button()
        self.myassert.assertEw(self.shopcar.del_goods, '购物车未添加成功')


    def test_KeepList(self):
        '''进入常购清单页面'''
        self.order.click_buy_list()
        self.myassert.assertEw(self.order.history_name, '进入常购清单列表失败')


    def test_KeepListGoodsdetails(self):
        '''进入常购清单——商品详情页'''
        self.order.click_buy_list()
        self.myassert.assertEw(self.order.history_name, '进入常购清单列表失败')
        self.order.click_history_name()
        self.myassert.assertEw(self.first.shop_car_add, '进入商品详情页失败')

    def test_GoodsdetailBackupKeepList(self):
        '''商品详情页返回至常购清单页面'''
        self.order.click_buy_list()
        self.myassert.assertEw(self.order.history_name, '进入常购清单列表失败')
        self.order.click_history_name()
        self.myassert.assertEw(self.first.shop_car_add, '进入商品详情页失败')
        self.first.click_backup()
        self.myassert.assertEw(self.order.history_name, '进入常购清单列表失败')


    def test_KeepListShopCarAdd(self):
        '''进入常购清单——添加购物车'''
        self.shopcar.click_shopcar()
        self.myassert.assertEw(self.shopcar.shopcar, '购物车页面加载失败')
        self.public.shopCarClear()
        self.order.click_hmorder()
        self.myassert.assertEw(self.order.hmorder, '惠民订货页面加载失败')
        self.order.click_buy_list()
        self.myassert.assertEw(self.order.history_name, '进入常购清单列表失败')
        self.first.click_add()
        time.sleep(1)
        num=self.first.get_buy_less()
        self.first.click_add()
        self.shopcar.click_ok()
        nums=len(self.order.find_elements(('name', num)))
        self.myassert.assertt(nums==1,'添加购物车失败')




if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestOrderPage('test_KeepListShopCarAdd'))
    # suite.addTest(TestOrderPage('test_GoodsDetailsBackSearch'))
    # suite.addTest(TestOrderPage('test_SearchBackOrderPage'))
    # suite.addTest(TestOrderPage('test_SearchGoodsHotBuySwipe'))
    # suite.addTest(TestFirstPage('test_CommingImport'))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    now = time.strftime('%y-%m-%d_%H_%M_%S')
    filename = 'G:/huipeitongUI/report/' + now + '_result.html'
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestOrderPage)
    suite = unittest.TestSuite(suite1)
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            verbosity=2,
            title='惠配通Android App回归测试报告',
            description='惠配通Android App回归测试报告'
        )
        runner.run(suite)
