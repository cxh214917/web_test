# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/04 15:28
file:index_page_locators.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
# 首页元素定位
from selenium.webdriver.common.by import By

# 用户名元素定位
user_name_exists_loc = (By.XPATH,'//a[contains(text(),"我的帐户")]')

# 投标按钮元素定位
bid_button_loc = (By.XPATH,'//a[@class="btn btn-special"]')

# 标名元素定位
bid_name_loc = (By.XPATH,'//span[@class="fs-22"]')