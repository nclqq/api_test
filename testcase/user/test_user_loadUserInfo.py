import pytest
import allure
from conftest import http
from testcase.user.test_user_login import Test_Login


@allure.feature("user下的获取用户信息")
class Test_LoadUserInfo:

    testLogin=Test_Login()

    # 测试用例体
    @allure.story("获取用户信息")
    def test_loadUserInfo(self):
        login_path='/user/loadUserInfo '
        login_data = {
            'id':Test_Login().test_login_success()
        }
        # 调用httpUtil的post方法
        resp_login = http.post(login_path, login_data)
        assert resp_login['code']==200
        assert resp_login['msg'] == '操作成功'
        print("pass------------\n")


