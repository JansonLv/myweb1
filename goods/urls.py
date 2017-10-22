from django.conf.urls import url, include
from .views import *

# ^起始字符一定要加,$结束符号根据要求
urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^detail/$', detail, name='detail'),
    url(r'^goods_list/(\d+)/(\d+)/$', goods_list, name='goods_list'),
]



