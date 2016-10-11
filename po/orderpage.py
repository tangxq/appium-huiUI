__author__ = 'Administrator'
from po.basepage import Action
class Orderpage(Action):

    '''惠民订货页'''
    #惠民订货
    hmorder=('name', '订货分类')
    #推荐
    hotlist=('name', '推荐')
    #左侧分类id
    left_view=('id', 'com.huimin.ordersystem:id/category_left_view')
    #左侧分类框
    left_window=('id', 'com.huimin.ordersystem:id/category_left')
    #惠民订货页商品名称
    goods_name=('id', 'com.huimin.ordersystem:id/category_good_name')
    #惠民订货页商品图
    goods_img=('id', 'com.huimin.ordersystem:id/category_good_img')
    #搜索框
    search_inpu=('id', 'com.huimin.ordersystem:id/category_search')
    #酒类按钮
    wine=('name', '酒类')
    #常购清单按钮
    buy_list=('id', 'com.huimin.ordersystem:id/category_collect')
    '''筛选'''
    #茶饮料
    tea_drink=('name', '茶饮料')
    #品牌筛选
    filter_brand=('name', '品牌筛选')
    #排序筛选
    filter_sort=('name', '排序筛选')
    #王老吉
    wanglj=('name', '王老吉')
    #价格最低
    price_low=('name', '价格最低')

    '''搜索页'''
    #搜索页面，搜索结果text
    search_result_text=('name', '搜索结果')
    #搜索输入框
    search_input=('id', 'com.huimin.ordersystem:id/activity_search_edit')
    #搜素按钮
    search_button=('name', '搜索')
    #没有更多了
    nosearch=('name', '没有更多了')
    #搜索结果页面商品名称
    search_goods_name=('id', 'com.huimin.ordersystem:id/item_order_goodsname')
    #搜索页面返回按钮
    search_backup=('id', 'com.huimin.ordersystem:id/includ_title_btleft')
    #火热购买商品名称
    hot_goods_name=('id', 'com.huimin.ordersystem:id/item_home_name')
    #火热购买商品，滑动框
    hot_goods_swipe=('id', 'com.huimin.ordersystem:id/activity_search_gridview')
    #搜索页返回按钮
    backup=('id', 'com.huimin.ordersystem:id/includ_title_btleft')

    '''常购清单页'''
    #商品名称
    history_name=('id', 'com.huimin.ordersystem:id/shop_history_name')
    #快捷购物车id
    right_shopcar=('id', 'com.huimin.ordersystem:id/float_shopcar_layout')

    def click_hmorder(self):
        '''点击惠民订货'''
        self.find_element(self.hmorder).click()

    def click_goods_img(self):
        '''点击惠民订货页商品图'''
        self.find_element(self.goods_img).click()

    def click_search_inpu(self):
        '''点击搜索框'''
        self.find_element(self.search_inpu).click()

    def sendkeys_search_input(self,key):
        '''搜索输入框输入“统一”'''
        self.send_keys(self.search_input, key)

    def click_search_button(self):
        '''点击搜索按钮'''
        self.find_element(self.search_button).click()

    def click_search_goods_name(self):
        '''点击搜索到的商品名'''
        self.find_elements(self.search_goods_name)[1].click()

    def click_search_backup(self):
        '''点击搜索页返回按钮'''
        self.find_element(self.search_backup).click()

    def click_hot_goodsname(self):
        '''点击火热购买商品名'''
        self.find_element(self.hot_goods_name).click()

    def click_wine(self):
        '''点击酒类'''
        self.find_element(self.wine).click()

    def click_tea_drink(self):
        '''点击茶饮料'''
        self.find_element(self.tea_drink).click()

    def click_filter_brand(self):
        '''点击品牌筛选'''
        self.find_element(self.filter_brand).click()

    def click_wanglj(self):
        '''点击王老吉'''
        self.find_element(self.wanglj).click()

    def click_filter_sort(self):
        '''点击排序筛选'''
        self.find_element(self.filter_sort).click()

    def click_price_low(self):
        '''点击价格最低'''
        self.find_element(self.price_low).click()

    def click_buy_list(self):
        '''点击常购清单按钮'''
        self.find_element(self.buy_list).click()

    def click_history_name(self):
        '''点击常购清单页商品名'''
        self.find_element(self.history_name).click()

    def click_right_shopcar(self):
        '''点击常购清单页面快捷购物车'''
        self.find_element(self.right_shopcar).click()

    def click_backup(self):
        '''点击搜索页的返回按钮'''
        self.find_element(self.backup).click()


    def get_list_view(self):
        '''得到惠民订货页左侧列表'''
        left_list=self.find_elements(self.left_view)
        return left_list

    def get_left_window(self):
        '''返回左侧分类框元素'''
        element=self.find_element(self.left_window)
        return element

    def get_hot_goods_swipe_window(self):
        '''返回搜索页面火热购买商品框'''
        element=self.find_element(self.hot_goods_swipe)
        return element

    def get_search_goods_name(self):
        '''返回搜索结果页商品名称'''
        name=self.find_element(self.search_goods_name).get_attribute('name')
        return name

    def get_hot_goodsname(self):
        '''返回火热购买商品名'''
        name=self.find_element(self.hot_goods_name).get_attribute('name')
        return name

    def get_huimin_goods_name(self):
        '''返回订货分类页面商品名'''
        name=self.find_element(self.goods_name).get_attribute('name')
        return name

    def get_huimin_goodsnum(self):
        '''返回订货分类页一页显示的商品数'''
        num=len(self.find_elements(self.goods_name))
        return num

