import re
from base.setting import *
from base.api import run_cmd


def get_web_view_version():
    """
    获取android system webview 版本号
    """
    try:
        info = run_cmd('adb shell dumpsys package com.google.android.webview')
        if not info:
            info = run_cmd('adb shell dumpsys package com.android.webview')
        version = re.findall('versionName=(.+)', info)
        version = int(version[0].split('.')[0])
    except Exception:
        version = None
    return version

web_view_chrome_dict = {
    '2.30': [59, 60],
    '2.29': [56, 57, 58],
    '2.26': [53, 54, 55],
    '2.22': [49, 50, 51, 52],
    '2.20': [43, 44, 45, 46, 47, 48],
    '2.14': [39, 40, 41, 42],
    '2.11': [36, 37, 38],
}


def get_chrome_driver_version():
    """
    得到chrome driver版本
    """
    version = get_web_view_version()
    if version:
        for j, k in web_view_chrome_dict.items():
            if version in k:
                return j
        else:
            return
    else:
        return


def get_chrome_path():
    """
    得到对应版本的chrome driver的路径
    """
    version = get_chrome_driver_version()
    if version:
        path = os.path.join(BASE_DIR, ('chromedriver\\' + version + '.exe'))
        return path
    else:
        return

if __name__ == '__main__':
    p = get_chrome_path()
    print(p)
