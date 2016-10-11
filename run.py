__author__ = 'Administrator'
import sys, time, os, re, logging
from logging.handlers import TimedRotatingFileHandler

sys.path.append('./interface')
from common.sendmail import sendreport
from common.create_report import create_report
from common.create_report import create_repAgain

logger = logging.getLogger('main')
logger.setLevel(logging.WARNING)
# handler=logging.FileHandler('G:/huipeitongUI/log/log.txt')
#设置日志为按时间过期删除日志,指定一天生成2个日志文件，保存15个日志文件（一周）,过期的会被自动删除掉
handler = TimedRotatingFileHandler('G:/huipeitongUI/log/log.txt', when='midnight', interval=1, backupCount=7)
handler.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

if __name__ == '__main__':
    output = os.popen('adb devices').read()
    if '\tdevice\n' in output:
        logger.warning('start testing...')
        report_info = create_report()
        #如果首次未通过，再将未通过的case执行一次case
        if report_info['fail'] != [] or report_info['error'] != []:
            logger.warning('start again...')
            report_info = create_repAgain(report_info['html'])
            #如果再次未通过就发送短信和邮件
            if report_info['fail'] != [] or report_info['error'] != []:
                send_outorfail = sendreport(report_info['file_new'])
                #判断邮件是否发送成功，未发送成功继续发送（总共发送3次）
                if send_outorfail != 0:
                    for i in range(3):
                        logger.warning('sendmail number: %s:', i)
                        send_outorfail = sendreport(report_info['file_new'])
                        if send_outorfail == 0:
                            break
        logger.warning('testing end!')
    else:
        logger.warning('please check whether the adb connection!')
        print('please check whether the adb connection!')