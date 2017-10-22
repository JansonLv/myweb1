from django.db import models

# Create your models here.











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