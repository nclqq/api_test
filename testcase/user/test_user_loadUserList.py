import allure
from conftest import http,common


@allure.feature("user下的加载用户列表")
class Test_LoadUserList:


    # 测试用例体
    @allure.story("加载用户列表")
    def test_loadUserList(self):
        userList_path='/user/loadUserList'
        userList_data = {
            'pageSize': 30,
            'pageCurrent':1
        }
        # 调用httpUtil的post方法
        resp_login = http.post(userList_path, userList_data)

        print(resp_login['object']['list'][0]['id'])
        print(common.newUserId)

        assert resp_login['code']==200
        assert resp_login['msg'] == '操作成功'
        assert resp_login['object']['list'][0]['id'] == common.newUserId
        print("pass------------\n")
