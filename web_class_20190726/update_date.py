# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/30 17:38
file:update_date.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.12306.cn/index/')

js = """
var a = document.getElementById("fromStationText");
var b = document.getElementById("fromStation");
var c = document.getElementById("toStationText");
var d = document.getElementById("toStation");
var e = document.getElementById("train_date");
a.value = arguments[0];
b.value = arguments[1];
c.value = arguments[2];
d.value = arguments[3];
e.readonly = false;
e.value = arguments[4];
"""
driver.execute_script(js,'上海','SHH','杭州东','HGH','2019-08-07')

loc_find = (By.XPATH,'//a[@id="search_one"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc_find))
driver.find_element(*loc_find).click()