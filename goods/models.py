from django.db import models
from db.AbstractModel import *
from tinymce.models import HTMLField
# Create your models here.

# 分类模型
class Category(AbstractModel):

    # 产品分类名称
    cag_name = models.CharField(max_length=30)


# 商品信息管理类
class GoodsInfoManager(models.Manager):
    # 获得最新添加商品
    def get_new_goods(self, cag, num=4):
        return self.filter(goods_cag=cag).order_by('-id')[:num]

    def get_hot_goods(self, cag, num=3):
        return self.filter(goods_cag=cag).order_by('-good_visits')[:num]

    # 获得所有商品中最新的两个商品
    def get_new_by_all_goods(self, num=2):
        return self.all().order_by('-id')[:num]

    # 根据商品的id分类获取商品列表
    # def get_goods_by_cagid(self, cag_id):
    #     return self.filter(goods_cag_id=cag_id)

    # 根据商品分类的id获取商品列表
    def get_goods_by_cagid(self, cag_id, show):
        if show == 'price':
            return self.filter(goods_cag_id=cag_id).order_by('-good_price')

        if show == 'hot':
            return self.filter(goods_cag_id=cag_id).order_by('-good_visits')

        return self.filter(goods_cag_id=cag_id)

class GoodsInfo(AbstractModel):
    # 商品名称
    good_name = models.CharField(max_length=30)
    # 商品价格
    good_price = models.DecimalField(max_digits=10, decimal_places=2)
    # 商品图片(配置静态文件图片路径)
    good_image = models.ImageField()
    # 商品简述
    good_compendium = models.CharField(max_length=100)
    # 商品详情(配置富文本编辑器)
    good_details = HTMLField()
    # 商品上架
    good_status = models.BooleanField(default=True)
    # 商品单位
    good_unit = models.CharField(max_length=20)
    # 商品访问量
    good_visits = models.IntegerField(default=0)
    # 商品销量
    good_sales = models.IntegerField(default=0)
    # 商品分类
    goods_cag = models.ForeignKey(Category)

    objects = GoodsInfoManager()

# 广告模型
class Advertise(AbstractModel):
    # 广告名字
    ad_name = models.CharField(max_length=30)
    # 广告图片
    ad_image = models.ImageField(upload_to='ad')
    # 广告链接
    ad_link = models.CharField(max_length=100)








'''
# 自定义管理器模式
class 自定义管理器类名(models.Manager):
    # 管理器新增方法
    def 方法名(self):
        # 获取父类方法
        变量 = super(自定义管理器类名, self).all()
        """""""
        # 处理过程
        """"""" 
        return 变量
'''
'''
# 字段元选项
class Meta:
        # 重定义数据库的数据表名
        db_table = 'my_custom_dbname'
        # 表示该模型类为抽象类,不生成表
        abstract = True
        # 排序
        ordering = ['-id']
'''