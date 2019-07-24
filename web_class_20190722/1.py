# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/24 10:42
file:1.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
print(driver.current_window_handle)

wins = driver.window_handles
print('当前所有窗口-0：',wins)

driver.find_element_by_id('kw').send_keys('柠檬班')
driver.find_element_by_id('su').click()

wait = WebDriverWait(driver,20)
wait.until(EC.visibility_of_element_located((By.XPATH,'//a[text()="_腾讯课堂"]')))

driver.find_element_by_xpath('//a[text()="_腾讯课堂"]').click()

wait.until(EC.new_window_is_opened(wins))

wins = driver.window_handles
print('当前所有窗口-1：',wins)

driver.switch_to.window(wins[-1])
loc = (By.XPATH,'//section//h2[contains(text(),"老师")]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()