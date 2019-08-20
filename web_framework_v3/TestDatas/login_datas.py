# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/08/04 18:33
file:login_datas.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
# 有效数据
success = [
    {"username":"18684720553","passwd":"python"},
    {"username":"13760246701","passwd":"python"}
]

# 用户名正确，密码错误
Invalid_data_01 = [
    {"username":"18684720553","passwd":"python111","check_info":"帐号或密码错误!"},
    {"username":"13760246701","passwd":"python222","check_info":"帐号或密码错误!"}
]

# 用户名格式合法，密码为空
Invalid_data_02 = [
    {"username":"18684720557","passwd":"","check_info":"请输入密码"},
    {"username":"18684720553","passwd":"","check_info":"请输入密码"}
]

# 用户名合法且未注册，密码不为空
Invalid_data_03 = [
    {"username":"18684720559","passwd":"wwewewe","check_info":"此账号没有经过授权，请联系管理员!"},
    {"username":"18936368795","passwd":"123wer","check_info":"此账号没有经过授权，请联系管理员!"}
]

# 用户名不合法，密码随意
Invalid_data_04 = [
    {"username":"qweqwrq123","passwd":"","check_info":"请输入正确的手机号"},
    {"username":"1893636879578","passwd":"123wer","check_info":"请输入正确的手机号"}
]

# 用户名为空，密码随意
Invalid_data_05 = [
    {"username":"","passwd":"","check_info":"请输入手机号"},
    {"username":"","passwd":"123wer","check_info":"请输入手机号"}
]