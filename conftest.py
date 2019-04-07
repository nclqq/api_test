import pytest
from util.httpUtil import HttpUtil
from common.commonData import CommonData


http = HttpUtil()  # cookies中的JSESSIONID
common=CommonData()

@pytest.fixture(scope='session', autouse=True)
def session_fixture():
    login_path="/sys/login"  #每个方法的路径都变化
    # 定义字典，添加登录传入的数据
    login_data={}
    login_data['userName']=common.admin_moblie
    # login_data['userName'] = common.my_mobile
    login_data['password']=common.admin_password
    #调用httpUtil的post方法
    resp_login=http.post(login_path,login_data)
    #获取token
    CommonData.token=resp_login['object']['token']
    CommonData.userId=resp_login["object"]["userId"]
    #断言
    assert resp_login['code'] == 200  #返回中的code
    print('登录成功')


    yield
    logout_path = "/sys/logout"
    logout_data=None
    resp_logout=http.post(logout_path,logout_data)
    assert resp_logout['code'] == 200
    print("登出成功")







