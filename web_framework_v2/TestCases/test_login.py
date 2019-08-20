# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/03 16:49
file:test_login.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
import unittest
import ddt
from selenium import webdriver
from web_framework_v2.TestDatas import login_datas as L_D
from web_framework_v2.TestDatas import common_datas as C_D
from web_framework_v2.PageObjects.login_page import LoginPage
from web_framework_v2.PageObjects.index_page import IndexPage

@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        """
        新建会话，最大化窗口，访问网址
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(C_D.login_url)

    def tearDown(self):
        self.driver.quit()

    @ddt.data(*L_D.success)
    def test_login_success(self,data):
        """
        登陆成功-->用户名和账号均正确
        :return:
        """
        # 步骤
        LoginPage(self.driver).login(data['username'],data['passwd'])
        # 断言
        self.assertTrue(IndexPage(self.driver).check_userName_exists())

    @ddt.data(*L_D.Invalid_data_01)
    def test_login_usernameIsOk_passwdIsWrong(self,data):
        """
        登陆失败-->用户名正确，密码错误
        :return:
        """
        # 步骤
        LoginPage(self.driver).login(data["username"],data["passwd"])
        # 断言
        self.assertEqual(data["check_info"],LoginPage(self.driver).get_page_center_error_info())

    @ddt.data(*L_D.Invalid_data_02)
    def test_login_usernameIsFormat_passwdIsNone(self,data):
        """
        用户名格式合法，密码为空
        :return:
        """
        # 步骤
        LoginPage(self.driver).login(data["username"],data["passwd"])
        # 断言
        self.assertEqual(data["check_info"],LoginPage(self.driver).get_form_error_info())

    @ddt.data(*L_D.Invalid_data_03)
    def test_usernameNotRegister_passwdNotNone(self,data):
        """
        用户名合法且未注册，密码不为空
        :return:
        """
        # 步骤
        LoginPage(self.driver).login(data["username"],data["passwd"])
        # 断言
        self.assertEqual(data["check_info"],LoginPage(self.driver).get_page_center_error_info())

    @ddt.data(*L_D.Invalid_data_04)
    def test_usernameNotFormat_passwd(self,data):
        """
        用户名不合法-->密码不用管，断言从上往下执行
        :return:
        """
        # 步骤
        LoginPage(self.driver).login(data["username"],data["passwd"])
        # 断言==也可以用以下断言
        # self.assertIn(LoginPage(self.driver).get_form_error_info(),'["请输入正确的手机号","请输入密码"]')
        self.assertEqual(data["check_info"],LoginPage(self.driver).get_form_error_info())

    @ddt.data(*L_D.Invalid_data_05)
    def test_usernameIsNone_passwd(self,data):
        """
        用户名为空，密码随意
        :return:
        """
        # 步骤
        LoginPage(self.driver).login(data["username"],data["passwd"])
        # 断言
        self.assertEqual(data["check_info"],LoginPage(self.driver).get_form_error_info())