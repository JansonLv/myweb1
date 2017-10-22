from django.contrib import admin

from .models import *




'''
# 采用装饰器
@admin.register(模型类名)
class 模型类名Admin(admin.ModelAdmin):
    list_display = [显示的模型字段名]
'''
