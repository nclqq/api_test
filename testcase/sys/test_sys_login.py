import pytest
import allure
from common.commonData import CommonData
from conftest import http


@allure.feature("登录用户模块")
class Test_Login:

    common=CommonData()

    # 测试用例体
    @allure.story("用户名密码都正确")
    def test_login_success(this):
        login_path='/sys/login'
        login_data = {
            'userName':this.common.admin_moblie,
            'password':this.common.admin_password
        }
        # 调用httpUtil的post方法
        resp_login = http.post(login_path, login_data)
        assert resp_login['code']==200
        assert resp_login['msg'] == '操作成功'
        assert resp_login['object']['userId'] == 2
        print("pass------------\n")
        return resp_login['object']['userId']
#
    #用户名或密码错误
    @allure.story("密码错误")
    def test_login_fail_pwderror(this):
        login_path='/sys/login'
        login_data = {
            'userName':this.common.admin_moblie,
            'password':this.common.error_pwd
        }
        # 调用httpUtil的post方法
        resp_login = http.post(login_path, login_data)
        assert resp_login['code']==410
        assert resp_login['msg'] == '用户名或密码错误'
        print("pass------------\n")
#
#     #用户名不存在
    @allure.story("用户名不存在")
    def test_login_fail_uNameNotExit(this):
        login_path='/sys/login'
        login_data = {
            'userName':this.common.notexit_uName,
            'password':this.common.admin_moblie
        }
        # 调用httpUtil的post方法
        resp_login = http.post(login_path, login_data)
        assert resp_login['code']==301
        assert resp_login['msg'] == '用户不存在'
        print("pass------------\n")
#
#     #用户名15位
    @allure.story("用户名15位")
    def test_login_fail_uNameNotTrueLength(this):
        login_path='/sys/login'
        login_data = {
            'userName':this.common.uName_errorLen,
            'password':this.common.admin_password
        }
        # 调用httpUtil的post方法
        resp_login = http.post(login_path, login_data)
        assert resp_login['code']==301
        assert resp_login['msg'] == '用户不存在'
        print("pass------------\n")
#
#     #用户名为空
    @allure.story("用户名为空")
    def test_login_fail_uNameNull(this):
        login_path = '/sys/login'
        login_data = {
            'userName': this.common.uName_null,
            'password': this.common.admin_password
        }
        # 调用httpUtil的post方法
        resp_login = http.post(login_path, login_data)
        assert resp_login['code'] == 3010
        assert resp_login['msg'] == "此账户禁止登录"
        print("存在用户名为空的bug\n")
#
#
#     #密码为空
    @allure.story("密码为空")
    def test_login_fail_uPwdNull(this):
        login_path = '/sys/login'
        login_data = {
            'userName': this.common.admin_moblie,
            'password': this.common.uPwd_null
        }
        # 调用httpUtil的post方法
        resp_login = http.post(login_path, login_data)
        assert resp_login['code'] == 410
        assert resp_login['msg'] == "用户名或密码错误"
        # print("存在密码为空的bug\n")
#
#
#
#
#
#
#
#
#
#
#
#
