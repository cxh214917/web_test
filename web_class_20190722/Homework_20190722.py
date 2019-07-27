# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/24 16:06
file:Homework_20190722.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 打开浏览器，并且窗口最大化
driver = webdriver.Chrome()
driver.maximize_window()

# 进到百度主页
driver.get('http://www.baidu.com')

# 搜索腾讯课堂
driver.find_element_by_id('kw').send_keys('腾讯课堂')
driver.find_element_by_id('su').click()

# 等待腾讯课堂加载完毕后点击进入
wait = WebDriverWait(driver,20)
wait.until(EC.visibility_of_element_located((By.XPATH,'//a[text()="_专业的在线教育平台(ke.qq.com)"]')))
driver.find_element_by_xpath('//a[text()="_专业的在线教育平台(ke.qq.com)"]').click()

# 获取当前句柄，切换到最新打开的页面
wins = driver.window_handles
driver.switch_to.window(wins[-1])

# 点击腾讯课堂登录按钮
loc = (By.XPATH,'//a[text()="登录"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 等待元素加载完全选择QQ登录
loc = (By.XPATH,'//a[text()="QQ登录"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 切换进入iframe页面:要唯一定位

# ①通过name属性
loc = (By.XPATH,'//iframe[@name="login_frame_qq"]')
# wait.until(EC.visibility_of_element_located(loc))
# driver.switch_to.frame("login_frame_qq")

# ②一步到位:等待加切换
wait.until(EC.frame_to_be_available_and_switch_to_it(loc))

# 切换到页面后点击“帐号密码登录”
wait.until(EC.visibility_of_element_located((By.XPATH,'//a[text()="帐号密码登录"]')))
driver.find_element_by_xpath('//a[text()="帐号密码登录"]').click()

# driver.find_element_by_id("u").send_keys('2904504961')
# driver.find_element_by_id("p").send_keys('*********')
# driver.find_element_by_xpath('//input[@type="submit"]').click()


