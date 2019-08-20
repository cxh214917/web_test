# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/04 15:25
file:index_page.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""

from web_framework_v4.Common.basepage import BasePage
from web_framework_v4.PageLocators import index_page_locators as I_P_loc

class IndexPage(BasePage):

    def check_username_exists(self):
        """
        用来检测用户是否登录
        :return:
        """
        try:
            self.wait_element_exist(I_P_loc.user_name_exists_loc,"标首页_等待用户名存在")
            return True
        except:
            return False

    def choice_first_bid(self):
        """
        选择第一个标
        :return:
        """
        self.click_element(I_P_loc.bid_button_loc,"标首页_点击抢投标按钮")

    def get_invested_bid_name(self):
        """
        获取已投的标名
        :return: 标名
        """
        return self.get_text(I_P_loc.bid_name_loc,"标首页_获取已投标标名")
