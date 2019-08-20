# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/03 16:25
file:login_page.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_framework_v2.PageLocators import login_page_locators as L_P_loc

class LoginPage:
    """
    封装登录页面的功能类
    """

    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)

    def login(self,username,passwd):
        """
        登录成功-->用户名和密码均正确
        :param username: 登录用户名
        :param passwd: 登录密码
        :return:
        """
        self.wait.until(EC.visibility_of_element_located(L_P_loc.username_loc))
        self.driver.find_element(*L_P_loc.username_loc).send_keys(username)
        self.driver.find_element(*L_P_loc.passwd_loc).send_keys(passwd)
        self.driver.find_element(*L_P_loc.button_loc).click()

    def get_form_error_info(self):
        """
        获取表单错误信息
        :return:
        """
        self.wait.until(EC.visibility_of_element_located(L_P_loc.form_error_info_loc))
        return self.driver.find_element(*L_P_loc.form_error_info_loc).text

    def get_page_center_error_info(self):
        """
        获取页面中间的错误信息
        :return:
        """
        self.wait.until(EC.visibility_of_element_located(L_P_loc.page_center_error_info))
        return self.driver.find_element(*L_P_loc.page_center_error_info).text





