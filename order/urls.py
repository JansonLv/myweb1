from django.conf.urls import url, include
from .views import *

# ^起始字符一定要加,$结束符号根据要求
#
urlpatterns = [
    url(r'^order/', order, name='order')
]



