#-*- coding:utf8 -*-
from init.ios.demoPorject.demoProjectInit import DemoProjectInit

import ConfigParser

def ios_init():
    """
    初始化ios项目必要的数据
    :return:
    """
    config = ConfigParser.ConfigParser()
    config.read('config/ios/ios_init.conf')

    if 1==int(config.get('isInit','demoProject')):
        DemoProjectInit().init()