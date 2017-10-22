from django.template import Library
from django.core.urlresolvers import reverse

# 库注册
register = Library()


def create_menu(flag):

    menu = [
        {'link': reverse('users:info'), 'name': '个人信息', 'active': flag == 'info' and 'active' or ''},
        {'link': reverse('users:order'), 'name': '全部订单', 'active': flag == 'order' and 'active' or ''},
        {'link': reverse('users:site'), 'name': '收货地址', 'active': flag == 'site' and 'active' or ''},
    ]

    return menu

register.filter('create_menu', create_menu)
