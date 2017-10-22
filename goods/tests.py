from django.test import TestCase
from goods.models import *
import random
# cags = ['新鲜水果', '海鲜水产', '猪牛羊肉', '禽类蛋品', '新鲜蔬菜', '速冻食品']
# # for cag in cags:
# #     c = Category()
# #     c.cag_name = cag
# #     c.save()
# #
# #
# units = ['500克', '1吨', '2个', '3条', '1包', '5支', '1头', '2瓶']
#
# # 创建商品测试数据
# with open('/home/python/Desktop/Django/ttsx/myweb/data.txt', 'r') as f:
#
#     for goods_name in f:
#         # 创建商品对象
#         goods = GoodsInfo()
#         goods.good_name = goods_name[:-1]
#         goods.good_compendium = '商品非常好，一天销量破百万!'
#         goods.good_details = '商品非常非常详细的描述在这里!'
#         # 要增加id
#         goods.goods_cag_id = random.randint(1, len(cags))
#         goods.good_image = 'goods/' + str(random.randint(1, 18)) + '.jpg'
#         goods.good_price = random.randint(1, 999)
#         goods.good_unit = units[random.randint(0, len(units) - 1)]
#
#         # 保存商品
#         goods.save()

# 创建广告数据
# for index in range(1, 5):
#     ad = Advertise()
#     ad.ad_name = '广告'
#     ad.ad_image = 'goods/ad/' + 'slide0' + str(index) + '.jpg'
#     ad.ad_link = '#'
#     ad.save()
#
# for index in range(1, 3):
#     ad = Advertise()
#     ad.ad_name = '广告'
#     ad.ad_image = 'goods/ad/' + 'adv0' + str(index) + '.jpg'
#     ad.ad_link = '#'
#     ad.save()