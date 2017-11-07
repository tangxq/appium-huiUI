"""封装所有与appium服务端通信的类"""
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from base.choose_chromedriver import get_chrome_path
from base.api import *

image_dir = os.path.abspath(os.path.join(BASE_DIR, 'image'))


class UiHelper:
    remoteHost = 'http://127.0.0.1:4900/wd/hub'
    XPATH_TAG = "//"
    XPATH_ABS = "/"
    ID_TAG = ":id/"

    def __init__(self):
        """
        初始化desired capabilities
        """
        self.desired_caps = dict()
        self._driver = None
        for j, k in DESIRED_CAPS.items():
            if j == 'app':
                # k = os.path.join(BASE_DIR, k)
                logger.info("apk 安装路径:{}".format(k))
            elif j == 'remoteHost':
                self.remoteHost = k
                continue
            self.desired_caps[j] = k
        necessary = {
            # 'platformVersion': PLATFORM_VERSION,
            # 'deviceName': DEVICES_NAME,
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noSign': True,
            'recreateChromeDriverSessions': True,  # 解决第二次进入h5页面点击无响应问题
        }
        self.desired_caps.update(necessary)
        chrome_path = get_chrome_path()
        if chrome_path:
            self.desired_caps['chromedriverExecutable'] = chrome_path

    def init_driver(self):
        """
        初始化driver
        """
        logger.info(self.remoteHost)
        print(self.remoteHost)
        self._driver = webdriver.Remote(self.remoteHost, self.desired_caps)

    def quit_driver(self):
        """
        退出driver
        """
        if self._driver:
            logger.info('退出driver.')
            self._driver.quit()

    def find_element(self, control_info, period=10):
        """
        通过给定的xpath, id 或 name来查找控件
        :Args:
            -control_info：控件的信息，可以是xpath,id，name或其他属性
            -period: 持续时间10s
        :Return:
            如果找到控件返回第一个.找不到则抛出not_find_element异常
        :Usage:
            self.find_element(control_info)
        """
        for i in range(period):
            try:
                if control_info.startswith(self.XPATH_TAG) or control_info.startswith(self.XPATH_ABS):
                    element = self._driver.find_element_by_xpath(control_info)
                elif self.ID_TAG in control_info:
                    element = self._driver.find_element_by_id(control_info)
                else:
                    element = self._driver.find_element_by_class_name(control_info)
            except NoSuchElementException:
                time.sleep(1)
                continue
            else:
                return element
        else:
            raise NoSuchElementException('Cannot find %s in %d times' % (control_info, period))

    def find_elements(self, control_info, period=10):
        """
        通过给定的xpath, id 或 name来查找控件
        :Args:
            -control_info：控件的信息，可以是xpath,id，name或其他属性
        :Return:
            返回所有满足条件的控件，返回的类型是一个列表.找不到则抛出not_find_element异常
        :Usage:
            self.find_elements(control_info)
        """
        for i in range(period):
            try:
                if control_info.startswith(self.XPATH_TAG):
                    element = self._driver.find_elements_by_xpath(control_info)
                elif self.ID_TAG in control_info:
                    element = self._driver.find_elements_by_id(control_info)
                else:
                    element = self._driver.find_elements_by_class_name(control_info)
            except NoSuchElementException:
                time.sleep(1)
                continue
            else:
                return element
        else:
            raise NoSuchElementException('Cannot find %s in %d times' % (control_info, period))

    def find_element_in_parent_element(self, parent_element, child_element_info):
        """
        在一个已知的控件中通过给定的xpath, id , name或者其他属性来查找子控件
        :Args:
            -parent_element:父控件，是一个一直的webElement
            -child_element_info:子控件信息，可以是xpath,id或者其他属性
        :Return:
            如果找到控件返回第一个.找不到则抛出not_find_element异常
        :Usage:
            self.find_element_in_parent_element(parent_element, child_element_info)
        """
        if child_element_info.startswith(self.XPATH_TAG):
            element = parent_element.find_element_by_xpath(child_element_info)
        elif self.ID_TAG in child_element_info:
            element = parent_element.find_element_by_id(child_element_info)
        else:
            element = parent_element.find_element_by_class_name(child_element_info)
        return element

    def find_elements_in_parent_element(self, parent_element, child_element_info):
        """
        在一个已知的控件中通过给定的xpath, id , name或者其他属性来查找子控件
        :Args:
            -parent_element:父控件，是一个已知的webElement
            -child_element_info:子控件信息，可以是xpath,id或者其他属性
        :Return:
            如果找到控件所有符合条件的控件，返回类型是一个列表.找不到则抛出not_find_element异常
        :Usage:
            self.find_elements_in_parent_element(parentElement, childElementInfo)
        """
        if child_element_info.startswith(self.XPATH_TAG):
            element = parent_element.find_elements_by_xpath(child_element_info)
        elif self.ID_TAG in child_element_info:
            element = parent_element.find_elements_by_id(child_element_info)
        else:
            element = parent_element.find_elements_by_class_name(child_element_info)
        return element

    def find_element_by_uiautomator(self, uia_string):
        """
        通过UIAutomator的uia_string来查找控件
        :Args:
            -uia_string: UiSelector相关的代码，参考http://developer.android.com/tools/help/
            uiautomator/UiSelector.html#fromParent%28com.android.uiautomator.core.UiSelector%29
        :Return:
            -找到的控件
        :Usage:
            self.find_element_by_uiautomator(new UiSelector().(android.widget.LinearLayout))
        """
        return self._driver.find_element_by_android_uiautomator(uia_string)

    def click(self, element_info):
        """
        点击某元素，如果元素不存在则抛出异常
        :Args:
            -element_info 元素信息，可以是xpath,id或者其他属性
        :Usage:
            self.click_element(element_info)
        """
        self.find_element(element_info).click()

    def tap(self, element_info):
        """
        点击某元素，如果元素不存在则抛出异常
        :Args:
            -element_info 元素信息，可以是xpath,id或者其他属性
        :Usage:
            self.tap(element_info)
        """
        self._driver.tap(self.find_element(element_info))

    def long_press(self, element_info, duration):
        """
        长按某元素，如果元素不存在则抛出异常
        :Args:
            -element_info 元素信息，可以是xpath,id或者其他属性
            -duration 持续时间,单位ms
        :Usage:
            self.long_press(element_info, duration)
        """
        self._driver.tap(self.find_element(element_info), duration)

    def swipe_up(self, duration=None):
        """
        向上滑动屏幕
        :Args:
            -duration 多长时间完成该操作，单位ms
        :Usage:
            self.swipe_up(duration)
        """
        width = self._driver.get_window_size()['width']
        height = self._driver.get_window_size()['height']
        start_y, end_y = height * 4 / 5, height * 1 / 5
        x = width * 1 / 2
        logger.info('上滑屏幕')
        self._driver.swipe(x, start_y, x, end_y, duration)

    def swipe_down(self, duration=None):
        """
        向下滑动屏幕
        :Args:
            -duration 多长时间完成该操作，单位ms
        :Usage:
            self.swipe_down(duration)
        """
        width = self._driver.get_window_size()['width']
        height = self._driver.get_window_size()['height']
        start_y, end_y = height * 1 / 5, height * 4 / 5
        x = width * 1 / 2
        logger.info('下滑屏幕')
        self._driver.swipe(x, start_y, x, end_y, duration)

    def swipe_left(self, duration=None):
        """
        向左滑动屏幕
        :Args:
            -duration 多长时间完成该操作，单位ms
        :Usage:
            self.swipe_left(duration)
        """
        width = self._driver.get_window_size()['width']
        height = self._driver.get_window_size()['height']
        start_x, end_x = width * 4 / 5, width * 1 / 5
        y = height * 1 / 2
        logger.info('左滑屏幕')
        self._driver.swipe(start_x, y, end_x, y, duration)

    def swipe_right(self, duration=None):
        """
        向右滑动屏幕
        :Args:
            -duration 多长时间完成该操作，单位ms
        :Usage:
            self.swipe_right(duration)
        """
        width = self._driver.get_window_size()['width']
        height = self._driver.get_window_size()['height']
        start_x, end_x = width * 1 / 5, width * 4 / 5
        y = height * 1 / 2
        logger.info('右滑屏幕')
        self._driver.swipe(start_x, y, end_x, y, duration)

    def swipe_on_element(self, element, direction, duration=None):
        """
        在某元素上进行上下左右滑动
        :Args:
            -element 滑动的目标元素，是一个element
            -direction 滑动的方向，可以是'Up'、'Down'、'Left'、'Right'
            -duration 多长时间完成该操作，单位ms
        :Usage:
            self.swipe_on_element(element, direction)
        """
        x, y = element.location.get('x'), element.location.get('y')
        element_width, element_height = element.size.get('width'), element.size.get('height')

        def swipe_up(x, y, width, height, duration):
            start_x = x + width * 1 / 2
            start_y, end_y = y + height * 7 / 8, y + height * 1 / 8
            self._driver.swipe(start_x, start_y, start_x, end_y, duration)

        def swipe_down(x, y, width, height, duration):
            start_x = x + width * 1 / 2
            start_y, end_y = y + height * 1 / 8, y + height * 7 / 8
            self._driver.swipe(start_x, start_y, start_x, end_y, duration)

        def swipe_left(x, y, width, height, duration):
            start_y = y + height * 1 / 2
            start_x, end_x = x + width * 7 / 8, x + width * 1 / 8
            self._driver.swipe(start_x, start_y, end_x, start_y, duration)

        def swipe_right(x, y, width, height, duration):
            start_y = y + height * 1 / 2
            start_x, end_x = x + width * 1 / 8, x + width * 7 / 8
            self._driver.swipe(start_x, start_y, end_x, start_y, duration)

        dicts = {'Up': swipe_up, 'Down': swipe_down, 'Left': swipe_left, 'Right': swipe_right}
        dicts.get(direction)(x, y, element_width, element_height, duration)

    def start_activity(self, app_activity, app_package=None):
        """
        打开指定的activity
        :Args:
            -app_activity activity名称
            -app_package app的包名,默认为当前测试的app包名
        :Usage:
            self.start_activity(app_activity, app_package)
        """
        if not app_package:
            app_package = self.desired_caps['appPackage']
        self._driver.start_activity(app_package, app_activity)

    def text(self, element_info):
        """
        获取某个元素的显示文本，如果找不到该元素则抛出异常
        :Args:
            -element_info 元素信息，可以是xpath,id或者其他属性
        :Return:
            返回该元素显示的文本
        :Usage:
            self.get_text_of_element(element_info)
        """
        element = self.find_element(element_info)
        return element.text

    def send_keys(self, element_info, words):
        """
        向输入框输入指定的文本
        :Args:
            -element_info 元素信息，可以是xpath,id或者其他属性
            -words 要输入的文本信息
        :Usage:
            self.send_keys(element_info, words)
        """
        element = self.find_element(element_info)
        element.send_keys(words)

    def clear(self, element_info):
        """
        清楚文本框里面的文本
        :Args:
            -element_info 元素信息，可以是xpath,id或者其他属性
        :Usage:
            self.clear_text_edit(element_info)
        """
        element = self.find_element(element_info)
        element.clear()

    def press_back_key(self, num=4):
        """
        按返回键
        :Usage:
            self.press_back_key()
        """
        logger.info('按返回键.')
        self._driver.press_keycode(num)

    def press_enter_key(self):
        """
        按确认键
        :Usage:
            self.press_enter_key()
        :return:
        """
        logger.info('按确认键')
        self._driver.press_keycode(66)

    def element_is_show(self, element_info, period=2):
        """
        判断某个元素是否显示
        :Args:
            -element_info 元素信息，可以是xpath,id或者其他属性
        :Return:
            元素找到则返回True,否则返回False
        :Usage:
            self.check_element_is_show(element_info)
        """
        try:
            self.find_element(element_info, period)
            return True
        except NoSuchElementException:
            return False

    def wait_element(self, element_info, retry=3):
        """
        等待某个元素显示,在某段时间内,并返回该元素
        :Args:
            -element_info 元素信息，可以是xpath,id或者其他属性
            -retry 查找的次数（因为find_element每次查找10s,所以这里的1次代表10s）
        :Usage:
            self.wait_for_element(element_info, period)
        """
        for i in range(0, retry):
            try:
                element = self.find_element(element_info)
                return element
            except NoSuchElementException:
                continue
        else:
            raise NoSuchElementException('Cannot find %s in %d times' % (element_info, retry))

    def element_in_time(self, element_info, retry=10):
        """
        在某段时间内，判断该元素是否显示，若显示返回true，否则返回false
        :Args:
            -element_info 元素信息，可以是xpath,id或者其他属性
            -retry 查找的次数（因为find_element每次查找ns,所以这里的1次代表retry X ns）
        :Return:
            -True or False
        :Usage:
            self.check_for_element_in_time(element_info, retry)
        """
        for i in range(0, retry):
            try:
                self.find_element(element_info)
                return True
            except NoSuchElementException:
                continue
        else:
            return False

    def element_not_in_time(self, element_info, retry=10):
        """
        在某段时间内等待某个元素不显示，若不显示则立即返回True，若一直显示则返回False
        :Args:
            -element_info 元素信息，可以是xpath,id或者其他属性
            -retry 查找的次数（因为find_element每次查找ns,所以这里的1次代表retry X ns）
        :Return:
            -True or False
        :Usage:
            self.check_for_element_not_in_time(element_info, retry)
        """
        status = True
        for i in range(0, retry):
            try:
                self.find_element(element_info)
                continue
            except NoSuchElementException:
                break
        else:
            status = False
        return status

    def is_selected(self, element_info):
        """
        判断某个元素是否被选中
        :Args:
            -element_info 元素信息，可以是xpath,id或者其他属性
        :Return:
            -如果该元素被选中则返回True,否则返回False
        :Usage:
            -self.check_element_is_selected(element_info)
        """
        element = self.find_element(element_info)
        return element.is_selected()

    def get_attribute(self, element_info, attribute_name):
        """
        得到指定元素的某个属性
        :Args:
            -element_info 元素信息，可以是xpath,id或者其他属性
            -attribute_name 属性名称
        :Returns:
            -对应的属性值
        :Usage:
            -self.get_attribute(element_info, attribute_name)
        """
        element = self.find_element(element_info)
        return element.get_attribute(attribute_name)

    def save_screen_shot(self):
        """
        保存当前手机的截图到report/image目录下，以当前时间来命名图片名
        :Usage:
            self.save_screen_shot()
        """
        image_name = time.strftime('%y-%m-%d_%H_%M_%S') + '.png'
        self._driver.save_screenshot(os.path.normpath(os.path.join(image_dir, image_name)))
        filename = IMAGE_IP + image_name
        print('image' + filename)

    def current_activity(self):
        """
        得到当前页面的activity
        :Usage:
            self.current_activity()
        """
        return self._driver.current_activity

    def find_toast(self, message, duration=5):
        """
        判断当前页面是否弹出内容为message的toast提示
        :Args:
            -message: toast提示信息的内容(可以为一部分)
            -duration: 持续时间，单位s
        :Returns:
            -True:找到指定的toast信息
            -False:未找到指定的toast信息
        :Usage:
            -self.find_toast(message)
        """
        message = '//*[contains(@text, "{}")]'.format(message)
        try:
            # 返回的elements是一个列表，如果找到elements，elements[0].text为获取到的内容
            WebDriverWait(self._driver, duration, 0.2).until(
                EC.presence_of_all_elements_located((By.XPATH, message))
            )
            logger.info('找到toast"{}"'.format(message))
            return True
        except (NoSuchElementException, TimeoutException):
            logger.info('未找到toast"{}"'.format(message))
            return False

    def get_contexts(self):
        """
        获得所有的上下文（获取webview）
        :Returns:
            -所有上下文，list
        :Usage:
            -self.get_contexts()
        """
        return self._driver.contexts

    def switch_context(self, context_name):
        """
        切换至对应名称的上下文
        :Args:
            -context_name:上下文名称
        :Usage:
            -self.switch_context()
        """
        logger.info('切换上下文至"{}"'.format(context_name))
        self._driver.switch_to.context(context_name)

    def find_by_scroll(self, text):
        """
        通过元素的text属性，边滑动边寻找元素
        :Args:
            -text:元素的text属性
        :Usage:
            -self.find_by_scroll(text)
        """
        return self.find_element_by_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.getChildByText(new UiSelector().className(android.widget.LinearLayout), "%s")' % text
        )
