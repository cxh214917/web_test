# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/15 17:36
file:basepage.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_framework_v4.Common.my_log import myLog
import time
import os
from web_framework_v4.Common.contant import IMG_PATH

class BasePage:

    def __init__(self,driver:WebDriver,timeout = 30,frequency = 0.5):
        self.drive = driver
        self.wait = WebDriverWait(self.drive,timeout,frequency)

    def save_img(self,img_description):
        """
        :param img_description:图片描述，格式为：页面名称_功能名
        :return:
        """
        img_path = os.path.join(IMG_PATH,(img_description + time.strftime('%Y-%m-%d %H_%M_%S') + ".png"))
        try:
            self.drive.save_screenshot(img_path)
        except:
            myLog.exception('网页截图失败!')
            raise
        else:
            myLog.info("截图成功，截图存放在 {}".format(img_path))

    def wait_element_exist(self,loc,img_description):
        """
        等待元素存在方法
        :param loc: 元素定位表达式
        :param img_description: 图片描述，格式为：页面名称_功能名
        :return:
        """
        start = time.time()
        try:
            self.wait.until(EC.presence_of_element_located(loc))
        except:
            myLog.exception("{} 页面 {} 元素不存在".format(img_description,loc))
            self.save_img(img_description)
            raise
        else:
            end = time.time()
            myLog.info("{} 页面 {} 元素存在，用时 {} 秒".format(img_description,loc,end-start))

    def wait_element_visible(self,loc,img_description):
        """
        等待元素可见方法
        :param loc: 元素定位表达式
        :param img_description: 图片描述，格式为：页面名称_功能名
        :return:
        """
        start = time.time()
        try:
            self.wait.until(EC.visibility_of_element_located(loc))
        except:
            myLog.exception("等待 {} 页面 {} 元素可见失败！".format(img_description,loc))
            self.save_img(img_description)
            raise
        else:
            end = time.time()
            myLog.info("等待 {} 页面 {} 元素可见成功，用时 {} 秒".format(img_description,loc,end-start))

    def get_element(self,loc,img_description):
        """
        查找元素方法
        :param loc: 元素定位表达式
        :param img_description: 图片描述，格式为：页面名称_功能名
        :return: element
        """
        start = time.time()
        try:
            element = self.drive.find_element(*loc)
        except:
            myLog.exception("查找 {} 页面 {} 元素失败!".format(img_description,loc))
            self.save_img(img_description)
            raise
        else:
            end = time.time()
            myLog.info("查找 {} 页面 {} 元素成功!用时 {} 秒".format(img_description,loc,end-start))
            return element

    def click_element(self,loc,img_description):
        """
        点击元素操作方法
        :param loc: 元素定位表达式
        :param img_description: 图片描述，格式为：页面名称_功能名
        :return: None
        """
        start = time.time()
        self.wait_element_visible(loc,img_description)
        element = self.get_element(loc,img_description)
        try:
            element.click()
        except:
            myLog.exception("点击 {} 页面 {} 元素失败!".format(img_description,loc))
            self.save_img(img_description)
            raise
        else:
            end = time.time()
            myLog.info("点击 {} 页面 {} 元素成功，用时 {} 秒".format(img_description,loc,end - start))

    def input_text(self,loc,value,img_description):
        """
        输入文本值方法
        :param loc: 元素定位表达式
        :param img_description: 图片描述，格式为：页面名称_功能名
        :param value: 输入的文本值
        :return: None
        """
        start = time.time()
        self.wait_element_visible(loc,img_description)
        ele = self.get_element(loc,img_description)
        try:
            ele.send_keys(value)
        except:
            myLog.exception("在 {} 页面 {} 元素上输入文本值 {} 失败!".format(img_description,loc,value))
            self.save_img(img_description)
            raise
        else:
            end = time.time()
            myLog.info("在 {} 页面 {} 元素上输入文本值 {} 成功，用时 {} 秒".format(img_description,loc,value,end-start))

    def get_text(self,loc,img_description):
        """
        获取元素文本值方法
        :param loc: 元素定位表达式
        :param img_description: 图片描述，格式为：页面名称_功能名
        :return:text（文本值）
        """
        start = time.time()
        self.wait_element_exist(loc,img_description)
        ele = self.get_element(loc,img_description)
        try:
            text = ele.text
        except:
            myLog.exception("获取 {} 页面 {} 元素的文本值失败!".format(img_description,loc))
            self.save_img(img_description)
            raise
        else:
            end = time.time()
            myLog.info("获取 {} 页面 {} 元素的文本值成功，用时 {} 秒".format(img_description,loc,end-start))
            return text

    def get_element_attribute(self,loc,name,img_description):
        """
        获取元素属性值方法
        :param loc: 元素定位表达式
        :param img_description: 图片描述，格式为:页面名称_功能名
        :param name: 属性名称
        :return: attr（属性值）
        """
        start = time.time()
        self.wait_element_exist(loc,img_description)
        ele = self.get_element(loc,img_description)
        try:
            attr = ele.get_attribute(name)
        except:
            myLog.exception("获取 {} 页面 {} 元素属性值失败!".format(img_description,loc))
            self.save_img(img_description)
            raise
        else:
            end = time.time()
            myLog.info("获取 {} 页面 {} 元素属性值成功，用时 {} 秒".format(img_description,loc,end-start))
            return attr

