#-*-coding:utf-8-*- 
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BaseApp():
    def __init__(self,driver):
        self.driver=driver
        self.fenbianlv=self.driver.get_window_size()
    def find(self,locator):
        # locator 穿字典 {"name": "输入账号", "by": "id", "value": "xxx", "timeout": "10"}
        timeout=30
        if "name" in locator["name"]:
            print("正在定位元素名称{}".format(locator['name'])+",定位方法: {}-->{}".format(locator['by'], locator['value']))
        if locator["by"]=="desc":
            # 通过desc定位
            value=locator["value"]
            elements=WebDriverWait(self.driver,timeout,0.5).until(lambda x:x.find_element_by_accessibility_id(value))
        elif locator["by"]=="text":
            # 通过text定位
            # ("//*[contains(@text, '同意')])"
            value="//*[contains(@text, '{}')]".format(locator["value"])
            elements=WebDriverWait(self.driver,timeout,0.5).until(lambda x:x.find_element_by_xpath(value))
        elif locator["by"]=="id":
            # 通过id定位
            value=locator["value"]
            elements=WebDriverWait(self.driver,timeout,0.5).until(lambda x:x.find_element_by_id(value))
        else:
            loc=(locator["by"],locator["value"])
            elements=WebDriverWait(self.driver,timeout,0.5).until(lambda x:x.find_element_by_xpath(loc))
        return elements

    def click(self,locator):
        el=self.find(locator)
        el.click()
    def send_text(self,locator,text):
        el=self.find(locator)
        el.send_keys(text)
    def clear(self,locator):
        el=self.find(locator)
        el.clear()
    def swipe_left(self,w1=0.8,w2=0.2,h=0.2,n=1):
        x1 = self.fenbianlv['width']*w1
        y1 = self.fenbianlv['height'] *h
        x2 = self.fenbianlv['width']/w2
        y2 = self.fenbianlv['height'] *h
        for i in range(n):
            self.driver.swipe(x1, y1,  x2, y2, 500)
    def swipe_right(self,w1=0.2,w2=0.8,h=0.2,n=1):
        x1 = self.fenbianlv['width']*w1
        y1 = self.fenbianlv['height'] *h
        x2 = self.fenbianlv['width'] *w2
        y2 = self.fenbianlv['height'] *h
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y2, 500)
    def swipe_up(self,h1=0.8,h2=0.2,w=0.5, n=1):
        x1 = self.fenbianlv['width']*w
        y1 = self.fenbianlv['height'] *h1
        x2 = self.fenbianlv['width']*w
        y2 = self.fenbianlv['height'] *h2
        for i in range(n):
            self.driver.swipe(x1, y1,  x2, y2, 500)
    def swipe_down(self, h1=0.2,h2=0.8,w=0.5, n=1):
        x1 = self.fenbianlv['width']*w
        y1 = self.fenbianlv['height'] *h1
        x2 = self.fenbianlv['width']*w
        y2 = self.fenbianlv['height'] *h2
        for i in range(n):
            self.driver.swipe(x1, y1,  x2, y2, 500)
    def is_element_exist(self,locator):
        els=[]
        els.append(self.find(locator))
        print(len(els))
        if len(els)<=0:
            return False
        else:
            return True

