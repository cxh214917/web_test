# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/27 21:54
file:scroll_bar.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""

"""
1、移动到元素element对象的“底端”与当前窗口的“底部”对齐：
     driver.execute_script("arguments[0].scrollIntoView(false);",element)

2、移动到元素element对象的“顶端”与当前窗口的“顶部”对齐：
     driver.execute_script("arguments[0].scrollIntoView();",element)

3、移动到页面底部：
      driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

4、移动到页面顶部：
     driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('柠檬班',Keys.ENTER)

loc = (By.XPATH,'//a[text()="软件测试_百度百科"]')
wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located(loc))
ele = driver.find_element(*loc)

# 移动到元素element对象的“底端”与当前窗口的“底部”对齐
# js = "arguments[0].scrollIntoView(false)"
# driver.execute_script(js,ele)

# 移动到元素element对象的“顶端”与当前窗口的“顶部”对齐--没意义
# js = "arguments[0].scrollIntoView()"
# driver.execute_script(js,ele)

# 移动到页面底部
# js = "window.scrollTo(0,document.body.scrollHeight)"

# 移动到页面顶部-->鸡肋，直接加载就是顶端对齐
js = "window.scrollTo(document.body.scrollHeight,0)"
driver.execute_script(js)



