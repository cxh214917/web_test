# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/24 21:06
file:mouse_operation.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.maximize_window()
driver.get('http://www.baidu.com')

# //div[@id="u1"]//a[@name="tj_settingicon"]
# 找到元素
ele = driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_settingicon"]')
# 实例化ActionChains
ac = ActionChains(driver)
# 悬浮操作
ac.move_to_element(ele).click(ele)
# 执行鼠标操作
ac.perform()