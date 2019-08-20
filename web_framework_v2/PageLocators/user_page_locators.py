# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/09 13:02
file:user_page_locators.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
from selenium.webdriver.common.by import By

# 可用余额定位表达式
user_available_money_loc = (By.XPATH,'//li[@class="color_sub"]')

# 投资项目定位表达式
investment_projects_loc = (By.XPATH,'//div[text()="投资项目"]')

# 已投资项目定位表达式
invested_projects_loc = (By.XPATH,'//div[@class="deal_tab_font1"]/child::a')
