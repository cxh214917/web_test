# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/27 15:25
file:Keyboard_operation.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')

driver.find_element_by_id('kw').send_keys('柠檬班',Keys.ENTER)