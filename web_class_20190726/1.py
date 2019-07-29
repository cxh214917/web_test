# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/29 13:46
file:1.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('柠檬班',Keys.ENTER)

wait = WebDriverWait(driver,10)
loc = (By.XPATH,'//a[text()="-CSDN学院r"]')
wait.until(EC.visibility_of_element_located(loc))

ele = driver.find_element(*loc)

js = 'arguments[0].scrollIntoView(false)'
driver.execute_script(js,ele)

time.sleep(3)

driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')