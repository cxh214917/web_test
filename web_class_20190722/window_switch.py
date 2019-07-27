# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/23 23:08
file:window_switch.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 加载驱动
driver = webdriver.Chrome()

# 打开百度首页，获取当前句柄
driver.get('http://www.baidu.com')
print(driver.current_window_handle)

# 获取所有句柄
wins = driver.window_handles
print("所有窗口-0：",wins)

# 搜索框中输入“柠檬班”并点击
driver.find_element_by_id('kw').send_keys('柠檬班')
driver.find_element_by_id('su').click()

# 实例化wait类，通过定位表达式等待腾讯课堂可见并点击
wait = WebDriverWait(driver,20)
wait.until(EC.visibility_of_element_located((By.XPATH,'//a[text()="_腾讯课堂"]')))
driver.find_element_by_xpath('//a[text()="_腾讯课堂"]').click()

# 等待新窗口可见并获取当前所有窗口句柄
wait.until(EC.new_window_is_opened(wins))
wins = driver.window_handles
print("所有窗口-1：",wins)

# 切换到最新开启的窗口
driver.switch_to.window(wins[-1])
loc = (By.XPATH,'//section//h2[contains(text(),"老师")]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()