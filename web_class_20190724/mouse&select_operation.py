# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/27 11:25
file:mouse_operation.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')

# //div[@id="u1"]//a[text()="设置"]---->“设置”定位表达式
# 找到元素
ele = driver.find_element_by_xpath('//div[@id="u1"]//a[text()="设置"]')

# 实例化对象
ac = ActionChains(driver)

# 鼠标悬浮
ac.move_to_element(ele).click(ele)

# 执行鼠标操作
ac.perform()

# 等待元素可见并点击
wait = WebDriverWait(driver,10)
loc = (By.XPATH,'//a[text()="高级搜索"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 等待下拉列表元素可见
loc = (By.XPATH,'//select[@name="ft"]')
wait.until(EC.visibility_of_element_located(loc))
sel_ele = driver.find_element(*loc)

# 初始化Select类并选择元素
s = Select(sel_ele)
# s.select_by_index(1)
# s.select_by_value('pdf')
s.select_by_visible_text('Adobe Acrobat PDF (.pdf)')