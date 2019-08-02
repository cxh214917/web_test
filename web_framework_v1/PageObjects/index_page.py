# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/01 16:18
file:index_page.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IndexPage:
    # 用户昵称定位
    userName_loc = (By.XPATH,'//a[contains(text(),"我的帐户")]')

    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)

    def check_userName_exists(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.userName_loc))
            return True
        except:
            return False
