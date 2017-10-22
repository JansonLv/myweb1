from django.shortcuts import render
from django.core.urlresolvers import reverse
# Create your views here.

# 提交订单
def order(request):
    return render(request, 'order/place_order.html', locals())