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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('12306',Keys.ENTER)
wins = driver.window_handles

loc = (By.XPATH,'//a[text()="铁道部火车票网上订票唯一官网 - 铁路客户服务中心"]')
wait = WebDriverWait(driver,20)
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

wait.until(EC.new_window_is_opened(wins))
wins = driver.window_handles
driver.switch_to.window(wins[-1])

loc_from = (By.XPATH,'//input[@id="fromStation"]/following-sibling::input')
wait.until(EC.visibility_of_element_located(loc_from))
from_station = driver.find_element(*loc_from)

loc_to = (By.XPATH,'//input[@id="toStationText"]/parent::div')
wait.until(EC.visibility_of_element_located(loc_to))
to_station = driver.find_element(*loc_to)

loc_date = (By.XPATH,'//input[@id="train_date"]')
wait.until(EC.visibility_of_element_located(loc_date))
date = driver.find_element(*loc_date)

time.sleep(3)
js = """
var a = document.getElementById("fromStationText");
var b = document.getElementById("fromStation");
var c = document.getElementById("toStationText");
var d = document.getElementById("toStation");
var e = document.getElementById("train_date");
a.value = '上海';
b.value = 'SHH';
c.value = '杭州东';
d.value = 'HGH';
e.readonly = false;
e.value = '2019-08-07';
"""
driver.execute_script(js,from_station,to_station,date)
time.sleep(3)

loc_find = (By.XPATH,'//a[@id="search_one"]')
wait.until(EC.visibility_of_element_located(loc_find))
driver.find_element(*loc_find).click()