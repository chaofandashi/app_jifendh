#-*-coding:utf-8-*- 
from selenium import webdriver
from appium import webdriver
import time
from common.base import BaseApp
from page_obj.page_element.pages import *
class Login(BaseApp):
    我 = login.我的
    账号 = login.输入账号
    密码 = login.输入密码
    登录=login.登录
    def click_my(self):
        self.click(self.我)
    def input_username(self,username):
        self.clear(self.账号)
        self.send_text(self.账号,username)
    def input_pwd(self,pwd):
        self.clear(self.密码)
        self.send_text(self.密码,pwd)
    def click_login(self):
        self.click(self.登录)
    def login_action(self,user,pwd):
        self.click_my()
        self.input_username(user)
        self.input_pwd(pwd)
        self.click_login()


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
    time.sleep(10)
    login_=Login(driver)
    login_.login_action("17666522464","123456")



