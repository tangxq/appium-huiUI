__author__ = 'Administrator'
from po.basepage import Action
class FirstPage(Action):

    '''登录页'''
    #登录用户名输入框
    login_name='id', 'com.huimin.ordersystem:id/login_name'
    #登录密码输入框
    login_pwd=('id', 'com.huimin.ordersystem:id/login_pwd')
    #登录按钮
    login_btlogin=('id', 'com.huimin.ordersystem:id/login_btlogin')
    '''首页'''
    #底部首页按钮
    first_pge=('name', '首页')
    #首页搜索框
    first_search=('id', 'com.huimin.ordersystem:id/home_search_layout')
    #积分商城按钮
    integral=('id', 'com.huimin.ordersystem:id/home_integral')
    #消息按钮
    msg_button=('id', 'com.huimin.ordersystem:id/home_xiaoxi_layout')
    #领卷中心
    home_coupon=('name', '领券')
    #充值
    recharge=('name', '充值')
    #饮料
    drink=('name', '饮料')
    #方便速食
    fast_food=('name', '方便速食')
    #消息中心
    home_message=('xpath', '//android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]')
    #新品上市推荐商品id
    new_goods=('id', 'com.huimin.ordersystem:id/good_style1_img')
    #抢购更多商品
    new_good_more=('name',  '抢购更多商品')
    #新品上市页title
    new_good_tittle=('name', '新品上市')
    #厂商周图片
    csz=('xpath', '//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView')
    #专题推荐1
    special1=('xpath', '//android.widget.LinearLayout[2]/android.widget.ImageView')
    #专题推荐2
    special2=('xpath', '//android.widget.LinearLayout[2]/android.widget.ImageView[2]')
    #专题推荐3
    special3=('xpath', '//android.widget.LinearLayout[3]/android.widget.ImageView')
    #专题推荐4
    special4=('xpath', '//android.widget.LinearLayout[3]/android.widget.ImageView[2]')
    #专题推荐5
    special5=('xpath', '//android.widget.LinearLayout[4]/android.widget.ImageView')
    #专题推荐6
    special6=('xpath', '//android.widget.LinearLayout[4]/android.widget.ImageView[2]')
    '''厂商周页'''
    #厂商周页面title
    csz_title=('name', '厂商周')
    #立即购买按钮
    buy_now=('name', '立即购买')
    #进入banner页商品图片
    goods_image=('id', 'com.huimin.ordersystem:id/subject_item_image')
    #进入banner页商品名称id
    goods_name_id=('id', 'com.huimin.ordersystem:id/subject_item_name')
    #购物车快捷按钮
    shopcar_button=('id', 'com.huimin.ordersystem:id/float_shopcar_layout')
    #返回按钮
    backup=('id', 'com.huimin.ordersystem:id/title_left_img')
    '''商品详情页'''
    #商品详情页分类text
    classify=('name', '分   类：')
    #商品详情页库存
    storenum=('id', 'com.huimin.ordersystem:id/good_detail_storenum')
    #商品详情页购物车快捷按钮
    detail_shopcar_button=('id', 'com.huimin.ordersystem:id/include_order_carimg')
    #收藏按钮
    collect=('name', '收藏')
    #已收藏按钮
    collected=('name','已收藏')
    #详情页商品名
    goods_detail_name=('id', 'com.huimin.ordersystem:id/good_detail_name')
    #详情页加入购物车按钮
    shop_car_add=('name', '加入购物车')
    #详情页起定量
    detail_buy_less=('id', 'com.huimin.ordersystem:id/good_detail_minlimit')
    '''购物车弹框'''
    #添加购物车弹框，起定量id
    buy_less=('id', 'com.huimin.ordersystem:id/shop_dialog_order')
    #+按钮
    add=('id', 'com.huimin.ordersystem:id/inclde_goods_add')
    #-按钮
    minus=('id', 'com.huimin.ordersystem:id/inclde_goods_minus')
    #商品数量输入框
    goods_size=('id', 'com.huimin.ordersystem:id/inclde_goods_size')

    '''我的积分页'''
    #我的积分元素
    myintegral=('class name', 'myintegral')
    '''领卷中心页'''
    #余额返卷
    yue_coupon=('name', '余额返券')
    #我的优惠卷
    my_coupon=('name', '我的优惠券')
    #去领卷中心看看
    see_home_coupon=('name', '去领券中心看看')
    #微信活动卷
    wx_coupon=('name', '微信活动券')
    #品牌现金卷
    # pp_coupon=('name', '品牌现金券')
    pp_coupon=('xpath', '/html/body/header/span[1]')
    #已领取
    geted=('name', '已领取')
    #领卷中心——微信活动卷——微信卷金额
    wx_coupon_price=('id', 'com.huimin.ordersystem:id/cash_money')
    '''消息中心页'''
    #商品通知
    good_notice=('name', '商品通知')
    #系统通知
    system_notice=('name', '系统通知')
    #消息列表
    message_item=('id', 'com.huimin.ordersystem:id/message_item_title')
    #消息中心——详细信息
    message_info=('name', '消息详情')
    #系统通知页点击查看按钮
    click_view=('name', '点击查看')






    def sendkeys_login_name(self):
        '''输入用户名'''
        # self.find_element(self.login_name).send_keys('xxxxxxx')
        self.send_keys(self.login_name,'13874973454')

    def sendkeys_login_pwd(self):
        '''输入密码'''
        # self.find_element(self.login_pwd).send_keys('xxxxxxx')
        self.send_keys(self.login_pwd,'111111')

    def sendkeys_goods_size(self, n):
        '''点击商品数量输入框'''
        self.send_keys(self.goods_size, n)

    def click_btlogin(self):
        '''点击登录按钮'''
        self.find_element(self.login_btlogin).click()

    def click_first(self):
        '''点击首页'''
        self.find_element(self.first_pge).click()

    def click_first_search(self):
        '''点击搜索输入框'''
        self.find_element(self.first_search).click()

    def click_msg_button(self):
        '''点击首页消息按钮'''
        self.find_element(self.msg_button).click()

    def click_recharge(self):
        '''点击充值'''
        self.find_element(self.recharge).click()

    def click_drink(self):
        '''点击饮料'''
        self.find_element(self.drink).click()

    def click_fast_food(self):
        '''点击方便食品'''
        self.find_element(self.fast_food).click()

    def click_integral(self):
        '''点击积分商城'''
        self.find_element(self.integral).click()

    def click_home_cupon(self):
        '''点击领卷中心'''
        self.find_element(self.home_coupon).click()

    def click_my_cuppon(self):
        '''点击我的优惠卷'''
        self.find_element(self.my_coupon).click()

    def click_see_home_cuppon(self):
        '''点击去领卷中心看看按钮'''
        self.find_element(self.see_home_coupon).click()

    def click_wx_cuppon(self):
        '''点击微信活动卷'''
        self.find_element(self.wx_coupon).click()

    def click_home_message(self):
        '''点击消息中心'''
        self.find_element(self.home_message).click()

    def click_new_good(self):
        '''点击新品上市推荐的商品进入详情页'''
        self.find_element(self.new_goods).click()

    def click_new_good_more(self):
        '''点击新品上市抢购更多'''
        self.find_element(self.new_good_more).click()

    def click_click_view(self):
        '''点击系统通知-点击查看按钮'''
        self.find_element(self.click_view).click()

    def click_message_item(self):
        '''点击消息列表'''
        self.find_element(self.message_item).click()

    def click_system_notice(self):
        '''点击系统通知标签'''
        self.find_element(self.system_notice).click()

    def click_csz(self):
        '''点击厂商周banner'''
        self.find_element(self.csz).click()

    def click_buy_now(self):
        '''点击立即购买按钮'''
        self.find_element(self.buy_now).click()

    def click_goods_image(self):
        '''点击banner页商品图片进入商品详情'''
        self.find_element(self.goods_image).click()

    def click_add(self):
        '''点击+按钮'''
        self.find_element(self.add).click()

    def click_minus(self):
        '''点击-按钮'''
        self.find_element(self.minus).click()

    def click_shopcar_button(self):
        '''点击购物车快捷按钮'''
        self.find_element(self.shopcar_button).click()

    def click_special1(self):
        '''点击专题推荐1'''
        self.find_element(self.special1).click()

    def click_special2(self):
        '''点击专题推荐2'''
        self.find_element(self.special2).click()

    def click_special3(self):
        '''点击专题推荐3'''
        self.find_element(self.special3).click()

    def click_special4(self):
        '''点击专题推荐4'''
        self.find_element(self.special4).click()

    def click_special5(self):
        '''点击专题推荐5'''
        self.find_element(self.special5).click()

    def click_special6(self):
        '''点击专题推荐6'''
        self.find_element(self.special6).click()

    def click_backup(self):
        '''点击返回按钮'''
        self.find_element(self.backup).click()

    def click_collect(self):
        '''点击收藏按钮'''
        self.find_element(self.collect).click()

    def click_collected(self):
        '''点击已收藏按钮'''
        self.find_element(self.collected).click()

    def click_shop_car_add(self):
        '''点击加入购物车按钮'''
        self.find_element(self.shop_car_add).click()

    def click_detail_shopcar_button(self):
        '''点击详情页购物车快捷按钮'''
        self.find_element(self.detail_shopcar_button).click()

    def get_good_name(self):
        '''得到商品名'''
        name = self.find_element(self.goods_name_id).get_attribute('name')
        return name

    def get_buy_less(self):
        '''得到起定量'''
        num=self.find_element(self.buy_less).get_attribute('name')
        return num

    def get_goods_list(self):
        '''得到商品列表'''
        goods_list=self.find_elements(self.goods_image)
        return goods_list

    def get_goods_detail_name(self):
        '''得到惠民订货页商品名'''
        name=self.find_element(self.goods_detail_name).get_attribute('name')
        return name

    def get_detail_buy_less(self):
        '''得到详情页商品起定量'''
        num=self.find_element(self.detail_buy_less).get_attribute('name')
        return num

    def get_goods_list_add(self):
        '''得到惠民订货页+列表'''
        add_list=self.find_elements(self.add)
        return add_list
