from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
from .functions import *
from .models import *
from goods.function import  *
# Create your views here.





def login(request):
    # 判断是否记录账号
    if get_cookies(request, 'memb_acount'):
        memb_acount = get_cookies(request, 'memb_acount')

    return render(request, 'users/login.html', locals())


def register(request):
    error_mess = get_message(request)

    return render(request, 'users/register.html', locals())


# 用户中心-个人信息
@check_permission
def info(request):
    # 获取用户信息
    user = User.objects.get_userData_by_name(get_session(request, 'username'))
    # 获取关联的信息
    records = user.recordbrowse_set.all().order_by('-update_time')

    return render(request, 'users/user_center_info.html', locals())


# 用户中心-订单中心
@check_permission
def order(request):
    return render(request, 'users/user_center_order.html', locals())


# 用户中心 -收货地址
@check_permission
def site(request):
    # 获取个人信息
    user_addrInfo = User.objects.get_userData_by_name(get_session(request, 'username'))

    return render(request, 'users/user_center_site.html', locals())


# 处理注册信息
def deal_register(request):
    #　判断资料是否符合情况
    if check_register_param(request):
        # 符合情况,加入数据库
        User.objects.user_registerData_save(request)
        print('注册成功')
        return redirect(reverse('users:login'))
    else:
        # 不符合情况,跳转回注册界面
        print('注册不成功')
        return redirect(reverse('users:register'))


#
def check_name(request):
    # 获取request中的username
    user_name = get_getvalue(request, 'username')
    # 获取数据是否存在该name
    bool_name = is_name_existing(user_name)

    if bool_name:
        # 用户名存在
        bool_name = True
    else:
        # 用户名不存在
        bool_name = False

    return JsonResponse({'ret': bool_name})


def login_handle(request):
    # 获取账号和密码
    username_login = post_getvalue(request, 'username_login')
    password_login = post_getvalue(request, 'password_login')
    member_account = post_getvalue(request, 'member_account')
    # 从数据库中效验信息,返回账号和密码
    password = get_name_and_passwd(username_login)

    # 密码匹配
    if password == password_encryption(password_login):
        # 定义response
        response = redirect(reverse('goods:index'))
        # 记录用户登录状态,写session
        keep_login_online(request, username_login)

        # # 判断是否有登录前的页面
        # url = get_session(request, 'pre_url')
        # print('prev_url------>', url)
        # if url:
        #     response = redirect(url)

        # 确定是否要记录账号
        if member_account:
            set_cookies(response, 'memb_acount', username_login)
        # 返回response,即连接index
        return response
    # 密码不匹配
    else:
        return redirect(reverse('users:login'))

# 注销
def login_out(request):
    # 消除session
    del_session(request)
    # 返回登录界面
    return redirect(reverse('users:login'))


# 处理地址信息修改
def info_edit(request):
    # 地址效验
    if check_addr_info(request):
        # 保存信息
        User.objects.user_addrInfo_save(request)

    return redirect(reverse('users:info'))
