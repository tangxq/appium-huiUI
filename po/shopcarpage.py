__author__ = 'Administrator'
from po.basepage import Action
class ShopCarPage(Action):

    '''购物车页面'''
    #底部购物车按钮
    shopcar=('name', '购物车')
    #购物车还是空的！赶快去订货吧！
    null_shopcar=('name', '购物车还是空的！赶快去订货吧！')
    #为您推荐商品名称
    hot_goods_name=('id', 'com.huimin.ordersystem:id/subject_item_name')
    #购物车页商品数量统计
    goods_num=('id', 'com.huimin.ordersystem:id/shop_car_total_money')
    #删除商品按钮
    del_goods=('name', '删除商品')
    #清空购物车
    clear_shopcar=('name', '清空购物车')
    #完成按钮
    finish=('name', '完成')
    #购物车页商品名称
    goods_name=('id', 'com.huimin.ordersystem:id/shop_car_item_name')
    '''提交订单，支付选择页'''
    #去结算按钮
    commit=('name', '去结算')
    #去支付按钮
    pay=('name', '去支付')
    #实物卷
    shw_tickets=('name', '实物券')
    #品牌现金卷
    pp_tickets=('name', '品牌现金券')
    #微信活动卷
    wx_tickets=('name', '微信活动券')
    #现金卷
    xj_tickets=('name', '现金券')
    #页面tittle的id
    tittle=('id', 'com.huimin.ordersystem:id/title_center_text')
    #备注输入框
    comment=('id', 'com.huimin.ordersystem:id/good_confirm_remark')
    #支付选择text
    pay_select=('name', '支付选择')
    #余额支付
    yue_pay=('name', '余额支付')
    #支付宝支付
    zfb_pay=('name', '支付宝付款')
    #微信支付
    wx_pay=('name', '微信支付')
    #货到付款
    hdf_pay=('name', '货到付款')
    #确认支付按钮
    makesure_pay=('id', 'com.huimin.ordersystem:id/pay_type_button')
    #提交订单按钮
    commit_order=('name', '提交订单')
    #知道了按钮
    konw=('name', '知道了')
    #确定按钮
    ok=('name', '确定')

    def sendkeys_commment(self,value):
        '''填写备注'''
        self.send_keys(self.comment,value)

    def click_shopcar(self):
        '''点击购物车按钮'''
        self.find_element(self.shopcar).click()

    def click_del_goods(self):
        '''点击删除商品按钮'''
        self.find_element(self.del_goods).click()

    def click_clear_shopcar(self):
        '''点击清空购物车按钮'''
        self.find_element(self.clear_shopcar).click()

    def click_goods_name(self):
        '''点击购物车页面的商品名进入商品详情页'''
        self.find_element(self.goods_name).click()

    def click_commit(self):
        '''点击去结算按钮'''
        self.find_element(self.commit).click()

    def click_pay(self):
        '''点击去支付按钮'''
        self.find_element(self.pay).click()

    def click_yue_pay(self):
        '''点击余额支付'''
        self.find_element(self.yue_pay).click()

    def click_zfb_pay(self):
        '''点击支付宝付款'''
        self.find_element(self.zfb_pay).click()

    def click_wx_pay(self):
        '''点击微信支付'''
        self.find_element(self.wx_pay).click()

    def click_hdf_pay(self):
        '''点击货到付'''
        self.find_element(self.hdf_pay).click()

    def click_makesure_pay(self):
        '''点击确认支付按钮'''
        self.find_element(self.makesure_pay).click()

    def click_commit_order(self):
        '''点击提交订单按钮'''
        self.find_element(self.commit_order).click()

    def click_know(self):
        '''点击知道了按钮'''
        self.find_element(self.konw).click()

    def click_ok(self):
        '''点击确定按钮'''
        self.find_element(self.ok).click()

    def click_finish(self):
        '''点击完成按钮'''
        self.find_element(self.finish).click()

    def click_shw_tickets(self):
        '''点击实物卷'''
        self.find_element(self.shw_tickets).click()

    def click_pp_tickets(self):
        '''点击品牌现金卷'''
        self.find_element(self.pp_tickets).click()

    def click_wx_tickets(self):
        '''点击微信活动卷'''
        self.find_element(self.wx_tickets).click()

    def click_xj_tickets(self):
        '''点击现金卷'''
        self.find_element(self.xj_tickets).click()

    def get_goods_num(self):
        '''得到购物车商品种类'''
        num=self.find_element(self.goods_num).get_attribute('name')[0]
        return num

    def get_tittle_name(self):
        '''得到页面tittle名'''
        name=self.find_element(self.tittle).get_attribute('name')
        return name