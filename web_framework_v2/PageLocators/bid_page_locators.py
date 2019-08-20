# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/09 12:18
file:bid_page_locators.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
from selenium.webdriver.common.by import By

# 投资前用户余额定位表达式
user_left_money_loc = (By.XPATH,'//div[@class="clearfix left"]//input')

# 投资金额输入框表达式
user_invest_money_loc = (By.XPATH,'//input[@class="form-control invest-unit-investinput"]')

# 投标按钮定位表达式
bid_money_button_loc = (By.XPATH,'//button[@class="btn btn-special height_style"]')

# 查看并激活定位表达式
view_activate_button_loc = (By.XPATH,'//div[text()="投标成功！"]/following::button[text()="查看并激活"]')