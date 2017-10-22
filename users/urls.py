from django.conf.urls import url
from .views import *

# ^起始字符一定要加,$结束符号根据要求
urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^user_center_info/$', info, name='info'),
    url(r'^user_center_order/$', order, name='order'),
    url(r'^user_center_site/$', site, name='site'),
    # 处理注册信息
    url(r'^deal_register/$', deal_register, name='deal_register'),
    # 处理用户名是否存在
    url(r'^checkname/$', check_name, name='check_name'),
    # 处理登录信息
    url(r'^login_handle/$', login_handle, name='login_handle'),
    # 注销
    url(r'^login_out/$', login_out, name='login_out'),
    # 地址信息修改
    url(r'^info_edit$', info_edit, name='info_edit'),
]



