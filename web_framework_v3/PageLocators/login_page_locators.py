# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/03 16:35
file:login_page_locator.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
from selenium.webdriver.common.by import By

# 用户名输入框
username_loc = (By.XPATH,'//input[@name="phone"]')

# 密码输入框
passwd_loc = (By.XPATH,'//input[@name="password"]')

# 登录按钮
button_loc = (By.XPATH,'//button')

# 表单错误信息提示
form_error_info_loc = (By.XPATH,'//div[@class="form-error-info"]')

# 获取页面中间错误信息
page_center_error_info = (By.XPATH,'//div[@class="layui-layer-content"]')