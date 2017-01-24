import unittest, multiprocessing, time, HTMLTestRunner,os,random,threading
from common.appiums import startappium


def createreport(suite):
    '''生成测试报告'''
    now = time.strftime('%y-%m-%d_%H_%M_%S')
    filename = 'G:/huipeitongUI/report/' + now + '-' + str(random.randint(0, 100)) + '_result.html'
    print(filename)
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            verbosity=2,
            title='惠配通Android APP 回归测试报告',
            description='惠配通Android APP 回归测试报告'
        )
        runner.run(suite)

def runcase():
    '''多进程运行case'''
    casedir = r'G:\huipeitongUIProcess\testcase'
    testunita = unittest.defaultTestLoader.discover(start_dir=casedir, pattern='testa*.py')
    testunitb = unittest.defaultTestLoader.discover(start_dir=casedir, pattern='testb*.py')
    suite = [testunita, testunitb]
    multiprocessing.freeze_support()
    proclist = []
    for i in suite:
        proc = multiprocessing.Process(target=createreport, args=(i,))
        proclist.append(proc)
    for proc in proclist:
        proc.start()
    for proc in proclist:
        proc.join()
if __name__ == '__main__':
    output=os.popen('adb devices').read()
    if '\tdevice\n' in output and '\tdevice\n\n' in output:
        #开启2个线程一个去启动appium服务一个去运行case
        th1 = threading.Thread(target=startappium)
        th2 = threading.Thread(target=runcase)
        threads = [th1, th2]
        for i in threads:
            i.start()
            time.sleep(10)
        # for i in threads:
        #     i.join()
        #这里只让runcase的线程守护，等到runcase的线程执行完毕，去杀掉启动的2个node.exe进程
        threads[1].join()
        os.popen('taskkill /f /t /im node.exe')
        os.popen('taskkill /f /t /im node.exe')
    else:
        print('please check whether the adb connection!')
