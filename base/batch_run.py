"""
依据adb devices数量批量启动appium服务
"""

import re
import time
import subprocess
import multiprocessing
import threading
from base.api import run_cmd, create_report, logger, check_appium_server_status, get_package, get_device_info
from base.setting import *


def get_udids():
    """
    得到连接的设备的udid
    :return: list
    """
    stdout = run_cmd('adb devices')
    logger.debug('adb devices的结果{}'.format(stdout))
    udids = re.findall(r'\n(.+)\tdevice', stdout)
    logger.info('udids{}'.format(udids))
    return udids


def get_ports(udids):
    """
    依据得到的设备数生成未使用的端口号,udid * 4
    :return: list
    """
    udids_num = len(udids)
    ports = list()
    port = 4724
    while True:
        if len(ports) == udids_num * 4:
            break
        if not run_cmd('netstat -ano | findstr {}'.format(port)):
            ports.append(port)
        port += 1
    logger.info('得到未使用的端口列表:{}'.format(ports))
    return ports


def run_server(arg, i):
    """
    执行输入的cmd命令,非阻塞线程
    :param arg:
    :return:
    """
    appium_log = os.path.join(BASE_DIR, 'log/appium_{}.txt'.format(i))
    appium_error_log = os.path.join(BASE_DIR, 'log/appium_error_{}.txt'.format(i))
    subprocess.Popen(
        arg, stdout=open(appium_log, 'w'),
        stderr=open(appium_error_log, 'a'),
        shell=True
    )


def start_appium(udids, ports):
    """
    依据设备udid和得到的端口号启动对应数量的appium服务
    :param udids: 设备的idid，type:list
    :param ports: 空闲的端口号，type:list
    :return:
    """
    k = 0
    for udid in udids:
        arg = ('appium -p {} -bp {} --chromedriver-port {} -U {} --session-override --log-timestamp'
               ' --local-timezone').format(ports[k], ports[k+1], ports[k+2], udid)
        logger.info('开始启动appium服务{}'.format(arg))
        th = threading.Thread(target=run_server, args=(arg, udid))
        th.start()  # 这里不需要join,runcase运行完毕杀掉appium服务相关进程即可
        k += 3


def kill_appium():
    """
    kill掉所有node.exe进程
    :return:
    """
    arg = 'taskkill -F -IM node.exe'
    r = run_cmd(arg)
    logger.info(r.strip())


def run_case(udids, ports):
    """
    依据udid和启动的appium服务去执行测试
    :param udids:
    :param ports:
    :return:
    """
    multiprocessing.freeze_support()
    pros = list()
    for i in udids:
        pro = multiprocessing.Process(target=create_report)
        pros.append(pro)
    for i, pro in enumerate(pros):
        platform_version, devices_name = get_device_info(udids[i])
        DESIRED_CAPS['platformVersion'] = platform_version
        DESIRED_CAPS['deviceName'] = devices_name
        DESIRED_CAPS['systemPort'] = ports[-(i + 1)]
        DESIRED_CAPS['remoteHost'] = 'http://127.0.0.1:{}/wd/hub'.format(ports[i * 3])
        config.write()
        if check_appium_server_status(ports[i * 3]):
            pro.start()
            time.sleep(2)
        else:
            logger.warning('{} appium服务未成功运行.'.format(DESIRED_CAPS['remoteHost']))
            pros.remove(pro)
    for pro in pros:
        pro.join()


if __name__ == "__main__":
    udids = get_udids()
    ports = get_ports(udids)
    if udids:
        get_package()
        try:
            th1 = threading.Thread(target=start_appium, args=(udids, ports))
            th2 = threading.Thread(target=run_case, args=(udids, ports))
            ths = [th1, th2]
            for th in ths:
                th.start()
                time.sleep(10)
            ths[1].join()  # 只需要ths[1]run_case的线程运行结束即可结束测试
        finally:
            kill_appium()
    else:
        logger.warning('adb devices未获取到设备，请检查adb连接状态')

