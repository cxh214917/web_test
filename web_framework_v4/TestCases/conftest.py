# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/19 22:48
file:conftest.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
import pytest
from web_framework_v4.Common.my_log import myLog
from selenium import webdriver
from web_framework_v4.TestDatas import common_datas as C_D
from web_framework_v4.PageObjects.login_page import LoginPage

@pytest.fixture
def init_driver():
    """
    初始化driver：新建会话，最大化窗口，访问网址
    :return: driver
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(C_D.login_url)
    yield driver
    driver.quit()

@pytest.fixture
@pytest.mark.usefixtures("init_driver")
def init_login(init_driver):
    """
    login success
    :return:
    """
    myLog.info("开始执行测试：开启会话，打开网页，成功登陆")
    LoginPage(init_driver).login(C_D.user_01, C_D.passwd)
    yield init_driver
