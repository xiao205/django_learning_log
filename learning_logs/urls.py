"""定义learning_logs的URL模式"""
from django.urls import path
from . import views  #从url所在目录导入views
app_name = 'learning_logs'
urlpatterns = [
    #主页
    #将url映射视图 匹配到url返回一个视图
    path('',views.index,name='index'),
    #显示所有的主题
    path('topics/',views.topics,name='topics'),
    #显示主题的详细信息
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    #添加新的主题页面
    path('new_topic/',views.new_topic,name='new_topic'),
    #添加新的条目页
    path('new_entry/<int:topic_id>',views.new_entry,name='new_entry'),
    #编辑已有条目页面
    path('edit_entry/<int:entry_id>',views.edit_entry,name='edit_entry'),
]