# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/09 12:49
file:user_page.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""

from web_framework_v3.Common.basepage import BasePage
from web_framework_v3.PageLocators import user_page_locators as U_P_loc

class UserPage(BasePage):

    def get_available_money_money(self):
        """
        获取用户投资后可用余额方法
        :return: 用户可用余额
        """
        return self.get_text(U_P_loc.user_available_money_loc,"个人信息页面_获取投资后余额").strip("元")

    def check_investment_project_name(self):
        """
        获取验证投资项目名方法
        :return: 投资项目名称
        """
        self.click_element(U_P_loc.investment_projects_loc,"个人信息页面_点击投资项目")
        return self.get_text(U_P_loc.invested_projects_loc,"个人信息页面_获取已投资项目名")


