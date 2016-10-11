__author__ = 'Administrator'
from po.basepage import Action
class Business_center_page(Action):

    '''商户中心页'''
    #商户中心按钮
    business_center=('name', '商户中心')
    #我的收藏按钮
    my_collect=('name', '我的收藏')
    #订单管理页面
    order_manage=('name', '订单管理')
    #账户余额
    account=('name', '账户余额')
    #优惠卷
    couppon=('name', '优惠券')
    #积分查询
    integral=('name', '积分兑换')
    #交易记录
    trading_record=('name', '交易记录')
    #消息中心
    msg_center=('name', '消息中心')
    #设置
    set=('name', '设置')
    #合作店铺
    partner=('name', '合作店铺')
    #客服电话
    phone=('name', '客服电话')
    #呼叫
    call=('name', '呼叫')
    #取消
    cancel=('name', '取消')
    '''收藏夹页'''
    #编辑按钮
    edit=('id', 'com.huimin.ordersystem:id/title_right_text')
    #收藏夹页面商品名称
    goods_name=('id', 'com.huimin.ordersystem:id/item_order_goodsname')
    #商品选择框
    select_goods=('id', 'com.huimin.ordersystem:id/check_normal')
    #删除按钮
    delete=('name', '删除')
    '''订单管理页'''
    #未完成订单标签
    unfinish=('name', '未完成订单')
    #订单号text
    orderNo=('name', '订  单  号 :')
    #取消订单按钮
    cancel_order=('name', '取消订单')
    #确认按钮
    okren=('name', '确认')
    #去评价按钮
    evaluate=('name', '去评价')
    #历史订单标签
    history_order=('name', '历史订单')
    #已取消text
    canceled=('name', '已取消')
    #点击查看详情
    check_detail=('name', '点击查看详情')
    #订单详情页商品名text
    order_detail_goods_name=('id', 'com.huimin.ordersystem:id/activity_goods_name')
    '''去充值'''
    #去充值按钮
    recharge=('name', '去充值')
    #充值金额输入框
    credit=('name', '请输入充值金额')
    #支付宝付款
    zfb_pay=('name', '支付宝支付')
    #明细按钮
    detail_button=('name', '明细')
    #余额明细
    yue_detail=('name', '余额明细')
    #余额记录页面的余额
    yue=('id', 'com.huimin.ordersystem:id/balance_money')
    #奖励明细页面的余额奖励
    yue_reward=('name', '余额奖励')
    #月奖励标签
    reward_mouth=('name', '月奖励')
    #年奖励标签
    reward_year=('name', '年奖励')
    #订货text
    order_goods=('name', '订货')
    #领卷按钮
    get_coupon=('name', '领券')
    '''积分查询页'''
    #可用积分
    usable_integral=('name', '可用积分')
    '''交易记录页'''
    #交易记录价格text
    history_price=('id', 'com.huimin.ordersystem:id/trade_history_price')
    '''设置页'''
    #检测更新
    check_update=('name', '检测更新')
    #关于我们
    about_us=('name', '关于我们')
    #退出登录
    log_out=('name', '退出登录')
    #关于我们页面惠配通text
    huipt=('name', '惠配通')
    '''合作店铺页'''
    #下一步按钮
    next_step=('name', '下一步')
    #A类
    A=('A类:7200.00/年')


    def click_business_center(self):
        '''点击商户中心'''
        self.find_element(self.business_center).click()

    def click_order_manage(self):
        '''点击订单管理'''
        self.find_element(self.order_manage).click()

    def click_my_lollect(self):
        '''点击我的收藏'''
        self.find_element(self.my_collect).click()

    def click_account(self):
        '''点击账户余额'''
        self.find_element(self.account).click()

    def click_couppon(self):
        '''点击优惠卷'''
        self.find_element(self.couppon).click()

    def click_integral(self):
        '''点击积分查询'''
        self.find_element(self.integral).click()

    def click_trading_record(self):
        '''点击交易记录'''
        self.find_element(self.trading_record).click()

    def click_msg_center(self):
        '''点击消息中心'''
        self.find_element(self.msg_center).click()

    def click_set(self):
        '''点击设置'''
        self.find_element(self.set).click()

    def click_partner(self):
        '''点击合作店铺'''
        self.find_element(self.partner).click()

    def click_phone(self):
        '''点击客服电话'''
        self.find_element(self.phone).click()

    def click_cancel(self):
        '''点击取消'''
        self.find_element(self.cancel).click()

    def click_edit(self):
        '''点击编辑按钮'''
        # self.find_element(self.edit).click()
        self.tap(self.find_element(self.edit))

    def click_select_goods(self):
        '''点击商品选择框'''
        self.find_element(self.select_goods).click()

    def click_delete(self):
        '''点击删除按钮'''
        self.find_element(self.delete).click()

    def click_goods_name(self):
        '''点击收藏夹页面商品名进入商品详情页'''
        # self.find_element(self.goods_name).click()
        self.tap(self.find_element(self.goods_name))

    def click_unfinish(self):
        '''点击未完成订单标签'''
        self.find_element(self.unfinish).click()

    def click_history_order(self):
        '''点击历史订单按钮'''
        self.find_element(self.history_order).click()

    def click_cancel_order(self):
        '''点击取消订单按钮'''
        self.find_element(self.cancel_order).click()

    def click_okren(self):
        '''点击取消订单页确认按钮'''
        self.find_element(self.okren).click()

    def click_check_detail(self):
        '''点击查看详情按钮'''
        self.find_element(self.check_detail).click()

    def click_recharge(self):
        ''''点击去充值按钮'''
        self.find_element(self.recharge).click()

    def click_zfb_pay(self):
        '''点击支付宝支付'''
        self.find_element(self.zfb_pay).click()

    def click_yue_detail(self):
        '''点击余额明细'''
        self.find_element(self.yue_detail).click()

    def click_detail_button(self):
        '''点击明细按钮'''
        self.find_element(self.detail_button).click()

    def click_reward_mouth(self):
        '''点击月奖励标签'''
        self.find_element(self.reward_mouth).click()

    def click_reward_year(self):
        '''点击年奖励标签'''
        self.find_element(self.reward_year).click()

    def click_getcoupon(self):
        '''点击领卷按钮'''
        self.find_element(self.get_coupon).click()

    def click_about_us(self):
        '''点击关于我们'''
        self.find_element(self.about_us).click()

    def click_log_out(self):
        '''点击退出登录'''
        self.find_element(self.log_out).click()

    def click_call(self):
        '''点击呼叫按钮'''
        self.find_element(self.call).click()

    def click_next_step(self):
        '''点击下一步按钮'''
        self.find_element(self.next_step).click()

    def click_A(self):
        '''点击A类'''
        self.find_element(self.A).click()

    def sendkeys_credit(self, n):
        '''输入充值金额'''
        self.send_keys(self.credit, n)

    def get_cancel_order(self):
        '''得到取消订单按钮列表'''
        order_list=self.find_elements(self.cancel_order)
        return order_list
