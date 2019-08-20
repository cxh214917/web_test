# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/16 20:29
file:test_suite.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
import unittest
import os
from web_framework_v3.Libraries.HTMLTestRunnerNew import HTMLTestRunner
from web_framework_v3.Common.contant import CASE_PATH,REPORT_PATH

suite = unittest.TestSuite()

loader = unittest.TestLoader()

suite.addTest(loader.discover(CASE_PATH))

with open(os.path.join(REPORT_PATH,"report.html"),"wb") as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        description="V3版本web自动化报告",
        title="V3_REPORT",
        tester="善待今天"
    )
    runner.run(suite)

