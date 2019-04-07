import requests
import json
from common.commonData import CommonData


#定义一个http的post请求
class HttpUtil:

    def __init__(self):
        self.http=requests.session()
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}

    def post(self,path,data):
        proxies = CommonData.proxies
        host = CommonData.host
        data_json = json.dumps(data)
        if CommonData.token is not None:
            self.headers['token'] = CommonData.token
        resp_login = self.http.post(url=host+path,
                         proxies=proxies,
                         data=data_json,
                         headers=self.headers
                         )
        assert resp_login.status_code==200  #校验返回码是否为200  http中的status_code
        resp_json=resp_login.text  #获取response响应的body值
        resplogin_dict = json.loads(resp_json)  #将body值转为dict
        return resplogin_dict




















# 字典格式是：单引号，json格式是双引号
#
# proxies={'http':'http://localhost:8888'}
# headers={'Content-Type':'application/json;charset=UTF-8'}
# http=requests.session()  #cookies中的JSESSIONID
#
# resp=http.post(url="http://192.168.1.203:8083/sys/login",
#                    proxies=proxies,
#                    data='{"userName":"18210034706","password":"123456"}',
#                    headers=headers
#                    )
# print("打印登录响应体")
# print("json格式：",resp.text)
#
#
# resp_dict=json.loads(resp.text)  #将json转字典格式
# print("字典格式：",resp_dict)
# token=resp_dict['object']['token']  #在响应中获取token值
# headers['token']=token  #将token添加到headers中
# data={'token':token}  #创建一个data的字典，添加token
# data_json=json.dumps(data)  #json.dump是将字典转json
# resp1=http.post(url="http://192.168.1.203:8083/sys/getUserInfo",
#                    proxies=proxies,
#                    # data='{"token":"'+token+'"}',
#                    data=data_json,
#                    headers=headers
#                    )
#
# print("打印获取用户信息响应体")
# print(resp1.text)

