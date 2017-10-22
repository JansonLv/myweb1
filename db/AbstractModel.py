from django.db import models

class AbstractModel(models.Model):
    # 数据创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 数据更新时间
    update_time = models.DateTimeField(auto_now=True)
    # 是否删除
    real_del = models.BooleanField(default=False)

    # 声明为抽象类
    class Meta:
        abstract = True