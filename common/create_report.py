__author__ = 'Administrator'
import unittest, time, re, os, shutil, BSTestRunner
from HTMLTestRunner import HTMLTestRunner
from testcase.test1_firstpage import TestFirstPage
from testcase.test2_orderpage import TestOrderPage
from testcase.test3_shopping_cart import TestShoppingCar
from testcase.test4_business_center import TestBusinessCenter


def create_report():
    '''生成测试报告，并返回fail、error信息和生成的html文件'''
    # 指定测试用例为当前文件夹下的./interface目录
    test_dir = 'G:/huipeitongUI/testcase'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now = time.strftime('%y-%m-%d_%H_%M_%S')
    filename = 'G:/huipeitongUI/report/' + now + '_result.html'
    # 生成测试报告
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            verbosity=2,
            title='惠配通Android APP 回归测试报告',
            description='惠配通Android APP 回归测试报告'
        )
        try:
            runner.run(discover)
        except:
            print('haha')
    # result_dir='./report'
    result_dir = 'G:/huipeitongUI/report'
    lists = os.listdir(result_dir)
    lists.sort()
    file_del = os.path.join('G:/huipeitongUI/report/', lists[0])
    #复制之前生成的报告至一个备份目录
    shutil.copy(file_del, 'G:/huipeitongUI/backupreport/')
    #删除之前生成的测试报告
    os.remove(file_del)
    file_new = os.path.join('G:/huipeitongUI/report/', lists[-1])
    with open(file_new, 'r', encoding='utf-8') as f:
        html = f.read()
    #匹配fail和error是否出现
    f = re.findall(r"class=\'failClass\'>\n", html)
    e = re.findall(r"class=\'errorClass\'>\n", html)
    # f=re.findall(r'<td class="text text-danger">.+</td>', html)[0].replace('</td>','').replace('<td class="text text-danger">','')
    # e=re.findall(r'<td class="text text-warning">.+</td>', html)[0].replace('</td>','').replace('<td class="text text-warning">','')
    #返回匹配的f和e以及读取到的html
    report_info = {'fail': f, 'error': e, 'file_new': file_new, 'html': html}
    return report_info


def create_repAgain(html):
    '''将首次未通过的用例再执行一次'''
    ema = re.findall(r"errorCase'><div class=.+:", html)
    fma = re.findall(r"failCase'><div class=.+:", html)
    # ema = re.findall(r"text-warning'><div class=.+:", html)
    # fma = re.findall(r"text-danger'><div class=.+:", html)
    errorcase = []
    failcase = []
    if ema != []:
        for i in range(len(ema)):
            emas = ema[i].split("'testcase'>")
            # 出现error的case名
            emassage = emas[1].strip(':')
            errorcase.append(emassage)
    if fma != []:
        for i in range(len(fma)):
            fmas = fma[i].split("'testcase'>")
            # 出现fail的case名
            fmassage = fmas[1].strip(':')
            failcase.append(fmassage)
    failcase.extend(errorcase)
    # suite = unittest.TestSuite()
    # suite.addTest(TestFirstPage('test_1Login'))
    # for testcase in failcase:
    #     if hasattr(TestFirstPage, testcase):
    #         suite.addTest(TestFirstPage(testcase))
    #     if hasattr(TestOrderPage, testcase):
    #         suite.addTest(TestOrderPage(testcase))
    #     if hasattr(TestShoppingCar, testcase):
    #         suite.addTest(TestShoppingCar(testcase))
    #     if hasattr(TestBusinessCenter,testcase):
    #         suite.addTest(TestBusinessCenter(testcase))
    firstcase=[]
    ordercase=[]
    shopcarcase=[]
    businesscenter=[]
    for testcase in failcase:
        if hasattr(TestFirstPage, testcase):
            firstcase.append(testcase)
        if hasattr(TestOrderPage, testcase):
            ordercase.append(testcase)
        if hasattr(TestShoppingCar, testcase):
            shopcarcase.append(testcase)
        if hasattr(TestBusinessCenter,testcase):
            businesscenter.append(testcase)
    if 'test_1Login' in firstcase:
        firstcase.remove('test_1Login')
    suite = unittest.TestSuite()
    if firstcase!=[]:
        suite.addTest(TestFirstPage('test_1Login'))
        for testcase in firstcase:
            suite.addTest(TestFirstPage(testcase))
    if ordercase !=[]:
        for testcase in ordercase:
            suite.addTest(TestOrderPage(testcase))
    if shopcarcase != []:
        for testcase in shopcarcase:
            suite.addTest(TestShoppingCar(testcase))
    if businesscenter != []:
        for testcase in businesscenter:
            suite.addTest(testcase)
    now = time.strftime('%y-%m-%d_%H_%M_%S')
    filename = 'G:/huipeitongUI/report/' + now + '_result.html'
    # 生成测试报告
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            verbosity=2,
            title='汇配通Android APP 回归测试报告',
            description='汇配通Android APP 回归测试报告'
        )
        runner.run(suite)
    # result_dir='./report'
    result_dir = 'G:/huipeitongUI/report'
    lists = os.listdir(result_dir)
    lists.sort()
    file_del=os.path.join('G:/huipeitongUI/report/',lists[0])
    #复制之前生成的报告至一个备份目录
    shutil.copy(file_del, 'G:/huipeitongUI/backupreport/')
    #删除之前生成的测试报告
    os.remove(file_del)
    file_new = os.path.join('G:/huipeitongUI/report/', lists[-1])
    with open(file_new, 'r', encoding='utf-8') as f:
        html = f.read()
    #匹配fail和error是否出现
    f = re.findall(r"class=\'failClass\'>\n", html)
    e = re.findall(r"class=\'errorClass\'>\n", html)
    # f=re.findall(r'<td class="text text-danger">.+</td>', html)[0].replace('</td>','').replace('<td class="text text-danger">','')
    # e=re.findall(r'<td class="text text-warning">.+</td>', html)[0].replace('</td>','').replace('<td class="text text-warning">','')
    #返回匹配的f和e以及读取到的html
    report_info = {'fail': f, 'error': e, 'file_new': file_new, 'html': html}
    return report_info
