#-*-coding:utf-8-*- 
from selenium import webdriver
from appium import webdriver
import time
from common.base import BaseApp
from page_obj.page_element.pages import *
from page_obj.login_api import Login

class Integral(BaseApp):
    首页兑分=duifen.首页兑分
    工行极速=duifen.工行极速
    建设标准=duifen.建设标准
    招商全清=duifen.招商全清
    中国银行=duifen.中国银行
    试算收益=duifen.试算收益
    def click_duifen(self):
        self.click(self.首页兑分)
    def income(self):
        time.sleep(2)
        print(self.is_element_exist(self.工行极速))
        # self.click(self.中国银行)
        # self.click(self.试算收益)
        self.send_text(self.试算收益,"80000")
        time.sleep(3)
        self.click(self.中国银行)
        self.click(self.试算收益)
        self.send_text(self.试算收益, "80000")
        # time.sleep(3)
        # self.click(self.china)
        # self.send_text(self.try_income, "80000")
    def income_action(self):
        self.click_duifen()
        self.income()
if __name__ == "__main__":
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '534f2f8',  # 534f2f8 be63dcec
        'platformVersion': '7.0',
        # apk 包名
        # 'noReset':True,
        'appPackage': 'com.bhsgd.jifenapp',
        # apk 的 launcherActivity
        'appActivity': 'com.bhsgd.jifenapp.MainActivity',
        # 用appium的自带键盘
        'unicodeKeyboard': False,
        'resetKeyboard': False
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(5)
    login_=Login(driver)
    login_.login_action("17666522464","123456")
    time.sleep(1)
    integral_=Integral(driver)
    integral_.income_action()



