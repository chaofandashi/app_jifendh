# -*- coding: utf-8 -*-

from page_obj.page_element import tools

pages = tools.parseyaml()


def get_locater(clazz_name, method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator


class duifen:
    首页兑分 = get_locater('duifen', '首页兑分')
    工行极速 = get_locater('duifen', '工行极速')
    建设标准 = get_locater('duifen', '建设标准')
    招商全清 = get_locater('duifen', '招商全清')
    中国银行 = get_locater('duifen', '中国银行')
    试算收益 = get_locater('duifen', '试算收益')

    
class login:
    我的 = get_locater('login', '我的')
    输入账号 = get_locater('login', '输入账号')
    输入密码 = get_locater('login', '输入密码')
    登录 = get_locater('login', '登录')

    