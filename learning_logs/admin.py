from django.contrib import admin

# Register your models here.
# 在这里进行注册
from .models import  Topic,Entry  # 导入模型
#注册让django通过管理网站来管理模型
admin.site.register(Topic)
admin.site.register(Entry)