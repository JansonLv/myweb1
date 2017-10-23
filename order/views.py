from django.shortcuts import render
from django.core.urlresolvers import reverse
from utils.wrappers import post_getlist, get_session
from carts.models import *
from users.models import User
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

    return render(request, 'order/place_order.html', locals())