from .wrappers import *


# 判断用户是否登录
def is_login(request):
    print('username', get_session(request, 'username'))
    return get_session(request, 'username')