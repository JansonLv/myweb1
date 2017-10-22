from django.db import models
from db.AbstractModel import *
# Create your models here.
from utils.wrappers import *
class UserManager(models.Manager):
    # 通过国用户名获取用户数据
    def get_userData_by_name(self, username):
        try:
            return self.get(user_name=username)
        except User.DoesNotExist:
            return None

    # 用户注册数据保存
    def user_registerData_save(self, request):
        userinfo = self.model()
        userinfo.user_name = post_getvalue(request, 'user_name')
        userinfo.user_pass = password_encryption(post_getvalue(request, 'user_pwd1'))
        userinfo.user_mail = post_getvalue(request, 'user_email')
        # print(type(userinfo.user_mail))
        # print(type(userinfo.user_pass))

        userinfo.save()


    # 用户地址信息保存
    def user_addrInfo_save(self, request):
        useraddrInfo = self.get_userData_by_name(get_session(request, 'username'))
        useraddrInfo.user_recv = post_getvalue(request, 'user_recv')
        useraddrInfo.user_addr = post_getvalue(request, 'user_site')
        useraddrInfo.user_code = post_getvalue(request, 'user_group')
        useraddrInfo.user_tele = post_getvalue(request, 'user_tele')
        useraddrInfo.save()


# 用户模型类
class User(AbstractModel):

    # 用户名
    user_name = models.CharField(max_length=20)
    # 用户密码
    user_pass = models.CharField(max_length=100)
    # 用户邮箱
    user_mail = models.CharField(max_length=50)
    # 用户地址
    user_addr = models.CharField(max_length=50)
    # 用户手机
    user_tele = models.CharField(max_length=11)
    # 邮政编码
    user_code = models.CharField(max_length=10)
    # 收件人
    user_recv = models.CharField(max_length=10, default='')


   # 创建自定义管理器类
    objects = UserManager()


# 用户浏览记录模型
class RecordBrowse(AbstractModel):
    # 浏览商品
    browse_good = models.ForeignKey('goods.GoodsInfo')
    # 浏览者
    browse_user = models.ForeignKey('User')








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