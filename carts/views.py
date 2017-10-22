from django.shortcuts import render
from django.core.urlresolvers import reverse
from utils.wrappers import *
from .models import *
from django.http import JsonResponse
# Create your views here.


# 购物车
@check_permission #检查账户是否登录
def cart(request):
    # 取出购物车数据
    carts = Cart.objects.filter(cart_user_id=get_session(request, 'uid'))
    # 记录总数量和总价格
    total_num = 0
    total_money = 0
    # 遍历购物车统计
    for cart1 in carts:
        cart1.total_money = cart1.cart_amount * cart1.cart_goods.good_price
        total_money += cart1.total_money
        total_num += cart1.cart_amount
    # 加入carts中
    carts.total_money = total_money
    carts.total_num = total_num

    return render(request, 'carts/cart.html', locals())


# 商品添加到购物车
def add_goods(request):
    # 1.获取用户id,商品id,商品数量
    goods_id = get_getvalue(request, 'goods_id')
    user_id = get_session(request, 'uid')
    goods_num = get_getvalue(request, 'goods_num')
    print(goods_id, user_id)
    # 2.先判断是否在购物车中存在
    try:
        # 2.1如果存在,之更新商品的数量
        goods = Cart.objects.get(cart_user_id=user_id, cart_goods_id=goods_id)
        # 获得的goods_num是字符串,必须int
        goods.cart_amount += int(goods_num)
        goods.save()
    except Exception as error:
        # 2.2如果不存在,新增一条购物车的商品数据
        # print(error)
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
