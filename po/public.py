__author__ = 'Administrator'
import unittest,time
from po.firstpage import FirstPage
from po.basepage import Action
from po.shopcarpage import ShopCarPage
from po.business_center_page import Business_center_page
from assection.assection import Assect
class Public(unittest.TestCase):

    def __init__(self,driver=None):
        self.driver = driver
        self.mym = Action(self.driver)
        self.first = FirstPage(self.driver)
        self.shopcar = ShopCarPage(self.driver)
        self.business = Business_center_page(self.driver)
        self.myassert = Assect(self.driver)

    def login(self):
        '''登录'''
        self.first.sendkeys_login_name()
        self.first.sendkeys_login_pwd()
        self.first.click_btlogin()
        self.myassert.assertEw(self.first.first_pge, '首页元素不存在')

    def shopCarAdd(self):
        '''添加商品至购物车,当前页面的每个商品都添加一个至购物车'''
        goods_list=self.first.get_goods_list_add()
        t=0#添加商品个数
        for i in goods_list:
            i.click()
            time.sleep(1)
            num=int(self.first.get_buy_less())
            self.first.click_add()
            self.shopcar.click_ok()
            t+=num
            self.myassert.assertEw(('name', str(t)), '购物车角标未增加')


    def shopCarClear(self):
        '''清空购物车'''
        self.mym.is_disappeared(self.shopcar.shopcar)
        if not self.mym.isElementExist(self.shopcar.null_shopcar):
            self.shopcar.click_del_goods()
            self.shopcar.click_clear_shopcar()
            self.shopcar.click_ok()
            self.myassert.assertIsE(self.shopcar.null_shopcar, '清空购物车失败')

    def cancelOrder(self):
        '''取消订单'''
        self.business.click_order_manage()
        self.business.click_unfinish()
        self.myassert.assertEw(self.business.orderNo, '未完成订单页面加载失败')
        # self.myassert.assertIsE(('name', orderid), '未找到要取消的订单号')
        while True:
            order_list=self.business.get_cancel_order()
            if order_list==[]:
                break
            # self.myassert.assertt((len(order_list) != 0), '没有需要取消的订单')
            # for i in range(len(order_list)):
            else:
                order_list[0].click()
                self.myassert.assertEw(self.business.okren, '取消订单失败')
                self.business.click_okren()
                self.myassert.assertEw(self.business.okren, '取消订单失败')
                self.business.click_okren()
                time.sleep(2)
        self.myassert.assertIsEn(self.business.cancel_order, '取消订单失败')




    def addshopcar_banner(self):
        '''添加banner专题页商品至购物车'''
        goods_name=self.first.get_good_name()
        self.first.click_buy_now()
        if self.mym.isElementExist(self.first.buy_less):
            num=self.first.get_buy_less()
        else:
            num='1'
        self.first.click_add()
        self.shopcar.click_ok()
        self.myassert.assertEw(('name', num), '购物车角标未增加')
        self.first.click_shopcar_button()
        self.myassert.assertEw(('name', goods_name), '添加购物车失败')
        self.shopCarClear()
