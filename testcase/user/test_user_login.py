import allure
from conftest import http,common



@allure.feature("user下的登录模块")
class Test_Login:

    # 测试用例体
    @allure.story("登录成功")
    def test_userLogin(self):
        login_path='/sys/login'
        login_data = {
            'userName':common.newUserName,
            'password':common.admin_password
        }
        # 调用httpUtil的post方法
        resp_login = http.post(login_path, login_data)

        assert resp_login['code']==200
        assert resp_login['msg'] == '操作成功'
        # assert resp_login['object']['userId'] == 263
        #将新注册的id传到公共数据中
        common.newUserId=resp_login['object']['userId']

        print(resp_login['object']['userId'])
        print("pass------------\n")
        return resp_login['object']['userId']


