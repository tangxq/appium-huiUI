import smtplib
import traceback
import unittest
import time
import re
import logging
import functools
import io
import subprocess
import requests
import paramiko
from requests.exceptions import ConnectionError
from enum import Enum
from logging.handlers import TimedRotatingFileHandler
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from paramiko.ssh_exception import SSHException
from base.BSTestRunner import BSTestRunner
from base.setting import *

outputBuffer = io.StringIO()


class Case(Enum):
    """
    用例级别枚举
    """
    level1 = 1
    level2 = 2
    level3 = 3


def run_cmd(shell):
    """
    运行cmd命令
    """
    return subprocess.getstatusoutput(shell)[1].strip()


PLATFORM_VERSION = run_cmd('adb shell getprop ro.build.version.release')
DEVICES_NAME = run_cmd('adb shell getprop ro.product.manufacturer') + ' ' + \
              run_cmd('adb shell getprop ro.product.name')


def get_device_info(udid):
    """
    依据设备的udid得到设备的android版本号和品牌、机型
    :param udid:
    :return:
    """
    args1 = 'adb -s {} shell getprop ro.build.version.release'.format(udid)
    args2 = 'adb -s {} shell getprop ro.product.manufacturer'.format(udid)
    args3 = 'adb -s {} shell getprop ro.product.name'.format(udid)
    platform_version = run_cmd(args1)
    devices_name = run_cmd(args2) + ' ' + run_cmd(args3)
    return platform_version, devices_name


def check_adb_status():
    """检查adb连接状态"""
    command = ['adb devices', 'adb kill-server', 'adb start-server']
    logger.info('开始获取adb连接状态')
    for item in command:
        p = subprocess.getstatusoutput(item)[1]
        if item == command[0]:
            if p.endswith('\tdevice\n'):
                logger.info('adb 连接正常')
                break
    else:
        p = subprocess.getstatusoutput(command[0])[1]
        if p.endswith('\tdevice\n'):
            logger.info('adb 连接正常')
        else:
            print('adb devices未获取到设备，请检查adb连接状态')
            logger.warning('adb devices未获取到设备，请检查adb连接状态')
    return p.endswith('\tdevice\n')


def check_appium_server_status(port=4723):
    """检测appium server是否启动"""
    url = 'http://127.0.0.1:{}/wd/hub/status'.format(port)
    try:
        r = requests.get(url)
        status = r.status_code
        if status == 200:
            logger.info('appium server成功运行{}'.format(url))
            return True
        else:
            logger.info(
                'appium server未成功运行{},status_code:{}'
                .format(url, status)
            )
            return False
    except ConnectionError:
        logger.info(
            'appium server未成功运行{},出现ConnectionError.'.format(url)
        )
        return False


def set_log(level, file_name='run.txt'):
    """
    设置日志打印格式
    """
    log_file = os.path.join(BASE_DIR, 'log/' + file_name)
    # if not os.path.isfile(log_file):
    #     os.mknod(log_file, 0o777)
    log_level_total = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARN,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }
    logger_f = logging.getLogger('main')
    logger_f.setLevel(logging.DEBUG)
    handler = TimedRotatingFileHandler(
        log_file, when='W6', encoding='utf-8', backupCount=2
    )
    handler.setLevel(log_level_total.get(level, logging.DEBUG))
    formatter = logging.Formatter(
        '%(asctime)s-%(funcName)s-%(levelname)s-%(message)s'
    )
    handler.setFormatter(formatter)
    logger_f.addHandler(handler)
    console = logging.StreamHandler(outputBuffer)
    formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
    console.setFormatter(formatter)
    logger_f.addHandler(console)
    return logger_f

logger = set_log(LOG_LEVEL)


def screen_shot(func):
    """截图装饰器"""
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception:
            args[0].uiHelper.save_screen_shot()
            raise
        else:
            return result
    return wrapper


def case(case_level):
    """
    设置case_level，在case运行失败时自动截图
    """
    def _case(func):
        # 为每个case设置用例级别case_level
        func.case_level = case_level.value
        # 将为case设定的level级别传进去

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info('START TEST:{}.{}'.format(
                    args[0].__class__.__name__, func.__name__)
                )
                result = func(*args, **kwargs)
            except Exception:
                # args[0]为传入args传入的第一个变量self
                args[0].uiHelper.save_screen_shot()
                raise
            else:
                return result
            finally:
                logger.info('END TEST:{}.{}'.format(
                    args[0].__class__.__name__, func.__name__)
                )
        return wrapper
    return _case


def web_view(func):
    """
    测试h5页面的装饰器,切换context最后再切换回来,若没有开启webview则跳过case
    """
    def wrapper(*args, **kwargs):
        self = args[0]
        context = self.uiHelper.get_contexts()
        if self.w_name in context:
            try:
                self.uiHelper.switch_context(self.w_name)
                func(*args, **kwargs)
            finally:
                self.uiHelper.switch_context(context[0])
        else:
            logger.info('获取到的context:{}'.format(context))
            raise unittest.SkipTest('未开启webview debug模式')
    return wrapper


def send_report(file):
    """发送带附件的邮件"""
    msg = MIMEMultipart()
    with open(file, 'rb') as f:
        mail_body = f.read()
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))  # 添加邮件正文
    att1 = MIMEText(mail_body, 'html', 'utf-8')  # 添加附件
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="result.html"'
    msg.attach(att1)
    msg['subject'] = Header(MAIL_HEADER, 'utf-8')  # 设定邮件标题
    msg['From'] = MAIL_HOST_USER
    msg['From'] = Header('Tester', 'utf-8')
    msg['To'] = MAIL_TO  # 收件人,设置多个收件人时用;隔开
    try:
        smtp = smtplib.SMTP(MAIL_HOST, MAIL_PORT)
        # smtp.set_debuglevel(1)
        smtp.login(MAIL_HOST_USER, MAIL_HOST_PASSWORD)  # 登录邮箱的账户和密码
        smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())
        smtp.quit()
        logger.info('测试报告发送成功!')
    except smtplib.SMTPException:
        error = traceback.format_exc()
        logger.warning(error)
        logger.info("测试报告发送失败!")


