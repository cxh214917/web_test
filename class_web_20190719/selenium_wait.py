# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/21 13:31
file:selenium_wait.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get('http://www.baidu.com')

# 隐形等待
driver.implicitly_wait(100)

driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()

# 显性等待
# TANGRAM__PSP_10__footerULoginBtn:用户名登录的ID
loc = (By.ID,'TANGRAM__PSP_10__footerULoginBtn')
WebDriverWait(driver,5).until(EC.visibility_of_element_located(loc))
time.sleep(1)
# driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
# driver.find_element_by_id(loc[1]).click()
driver.find_element(*loc).click()
