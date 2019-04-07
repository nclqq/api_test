import pytest
import allure
from  conftest import http,common



#运行修改密码时，就不能运行其他
@allure.feature("修改密码模块")
# @pytest.mark.info
class Test_changePwd:

    login_path = '/sys/changePwd'


    @allure.story("修改密码成功")
    @pytest.mark.usefixtures("changePwd_return")
    def test_changePwd(self):
        login_data = {
            'userId': common.userId,
            'userName': common.my_mobile,
            'oldPwd': common.admin_password,
            'password': common.error_pwd
        }
        # 调用httpUtil的post方法
        resp_login = http.post(self.login_path, login_data)
        assert resp_login['code'] == 200
        assert resp_login['msg'] == '操作成功'
        print("修改密码成功------\n")


    @allure.story("恢复密码成功")
    @pytest.fixture()
    def changePwd_return(self):
        yield
        login_data = {
            'userId': common.userId,
            'userName': common.my_mobile,
            'oldPwd': common.error_pwd,
            'password': common.admin_password
        }
        # 调用httpUtil的post方法
        resp_login = http.post(self.login_path, login_data)
        assert resp_login['code'] == 200
        assert resp_login['msg'] == '操作成功'
        print("恢复密码成功------\n")

