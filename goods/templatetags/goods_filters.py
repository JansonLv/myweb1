from django.template import Library

# register变量名不可改,否则注册不成功
register = Library()

def create_imgage_name(index):
    return "images/banner0" + str(index) + ".jpg"

register.filter('create_imgage_name', create_imgage_name)


# from django.template import Library
#
#
# register = Library()
#
#
# # 创建过滤器
# def create_imgage_name(index):
#     return 'images/banner0' + str(index) +'.jpg'
#
#
# register.filter('create_imgage_name', create_imgage_name)
