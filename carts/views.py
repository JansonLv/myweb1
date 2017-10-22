from django.shortcuts import render
from django.core.urlresolvers import reverse
from utils.wrappers import *
from .models import *
from django.http import JsonResponse
# Create your views here.


# 购物车
def cart(request):

    return render(request, 'carts/cart.html', locals())

# 商品添加到购物车
def add_goods(request):
    # 1.获取用户id,商品id,商品数量
    goods_id = get_getvalue(request, 'goods_id')
    user_id = get_session(request, 'uid')
    goods_num = get_getvalue(request, 'goods_num')
    # 2.先判断是否在购物车中存在
    try:
        # 2.1如果存在,之更新商品的数量
        goods = Cart.objects.get(cart_goods_id=goods_id, cart_user_id=user_id)
        goods.cart_amount += goods_num
        goods.save()
    except:
        # 2.2如果不存在,新增一条购物车的商品数据
        goods = Cart()
        goods.cart_goods_id = goods_id
        goods.cart_user_id = user_id
        goods.cart_amount = goods_num
        goods.save()
    finally:
        # 将当前购物车商品数量总和返回
        total = 0
        carts = Cart.objects.filter(cart_user_id=user_id)
        for good in carts:
            total += good.cart_amount

    return JsonResponse({'total': total})
