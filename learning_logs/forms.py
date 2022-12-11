from django import forms   #创建表单
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

# 添加新的条目
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':' '}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}