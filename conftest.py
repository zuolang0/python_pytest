import pytest
def read_yaml():
    return ['chenglong','zhenzidan','gutianle']

@pytest.fixture(scope="function",autouse=False,params=read_yaml(),ids=['c','z','g'])
def exe_data(request):
    print('start')
    yield request.param
    print('end')

@pytest.fixture(scope="function",autouse=False)
def exe_user():
    pass
@pytest.fixture(scope="module",autouse=False) #一个module里的所有函数共用一个句柄实例
def sql_query():
    #连接数据库
    #获得数据库查询句柄
    yield "查询句柄"
    #关闭句柄
    #关闭数据库连接
# 会话级别
@pytest.fixture(scope="session",autouse=False)
def exe_user():
    pass
