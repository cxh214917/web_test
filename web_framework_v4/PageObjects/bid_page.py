# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/08 19:02
file:bid_page.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""

from web_framework_v4.PageLocators import bid_page_locators as B_P_loc
from web_framework_v4.TestDatas import bid_datas as BD
from web_framework_v4.Common.basepage import BasePage

class BidPage(BasePage):
    """
    封装标页面的功能类
    """

    def get_pre_invest_money(self):
        """
        获取投资前余额的方法
        :return: 投资前金额
        """
        return self.get_element_attribute(B_P_loc.user_left_money_loc,"data-amount","标页面_获取用户投资前余额")

    def invest(self):
        """
        等待投标输入框出现，输入投资金额，点击投标
        :return:
        """
        self.input_text(B_P_loc.user_invest_money_loc,BD.invest_money,"标页面_输入投标金额")
        self.click_element(B_P_loc.bid_money_button_loc,"标页面_点击投标按钮")

    def view_activate(self):
        """
        查看并激活
        :return:
        """
        self.click_element(B_P_loc.view_activate_button_loc,"标页面_点击查看并激活按钮")





