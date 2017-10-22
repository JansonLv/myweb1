from utils.wrappers import *
import re
from .models import *



def check_register_param(request):
    # 获取信息
    user_name = post_getvalue(request, 'user_name')
    user_pwd1 = post_getvalue(request, 'user_pwd1')
    user_pwd2 = post_getvalue(request, 'user_pwd2')
    user_email = post_getvalue(request, 'user_email')
    user_allow = post_getvalue(request, 'user_allow')

    flag = True

    # 判断用户名长度是否符合,
    if not (16 > len(user_name) > 5):
        add_message(request, 'user_name', '用户名长度不符合')
        flag = False

    # 密码长度
    if not (16 > len(user_pwd1) > 5 and re.match(r'^\w+$', user_name)):
        add_message(request, 'user_pwd1', '密码长度不符合且只能为字母和数字')
        flag = False

    # 密码相等
    if not (user_pwd1 == user_pwd2):
        add_message(request, 'user_pwd2', '两次密码要一样')
        flag = False

    # 判断邮箱符合规范
    reg = r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$'
    if not re.match(reg, user_email):
        add_message(request, 'user_email', '邮箱不正确')
        flag = False

    # 是否同意协议
    if not(user_allow == 'on'):
        add_message(request, 'user_allow', '请阅读协议')
        flag = False

    return flag


# 数据库获取信息
def is_name_existing(key):
    return User.objects.filter(user_name=key)


#
def get_name_and_passwd(name):
    user = User.objects.get_userData_by_name(name)
    if user:
        return user.user_pass
    else:
        return False


# 保持登录状态
def keep_login_online(request, name):

    user = User.objects.get_userData_by_name(name)
    # 写入session保持登录状态
    set_session(request, 'username', name)
    # 写入session
    set_session(request, 'uid', user.id)


# 效验地址信息
def check_addr_info(request):
    user_recv = post_getvalue(request, 'user_recv')
    user_site = post_getvalue(request, 'user_site')
    print('user_site------->', user_site)
    user_group = post_getvalue(request, 'user_group')
    user_tele = post_getvalue(request, 'user_tele')

    if user_recv == '':
        return False
    if user_site == '':
        return False
    if len(user_group) != 6:
        return False
    if len(user_tele) != 11:
        return False

    return True
