__author__ = 'Administrator'
import unittest
from po.basepage import Action
class Assect(unittest.TestCase):

    def __init__(self,driver=None):
        self.driver=driver
        self.current=Action(self.driver)

    def assertt(self, loc, errorinfo):
        '''断言assertTrue封装'''
        self.assertTrue(loc, self.driver, errorinfo)

    def assertIsE(self,loc,erroinfo):
        "断言某个元素是否存在,loc为查找的元素，errorinfo为错误提示信息"
        self.assertTrue(self.current.isElementExist(loc), self.driver, erroinfo)

    def assertIsEn(self,loc,erroinfo):
        "断言某个元素是否存在,loc为查找的元素，errorinfo为错误提示信息"
        self.assertTrue(not self.current.isElementExist(loc), self.driver, erroinfo)

    def assertEw(self, loc, errorinfo):
        '''断言某个元素是否出现(60s内)，'''
        self.assertTrue(self.current.elementwait(loc), self.driver, errorinfo)

    def assertI(self, one, two, errorinfo):
        '''断言assertIn封装'''
        self.assertTrue(one in two, self.driver, errorinfo)



