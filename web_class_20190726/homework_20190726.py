# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/29 16:06
file:homework_20190726.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""

# 滚动条处理

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from web_class_20190726.file_upload import upload
import os

driver = webdriver.Chrome()
driver.maximize_window()
wins = driver.window_handles

driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('柠檬班',Keys.ENTER)

wait = WebDriverWait(driver,20)
# ==================第一题:js处理滚动条
loc = (By.XPATH,'//a[text()="-CSDN学院"]')
wait.until(EC.visibility_of_element_located(loc))

ele = driver.find_element(*loc)

# 元素对象与窗口底部对齐
driver.execute_script('arguments[0].scrollIntoView(false)',ele)

time.sleep(1)

# 页面滚动到最底端
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

# 元素对象与窗口顶部对齐:
#     driver.execute_script('arguments[0].scrollIntoView()')
# 以及页面滚到顶端:
#     driver.execute_script('window.scrollTo(document.body.scrollHeight,0)')
# 没意义
time.sleep(1)

# ==================第二题:js处理12306的日期框
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('12306',Keys.ENTER)

loc = (By.XPATH,'//a[text()="铁道部火车票网上订票唯一官网 - 铁路客户服务中心"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

wait.until(EC.new_window_is_opened(wins))
wins = driver.window_handles
driver.switch_to.window(wins[-1])

loc = (By.XPATH,'//input[@id="train_date"]')
wait.until(EC.visibility_of_element_located(loc))

ele = driver.find_element_by_id('train_date')
js = """
var a = document.getElementById('train_date');
a.readOnly = false;
a.value = '2019-08-07'
"""
time.sleep(5)    #等待页面加载完毕再更改日期，否则显示当前日期
driver.execute_script(js,ele)

# ==================第三题:上传操作
driver.implicitly_wait(5)
driver.switch_to.window(wins[0])

driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('课堂派',Keys.ENTER)

loc = (By.XPATH,'//a[text()="ketangpai-简单好用的互动课堂管理工具"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

wait.until(EC.new_window_is_opened(wins))
wins = driver.window_handles
driver.switch_to.window(wins[-1])

loc = (By.XPATH,'//a[text()="登录"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

loc = (By.XPATH,'//input[@placeholder="邮箱/账号/手机号"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys('18936368721')
driver.find_element_by_xpath('//input[@name="pass"]').send_keys('cxh214917')
driver.find_element_by_xpath('//div[@class="opt clearfix"]/following-sibling::a').click()

loc = (By.XPATH,'//a[text()="0726-元素操作作业-同步上课代码+完成12306查询车票"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()


BASE_PATH = os.path.dirname(__file__)
HOMEWORK_PATH = os.path.join(BASE_PATH,'homework_20190726.py').replace('/','\\')
FILE_UPLOAD_PATH = os.path.join(BASE_PATH,'file_upload.py').replace('/','\\')

# 首次提交作业，后续操作终断也行
# for i in [HOMEWORK_PATH,FILE_UPLOAD_PATH]:
#     loc = (By.XPATH, '//a[@class="sc-btn webuploader-container"]')
#     wait.until(EC.visibility_of_element_located(loc))
#     driver.find_element(*loc).click()
#     time.sleep(2)
#     upload(i)


# 更新作业
loc = (By.XPATH, '//a[@class="new-tj1" and text()="更新提交"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

loc = (By.XPATH,'//a[@class="sure active" and text()="确定"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

for i in range(2):
    loc = (By.XPATH, '//a[@class="cancel hide"]')
    wait.until(EC.visibility_of_element_located(loc))
    driver.find_element(*loc).click()

for i in [HOMEWORK_PATH,FILE_UPLOAD_PATH]:
    loc = (By.XPATH, '//a[@class="sc-btn webuploader-container"]')
    wait.until(EC.visibility_of_element_located(loc))
    driver.find_element(*loc).click()
    time.sleep(2)
    upload(i)

time.sleep(1)
loc = (By.XPATH,'//a[text()="更新提交" and @class="new-tj2 active"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

time.sleep(3)
loc = (By.XPATH,'//a[text()="知道了"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

time.sleep(3)
driver.quit()




