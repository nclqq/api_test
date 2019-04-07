#import pytest
#import random
#import allure
#from conftest import http,common
#from testcase.user.test_user_login import Test_Login
#from testcase.user.test_user_loadUserList import Test_LoadUserList
#from testcase.user.test_user_loadUserInfo import Test_LoadUserInfo


#@allure.feature("注册-登录-列表判断id-获取用户信息模块")
#class Test_Register:

    # login=Test_Login()
    # userList=Test_LoadUserList()
    # userInfo=Test_LoadUserInfo()

 #   nickName = str(random.randint(10000000, 100000000))  # 前包后不包
  #  mobile = '135' + nickName
  #  common.newUserName=mobile

    # 测试用例体
 #   @allure.story("注册")
 #   @pytest.mark.debug
 #   def test_register(self):
 #       register_path='/user/saveOrUpdateUser'

 #       register_data = {
  #          'nickName':self.nickName,
  #          'userName':self.mobile
  #      }
        # 调用httpUtil的post方法
   #     resp_login = http.post(register_path, register_data)
   #     assert resp_login['code']==401
        # assert resp_login['msg'] == '操作成功'

   #     Test_Login().test_userLogin()
   #     Test_LoadUserList().test_loadUserList()
   #     Test_LoadUserInfo().test_loadUserInfo()


