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

from web_framework_v4.TestDatas import bid_datas as BD
from web_framework_v4.PageObjects.index_page import IndexPage
from web_framework_v4.PageObjects.user_page import UserPage
from web_framework_v4.PageObjects.bid_page import BidPage
import pytest

@pytest.mark.usefixtures("init_login")
class TestInvest:

    def test_invest_success(self,init_login):
        """
        投资成功的测试用例
        :return:
        """
        # 步骤

        # 1、获取投资标名称
        invest_name = IndexPage(init_login).get_invested_bid_name()
        # 2、选择第一个标
        IndexPage(init_login).choice_first_bid()
        # 3、获取投标前的余额
        before_invest_money = BidPage(init_login).get_pre_invest_money()
        # 4、投标
        BidPage(init_login).invest()
        # 5、点击查看并激活
        BidPage(init_login).view_activate()
        # 6、投资后余额
        after_invest_money = UserPage(init_login).get_available_money_money()
        # 7、验证已投资项目名称
        invested_name = UserPage(init_login).check_investment_project_name()

        # 断言
        assert invest_name == invested_name
        assert eval(before_invest_money) - eval(after_invest_money) == BD.invest_money



