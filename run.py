import time
import threading
from base.batch_run import get_udids, get_ports, start_appium, run_case, kill_appium
from base.api import get_package, logger


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
                time.sleep(15)
            ths[1].join()
        finally:
            kill_appium()
    else:
        logger.warning('adb devices未获取到设备，请检查adb连接状态')

    # try:
    #     if check_adb_status():
    #         boot_time = 1
    #         DESIRED_CAPS['remoteHost'] = 'http://127.0.0.1:{}/wd/hub'.format(4723)
    #         config.write()
    #         while boot_time <= 3:
    #             if check_appium_server_status():
    #                 get_package()
    #                 report_info = create_report()
    #                 if report_info['fail'] != '0' or report_info['error'] != '0':
    #                     send_report(report_info['file'])
    #                 break
    #             logger.info('尝试第{}次启动appium server'.format(boot_time))
    #             start_appium()
    #             boot_time += 1
    #         else:
    #             logger.info('appium server 启动失败请检查本地运行环境.')
    # except Exception:
    #     error = traceback.format_exc()
    #     logger.error(error)
    #     raise
