__author__ = 'Administrator'
#coding=UTF-8
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium import webdriver
import time
class Action(object):
    def __init__(self,driver=None):
        self._touch=TouchAction(driver)
        self._mydriver=driver

    #重写元素定位方法
    def find_element(self, loc):
        return self._mydriver.find_element(loc[0],loc[1])
        # try:
        #     # WebDriverWait(self._mydriver, 15).until(lambda driver: driver.find_element(loc[0],loc[1]).is_displayed())
        #     return self._mydriver.find_element(loc[0],loc[1])
        # except:
        #     print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    #重写一组元素定位方法
    def find_elements(self, loc):
        return self._mydriver.find_elements(loc[0],loc[1])
        # try:
        #     if len(self._mydriver.find_elements(loc[0],loc[1])):
        #         return self._mydriver.find_elements(loc[0],loc[1])
        # except:
        #     print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    #重写定义send_keys方法
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            self.find_element(loc).send_keys(vaule)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))


    def tap(self,Element):
        #点击某元素
        try:
            self._touch.tap(Element).release().perform()
        except Exception as err:
            print("The error:"+str(err))
    def taps(self,x,y):
        #点击某坐标
        try:
            self._touch.tap(x,y).release().perform()
        except Exception as err:
            print("The error:"+str(err))
    def swipeUp(self,duration=None):
        #向上滑动,duration单位ms
        try:
            (width,height)=(self._mydriver.get_window_size()['width'],self._mydriver.get_window_size()['height'])
            starty=height*4/5
            endy=height*1/5
            x=width*1/2
            self._mydriver.swipe(x,starty,x,endy,duration)
        except Exception as err:
            print("The error:"+str(err))
    def swipeDown(self,duration=None):
        #向下滑动
        try:
            (width,height)=(self._mydriver.get_window_size()['width'],self._mydriver.get_window_size()['height'])
            starty=height*1/5
            endy=height*4/5
            x=width*1/2
            self._mydriver.swipe(x,starty,x,endy,duration)
        except Exception as err:
            print("The error:"+str(err))
    def swipeLeft(self,duration=None):
        #向左滑动
        try:
            (width,height)=(self._mydriver.get_window_size()['width'],self._mydriver.get_window_size()['height'])
            startx=width*4/5
            endx=width*1/5
            y=height*1/2
            self._mydriver.swipe(startx,y,endx,y,duration)
        except Exception as err:
            print("The error:"+str(err))
    def swipeRight(self,duration=None):
        #向右滑动
        try:
            (width,height)=(self._mydriver.get_window_size()['width'],self._mydriver.get_window_size()['height'])
            startx=width*1/5
            endx=width*4/5
            y=height*1/2
            self._mydriver.swipe(startx,y,endx,y,duration)
        except Exception as err:
            print("The error:"+str(err))
    def swipeOnEmelent(self,Element,direction,duration=None):
        #在某元素上进行上、下、左、右滑动
        x=Element.location.get('x')
        y=Element.location.get('y')
        elementWidth=Element.size.get('width')
        elementHeight=Element.size.get('height')
        def swipeUp(x,y,elementWidth,elementHeight,duration):
            startx=x+elementWidth*1/2
            starty=y+elementHeight*7/8
            endy=y+elementHeight*1/8
            self._mydriver.swipe(startx,starty,startx,endy,duration)
        def swipeDown(x,y,elementWidth,elementHeight,duration):
            startx=x+elementWidth*1/2
            starty=y+elementHeight*1/8
            endy=y+elementHeight*7/8
            self._mydriver.swipe(startx,starty,startx,endy,duration)
        def swipeLeft(x,y,elementWidth,elementHeight,duration):
            starty=y+elementHeight*1/2
            startx=x+elementWidth*7/8
            endx=x+elementWidth*1/8
            self._mydriver.swipe(startx,starty,endx,starty,duration)
        def swipeRight(x,y,elementWidth,elementHeight,duration):
            starty=y+elementHeight*1/2
            startx=x+elementWidth*1/8
            endx=x+elementWidth*7/8
            self._mydriver.swipe(startx,y,endx,y,duration)
        dicts={'Up':swipeUp,'Down':swipeDown,'Left':swipeLeft,'Right':swipeRight}
        dicts.get(direction)(x,y,elementWidth,elementHeight,duration)
    def swipeUntilElementAppear(self,loc,direction,duration=None):
        #在某个方向上滑动直到出现某元素为止
            i=0
            while i<=10:
                try:
                    self.find_element(loc)
                    break
                except Exception:
                    dicts={"Up":self.swipeUp,"Down":self.swipeDown,"Left":self.swipeLeft(),"Right":self.swipeRight}
                    dicts.get(direction)(duration)
                    i+=1
    def isElementExist(self,loc):
        #判断在当前页面某元素是否存在
        try:
            self.find_element(loc)
            return True
        except Exception as err:
            #print('error:'+str(err))
            return False

    def is_disappeared(self, loc):
        #显示等待，在设定的时间段内去查找元素，如果找到该元素停止等待，未找到则一直找知道超时,超时返回TimeoutException
        WebDriverWait(self._mydriver, 60, 1).until(lambda x: x.find_element(loc[0], loc[1]).is_displayed())

    def elementwait(self, loc):
        #判断指定时间内是否查找到该元素，找到返回True,找不到返回False
        try:
            WebDriverWait(self._mydriver, 60, 1).until(lambda x: x.find_element(loc[0], loc[1]).is_displayed())
        except TimeoutException:
            return False
        else:
            return True