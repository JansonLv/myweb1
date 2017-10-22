from django.shortcuts import render
from .models import *
from django.core.urlresolvers import reverse
from utils.wrappers import *
# Create your views here.
from .function import *
from django.core.paginator import Paginator

# 首页
@get_total_cart_sum
def index(request):

    # 获取广告信息
    ads1 = Advertise.objects.all()[:4]
    ads2 = Advertise.objects.all()[4:]




    # 获得商品所有分类
    cags = Category.objects.all()

    # 获得每一个分类的最新商品的列表(4个),热门商品(3个)
    for cag in cags:
        # 获得最新商品4个
        new_goods = GoodsInfo.objects.get_new_goods(cag, 4)
        # 获得最热商品3个
        hot_goods = GoodsInfo.objects.get_hot_goods(cag, 3)

        ################为什么有个.hot.new####################
        # print(cag.new)
        cag.new = new_goods
        cag.hot = hot_goods

    return render(request, 'goods/index.html', locals())


# 商品详情
@get_total_cart_sum
def detail(request):

    # 获取get请求id
    key_id = get_getvalue(request, 'id')

    # 获取商品信息
    good_info = GoodsInfo.objects.get(pk=key_id)




    # 获取两个所有商品中最热门的
    good_new = GoodsInfo.objects.get_new_by_all_goods()

    # 更新用户浏览记录
    update_user_browe_record(request)

    return render(request, 'goods/detail.html', locals())


# 商品列表
@get_total_cart_sum
def goods_list(request, cag_id, pag_id):

    #读取商品分类
    cags = Category.objects.all()

    show = get_getvalue(request, 'show')
    print(show)
    #根据商品的id分类获取商品列表
    goods_lists = GoodsInfo.objects.get_goods_by_cagid(cag_id, show)

    # 创建分页对象
    paginator = Paginator(goods_lists, 10)
    # 获得当前分页数据
    current_page = paginator.page(pag_id)

    goods_new = GoodsInfo.objects.get_new_by_all_goods(2)

    pag_id = int(pag_id)

    return render(request, 'goods/list.html', locals())
