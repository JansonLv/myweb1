from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
import hashlib

# 写入cookies
def set_cookies(response, key, value):
    response.set_cookie(key, value, max_age=60*60*24)


# 获取cookies
def get_cookies(request, key):
    return request.COOKIES.get(key, '')


# 删除cookies
def del_cookies(response, key):
    response.delete_cookie(key)


# 写入session
def set_session(request, key, value):
    request.session[key] = value


# 获取session

def get_session(request, key):
    return request.session.get(key, '')


# 删除session
def del_session(request):
    request.session.flush()


def post_getvalue(request, key):
    return request.POST.get(key, "").strip()


def get_getvalue(request, key):
    return request.GET.get(key, "").strip()


# 获取post传过来的list列表
def post_getlist(request, key):
    return request.POST.getlist(key, "")


# 增加消息到系统消息队列中,调用时利用spilt切割
def add_message(request, key, mess):
    messages.add_message(request, messages.INFO, key+':'+mess)

# 取出所有错误信息并整理返回
def get_message(request):

    # 取出所有错误信息
    mess = messages.get_messages(request)
    # print(mess)
    info = dict()
    for message in mess:
        messaage_list = str(message).split(':')
        info[messaage_list[0]] = messaage_list[1]

    return info

# 加密数据
def password_encryption(password, salt=''):
    sha = hashlib.sha256()
    new_password = '$%^$%^@$%@' + password + salt + '*(&^%$#DSFGDRS'
    sha.update(new_password.encode('utf-8'))

    return sha.hexdigest()

# 判断用户是否登陆
def check_user_login(request):
    return get_session(request, 'username')

# 检测用户权限
def check_permission(view_func):

    def wrapper(request, *args, **kwargs):
        # 判断用户是否登录
        if check_user_login(request):
            # 调用视图函数
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse('users:login'))
    return wrapper