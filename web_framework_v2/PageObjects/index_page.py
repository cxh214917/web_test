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

from selenium.webdriver.remote.webdriver import WebDriver
from web_framework_v2.PageLocators import index_page_locators as I_P_loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IndexPage:

    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)

    def check_userName_exists(self):
        """
        用来检测用户是否登录
        :return:
        """
        try:
            self.wait.until(EC.visibility_of_element_located(I_P_loc.user_name_exists_loc))
            return True
        except:
            return False

    def choice_first_bid(self):
        """
        选择第一个标
        :return:
        """
        self.wait.until(EC.visibility_of_element_located(I_P_loc.bid_button_loc))
        self.driver.find_element(*I_P_loc.bid_button_loc).click()

    def get_invested_bid_name(self):
        """
        获取已投的标名
        :return:
        """
        self.wait.until(EC.visibility_of_element_located(I_P_loc.bid_name_loc))
        return self.driver.find_element(*I_P_loc.bid_name_loc).text
