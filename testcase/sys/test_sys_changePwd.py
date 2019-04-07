import pytest
import allure
from  conftest import http
from common.commonData import CommonData


@allure.feature("修改密码模块")
class Test_changePwd:
    common=CommonData
    login_path = '/sys/changePwd'


    @allure.story("修改密码成功")
    # @pytest.mark.info
    @pytest.mark.usefixtures("changePwd_return")
    def test_changePwd(self):
        login_data = {
            'userId': self.common.userId,
            'userName': self.common.my_mobile,
            'oldPwd': self.common.admin_password,
            'password': self.common.error_pwd
        }
        # 调用httpUtil的post方法
        resp_login = http.post(self.login_path, login_data)
        assert resp_login['code'] == 200
        assert resp_login['msg'] == '操作成功'
        print("修改密码成功------\n")

    @allure.story("重置密码成功")
    @pytest.fixture()
    def changePwd_return(self):
        yield
        login_data = {
            'userId': self.common.userId,
            'userName': self.common.my_mobile,
            'oldPwd': self.common.error_pwd,
            'password': self.common.admin_password
        }
        # 调用httpUtil的post方法
        resp_login = http.post(self.login_path, login_data)
        assert resp_login['code'] == 200
        assert resp_login['msg'] == '操作成功'
        print("恢复密码成功------\n")

