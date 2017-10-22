from django.conf.urls import url, include
from .views import *

# ^起始字符一定要加,$结束符号根据要求
urlpatterns = [
    url(r'^cart/$', cart, name='cart'),
    url(r'^add_goods/$', add_goods, name='add_goods'),
    url(r'^edit_goods_num/$', edit_goods_num, name='edit_goods_num'),
    url(r'^del_goods/$', del_goods, name='del_goods'),
]



