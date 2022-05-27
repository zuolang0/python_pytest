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
# 会话级别
@pytest.fixture(scope="session",autouse=False)
def exe_user():
    pass
