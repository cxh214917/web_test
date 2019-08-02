# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/02 16:58
file:test_login.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""

import unittest
from selenium import webdriver
from web_framework_v1.PageObjects.login_page import LoginPage
from web_framework_v1.PageObjects.index_page import IndexPage

class TestLogin(unittest.TestCase):

    def setUp(self):
        """
        打开浏览器
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.get('http://120.78.128.25:8765/Index/login.html')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # 步骤
        LoginPage(self.driver).login("18684720553","python")
        # 断言
        self.assertTrue(IndexPage(self.driver).check_userName_exists())

    def test_login_noPasswd(self):
        # 步骤
        lp = LoginPage(self.driver)
        lp.login("18684720553", "")
        # 断言
        self.assertEqual("请输入密码",lp.get_form_error_info())

    def test_login_wrongPasswd(self):
        # 步骤
        lp = LoginPage(self.driver)
        lp.login("18684720000", "python")
        # 断言
        self.assertEqual("此账号没有经过授权，请联系管理员!",lp.get_page_center_error_info())