def create_report():
    """生成测试报告，并返回fail、error信息和生成的html文件"""
    test_dir = os.path.join(BASE_DIR, 'testcase')
    result_dir = os.path.join(BASE_DIR, 'report')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login*.py')
    now = time.strftime('%y-%m-%d_%H_%M_%S')
    filename = result_dir + '/' + now + '_result.html'
    # platform_version, devices_name = get_device_info(udid)
    with open(filename, 'wb') as fp:
        runner = BSTestRunner(
            stream=fp,
            verbosity=2,
            title=MAIL_HEADER,
            description='运行环境:' + DESIRED_CAPS['deviceName'] +
                        ' android ' + DESIRED_CAPS['platformVersion'] +
                        ' 测试apk: ' + DESIRED_CAPS['app'].split('\\')[-1]
        )
        logger.info('开始执行测试.')
        runner.run(discover)
        logger.info('测试执行完毕.')
    lists = os.listdir(result_dir)
    lists.sort()
    file_del = os.path.join(result_dir, lists[0])
    os.remove(file_del)     # 删除之前生成的测试报告
    file_new = os.path.join(result_dir, lists[-1])
    with open(file_new, 'r', encoding='utf-8') as f:
        html = f.read()
    # 匹配fail和error是否出现
    f = re.findall(r'<td class="text text-danger">.+</td>', html)[0] \
        .replace('</td>', '').replace('<td class="text text-danger">', '')
    e = re.findall(r'<td class="text text-warning">.+</td>', html)[0] \
        .replace('</td>', '').replace('<td class="text text-warning">', '')
    # 返回匹配的f和e以及读取到的html
    return {'fail': f, 'error': e, 'file': file_new, 'html': html}


def start_appium(port=4723):
    """
    启动appium服务
    :param port:
    :return:
    """
    args1 = 'netstat -ano |findstr {}'.format(port)
    logger.debug('开始查到{}端口是否被占用'.format(port))
    p1_stdout, p1_stderr = subprocess.Popen(
        args1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    ).communicate(timeout=30)
    if p1_stderr:
        logger.error(p1_stderr)
    if p1_stdout:
        data = p1_stdout.decode('utf-8').strip()
        logger.info('查找到的端口占用结果{}'.format(data))
        port_list = re.findall(r".*(\d{4}).*\s.*\s(\d{1,5})", data)
        logger.debug('匹配到的端口占用结果{}'.format(data))
        if port_list:
            # 剔除掉pid为0的
            port_list = [i for i in port_list if i[1] != '0']
            port_list = dict(port_list)
            logger.info('需要杀掉的进程号{}'.format(port_list))
            for i in port_list.keys():
                logger.info('端口{}被占用, 杀掉进程号{}'.format(i, port_list[i]))
                args2 = 'taskkill -PID {} -F'.format(port_list[i])
                p2_stdout, p2_stderr = subprocess.Popen(
                    args2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
                ).communicate(timeout=30)
                logger.info(p2_stdout.strip().decode('gbk'))
                logger.info(p2_stderr.strip().decode('gbk'))
    else:
        logger.info('端口{}未被占用'.format(port))
    args3 = 'appium --session-override'
    appium_log = os.path.join(BASE_DIR, 'log/appium.txt')
    appium_error_log = os.path.join(BASE_DIR, 'log/appium_error.txt')
    subprocess.Popen(
        args3, stdout=open(appium_log, 'w'),
        stderr=open(appium_error_log, 'a'),
        shell=True
    )
    time.sleep(10)


def get_package():
    """
    将需要测试的apk从192.168.88.90的机器下载到本地
    """
    remove_path = '/home/ftp/惠配通/安卓/auto'
    local_path = os.path.join(BASE_DIR, 'package')
    try:
        scp = paramiko.Transport(('192.168.xx.xx', 22))
        scp.connect(username='xxxx', password='xxxxxx')
        sftp = paramiko.SFTPClient.from_transport(scp)
        ssh = paramiko.SSHClient()
        ssh._transport = scp
        stdin, stdout, stderr = ssh.exec_command('ls /home/ftp/xxx/安卓/auto')
        try:
            if stdout.readlines:
                package_name = stdout.readlines()[-1].strip()
                remove_path = remove_path + '/' + package_name
                local_path = os.path.join(local_path, package_name)
                if not os.path.exists(local_path):
                    logger.info("开始从远程机器目录{}下载apk文件,请稍后.".format(remove_path))
                    sftp.get(remove_path, local_path)
                    if not os.path.exists(local_path):
                        logger.info("文件下载失败,请检查远程路径与本地目录.")
                        raise Exception('get apk failed.')
                    else:
                        logger.info("文件成功下载至{}".format(local_path))
                else:
                    logger.info("需要测试的apk已存在目录{}".format(local_path))
                DESIRED_CAPS['app'] = local_path
                config.write()
            else:
                logger.info('远程机器目录下{}未获取到apk文件'.format(remove_path))
                raise Exception('remote path not found apk.')
        finally:
            ssh.close()
            scp.close()
    except SSHException:
        logger.info('ssh连接远程服务失败,请检查远程机器是否连接正常.')
        raise

if __name__ == '__main__':
    # start_appium()
    print(DESIRED_CAPS['app'].split('\\')[-1])
