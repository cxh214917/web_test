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

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_framework_v2.PageLocators import bid_page_locators as B_P_loc
from web_framework_v2.TestDatas import bid_datas as BD

class BidPage:
    """
    封装标页面的功能类
    """

    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)

    def get_pre_invest_money(self):
        """
        获取投资前余额的方法
        :return: 投资前金额
        """
        self.wait.until(EC.visibility_of_element_located(B_P_loc.user_left_money_loc))
        return self.driver.find_element(*B_P_loc.user_left_money_loc).get_attribute('data-amount')

    def invest(self):
        """
        等待投标输入框出现，输入投资金额，点击投标
        :return:
        """
        self.wait.until(EC.visibility_of_element_located(B_P_loc.user_invest_money_loc))
        self.driver.find_element(*B_P_loc.user_invest_money_loc).send_keys(BD.invest_money)
        self.driver.find_element(*B_P_loc.bid_money_button_loc).click()

    def view_activate(self):
        """
        查看并激活
        :return:
        """
        self.wait.until(EC.visibility_of_element_located(B_P_loc.view_activate_button_loc))
        self.driver.find_element(*B_P_loc.view_activate_button_loc).click()




