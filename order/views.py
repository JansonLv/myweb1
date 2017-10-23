from django.shortcuts import render
from django.core.urlresolvers import reverse
from utils.wrappers import *
from carts.models import *
from .models import *
from goods.models import *
from users.models import User
from django.http import JsonResponse
import time
from django.db import transaction
# Create your views here.


# 提交订单
def order(request):
    # 结算的商品编号
    goods_id_list = post_getlist(request, 'goods_id')

    # 结算的商品
    cart_goods = Cart.objects.filter(cart_user_id=get_session(request, 'uid'), cart_goods_id__in=goods_id_list)

    total_num = 0
    total_money = 0
    for goods in cart_goods:

        # 单个商品总价
        goods.single_total_money = goods.cart_amount * goods.cart_goods.good_price
        # 商品总数
        total_num += goods.cart_amount
        # 商品总数,商品总价
        total_money += goods.single_total_money

        cart_goods.total_num = total_num
        cart_goods.total_money = total_money

        cart_goods.total_money_and_freight = cart_goods.total_money + 10

        user = User.objects.get(id=get_session(request, 'uid'))

    goods_id_list = ','.join(goods_id_list)

    return render(request, 'order/place_order.html', locals())


@transaction.atomic()
def balance_order(request):
    # 获取商品,根据获取的字符串生成商品id列表
    goods_idList = post_getvalue(request, 'idList').split(',')
    # 获取购买方式
    pay_way = post_getvalue(request, 'pay_way')
    # 获取购买用户id
    user_id = int(get_session(request, 'uid'))
    # 获取用户信息,通过order_user外键获取
    user = User.objects.get(pk=user_id)

    # 创建事务还原点(用于回滚)
    save_point = transaction.savepoint()

    try:
        # 生成订单信息
        orderInfo = Order()
        orderInfo.order_num = str(user_id) + str(int(time.time() * 10000))
        orderInfo.order_user_id = user_id
        orderInfo.order_addr = user.user_addr
        orderInfo.order_recName = user.user_name
        orderInfo.order_tele = user.user_tele
        orderInfo.order_fee = 10
        orderInfo.order_pay = int(pay_way)
        orderInfo.save()

        # 查询已购买商品,根据用户id和商品id
        goods = Cart.objects.filter(cart_user_id=user_id, cart_goods_id__in=goods_idList)

        # 生成订单商品信息
        for good in goods:
            goods_detail = GoodsDetail()
            goods_detail.detail_name = good.cart_goods.good_name
            goods_detail.detail_price = good.cart_goods.good_price
            goods_detail.detail_amount = good.cart_amount
            goods_detail.detail_unit = good.cart_goods.good_unit
            goods_detail.detail_image = good.cart_goods.good_image
            goods_detail.detail_goodsID = good.cart_goods.id
            goods_detail.detail_order = orderInfo
            goods_detail.save()
    except Exception as error:
        # 回滚事务
        transaction.rollback(save_point)
        return JsonResponse({'ret': 0})
    else:
        # 删除购物车
        goods.delete()
        return JsonResponse({'ret': 1})
