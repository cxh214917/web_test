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
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_framework_v2.PageLocators import user_page_locators as U_P_loc


class UserPage:

    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)

    def get_available_money_money(self):
        """
        获取用户投资后可用余额方法
        :return: 用户可用余额
        """
        self.wait.until(EC.visibility_of_element_located(U_P_loc.user_available_money_loc))
        return self.driver.find_element(*U_P_loc.user_available_money_loc).text.strip("元")

    def check_investment_project_name(self):
        """
        获取验证投资项目名方法
        :return: 投资项目名称
        """
        self.wait.until(EC.visibility_of_element_located(U_P_loc.investment_projects_loc))
        self.driver.find_element(*U_P_loc.investment_projects_loc).click()
        self.wait.until(EC.visibility_of_element_located(U_P_loc.invested_projects_loc))
        return self.driver.find_element(*U_P_loc.invested_projects_loc).text

