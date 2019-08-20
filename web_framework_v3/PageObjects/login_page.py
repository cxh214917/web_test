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

from web_framework_v3.PageLocators import login_page_locators as L_P_loc
from web_framework_v3.Common.basepage import BasePage

class LoginPage(BasePage):
    """
    封装登录页面的功能类
    """

    def login(self,username,passwd):
        """
        登录成功-->用户名和密码均正确
        :param username: 登录用户名
        :param passwd: 登录密码
        :return:
        """
        self.input_text(L_P_loc.username_loc, username, "登录页面_输入用户名")
        self.input_text(L_P_loc.passwd_loc,passwd,"登录页面_输入密码")
        self.click_element(L_P_loc.button_loc,"登录页面_点击登录按钮")

    def get_form_error_info(self):
        """
        获取表单错误信息
        :return:
        """
        return self.get_text(L_P_loc.form_error_info_loc,"登录页面_获取表单错误信息")

    def get_page_center_error_info(self):
        """
        获取页面中间的错误信息
        :return:
        """
        return self.get_text(L_P_loc.page_center_error_info,"登录页面_获取页面中间的错误信息")





