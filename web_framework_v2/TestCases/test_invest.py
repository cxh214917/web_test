# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/08 16:55
file:test_invest.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from web_framework_v2.TestDatas import common_datas as CD
from web_framework_v2.TestDatas import bid_datas as BD
from web_framework_v2.PageObjects.login_page import LoginPage
from web_framework_v2.PageObjects.index_page import IndexPage
from web_framework_v2.PageObjects.user_page import UserPage
from web_framework_v2.PageObjects.bid_page import BidPage


class TestInvest(unittest.TestCase):

    def setUp(self):
        """
        打开网页\帐号登陆成功
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(CD.login_url)
        LoginPage(self.driver).login(CD.user_01,CD.passwd)
        self.wait = WebDriverWait(self.driver,20)

    def tearDown(self):
        self.driver.quit()

    def test_invest_success(self):
        """
        投资成功的测试用例
        :return:
        """
        # 步骤

        # 1、获取投资标名称
        invest_name = IndexPage(self.driver).get_invested_bid_name()
        # 2、选择第一个标
        IndexPage(self.driver).choice_first_bid()
        # 3、获取投标前的余额
        before_invest_money = BidPage(self.driver).get_pre_invest_money()
        # 4、投标
        BidPage(self.driver).invest()
        # 5、点击查看并激活
        BidPage(self.driver).view_activate()
        # 6、投资后余额
        after_invest_money = UserPage(self.driver).get_available_money_money()
        # 7、验证已投资项目名称
        invested_name = UserPage(self.driver).check_investment_project_name()

        # 断言
        self.assertEqual(invest_name, invested_name)
        self.assertEqual(eval(before_invest_money) - eval(after_invest_money),BD.invest_money)




