from django.db import models
#将主题关联到特定用户
from django.contrib.auth.models import User
# Create your models here.
#这里创建模型，用于如何处理应用程序中存储的数据
class Topic(models.Model):
    """用户学习主题"""
    # 设置又字符串组成的数据作为文本 ， 长度为200个字节
    text = models.CharField(max_length=200)
    #记录日期True表示自动设置为当前日期和时间
    date_added = models.DateTimeField(auto_now_add=True)
    #建立到模型User的外键，用户删除，所相关联的主题也删除
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        # 返回字符串表示
        return self.text

#添加条目，每个条目与特定的主题相关联，多对一关系， 多个条目可以关联到多个主题
class Entry(models.Model):
    # 某个主题的具体知识
    #外键关联到另一个主题， on_delte 在删除时删除相关条目
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField() #长度不受限制
    date_added = models.DateTimeField(auto_now_add=True)

    # 存储管理模型的额外信息
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        "返回模型字符串"
        return f"{self.text[:50]}..."