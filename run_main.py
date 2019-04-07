import pytest


if __name__ == '__main__':
    pytest.main(['-s','-m=debug','--alluredir','./report/xml'])  #运行注册-登录-列表-信息
    # pytest.main(['-s','-m=info','--alluredir','./report/xml']])  # 启动修改密码
    # pytest.main(['-s'])  # 启动  -s用于可输出
    # pytest.main(['-s','--alluredir','./report/xml'])

