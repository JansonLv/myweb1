from django.db import models
from db.AbstractModel import AbstractModel

# Create your models here.
# 订单详细信息表
class GoodsDetail(AbstractModel):
    # 商品名称
    detail_name = models.CharField(max_length=50)
    # 商品价格
    detail_price = models.IntegerField()
    # 商品数量
    detail_amount = models.IntegerField()
    # 商品单位
    detail_unit = models.CharField(max_length=10)
    #　商品图片
    detail_image = models.ImageField()
    # 商品id
    detail_goodsID = models.IntegerField()
    # 所属订单
    detail_order = models.ForeignKey('Order')

# 订单信息模型
class Order(AbstractModel):
    status = (
        (1, '待支付'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '已完成'),
    )

    pay = (
        (1, '货到付款'),
        (2, '微信支付'),
        (3, '支付宝支付'),
        (4, '银联支付'),
    )

    # 订单编号
    order_num = models.CharField(max_length=50)
    # 订单收货地址
    order_addr = models.CharField(max_length=50)
    # 收件人姓名
    order_recName = models.CharField(max_length=20)
    # 收件人号码
    order_tele = models.CharField(max_length=12)
    # 运费
    order_fee = models.IntegerField(default=10)
    # 订单状态
    order_status = models.SmallIntegerField(choices=status, default=1)
    #　订单支付方式
    order_pay = models.SmallIntegerField(choices=pay, default=1)
    # 订单所属用户
    order_user = models.ForeignKey('users.User')










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