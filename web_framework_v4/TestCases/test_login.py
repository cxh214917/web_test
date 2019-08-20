# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/03 16:49
file:test_login.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""

import pytest
from web_framework_v4.TestDatas import login_datas as L_D
from web_framework_v4.PageObjects.login_page import LoginPage
from web_framework_v4.PageObjects.index_page import IndexPage
from web_framework_v4.Common.my_log import myLog

@pytest.fixture()
@pytest.mark.usefixtures("init_driver")
def init(init_driver):
    myLog.info("开始执行测试：新建会话，最大化窗口，访问网址")
    yield init_driver
    myLog.info("测试执行完毕：退出会话")

@pytest.mark.usefixtures("init")
class TestLogin:

    @pytest.mark.parametrize("data", L_D.success)
    def test_login_success(self,init,data):
        """
        登陆成功-->用户名和账号均正确
        :return:
        """
        # 步骤
        LoginPage(init).login(data['username'],data['passwd'])
        # 断言
        assert IndexPage(init).check_username_exists()

    @pytest.mark.parametrize("data",L_D.Invalid_data_01)
    def test_login_usernameIsOk_passwdIsWrong(self,data,init):
        """
        登陆失败-->用户名正确，密码错误
        :return:
        """
        # 步骤
        LoginPage(init).login(data["username"],data["passwd"])
        # 断言
        assert data["check_info"] == LoginPage(init).get_page_center_error_info()

    @pytest.mark.parametrize("data",L_D.Invalid_data_02)
    def test_login_usernameIsFormat_passwdIsNone(self,data,init):
        """
        用户名格式合法，密码为空
        :return:
        """
        # 步骤
        LoginPage(init).login(data["username"],data["passwd"])
        # 断言
        assert data["check_info"] == LoginPage(init).get_form_error_info()

    @pytest.mark.parametrize("data",L_D.Invalid_data_03)
    def test_usernameNotRegister_passwdNotNone(self,data,init):
        """
        用户名合法且未注册，密码不为空
        :return:
        """
        # 步骤
        LoginPage(init).login(data["username"],data["passwd"])
        # 断言
        assert data["check_info"] == LoginPage(init).get_page_center_error_info()

    @pytest.mark.parametrize("data",L_D.Invalid_data_04)
    def test_usernameNotFormat_passwd(self,data,init):
        """
        用户名不合法-->密码不用管，断言从上往下执行
        :return:
        """
        # 步骤
        LoginPage(init).login(data["username"],data["passwd"])
        # 断言==也可以用以下断言
        # self.assertIn(LoginPage(self.driver).get_form_error_info(),'["请输入正确的手机号","请输入密码"]')
        assert data["check_info"] == LoginPage(init).get_form_error_info()

    @pytest.mark.parametrize("data",L_D.Invalid_data_05)
    def test_usernameIsNone_passwd(self,data,init):
        """
        用户名为空，密码随意
        :return:
        """
        # 步骤
        LoginPage(init).login(data["username"],data["passwd"])
        # 断言
        assert data["check_info"] == LoginPage(init).get_form_error_info()