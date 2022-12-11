from django.shortcuts import render,redirect
from .models import Topic ,Entry # 导入模板
from .forms import TopicForm,EntryForm
#作为装饰器，用户运行topics代码时候会检查是否登录，没有登录会返回登录页面
from django.contrib.auth.decorators import  login_required
from django.http import Http404 #没有请求资源返回404
# Create your views here.
def index(request):
    """学习笔记主页"""
    return render(request,'learning_logs/index.html')
@login_required
def topics(request):
    #显示所有主题
   # topics = Topic.objects.order_by('date_added')
    #hi只允许用户访问自己的主题，从数据库中获取owner属性 ，
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
    #显示主题的详细内容
    topic = Topic.objects.get(id=topic_id)
    #确认请求的主题属于当前用户, 如果请求的主题不贵用户，就会引发404
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

def new_topic(request):
    #对提交的表单数据进行处理，并将用户重定向到页面topics
    """添加新主题"""
    if request.method != 'POST':
        #当请求是get请求发返回一个空的表单
        form = TopicForm()
    else:
        #post请求对提交数进行处理
        form = TopicForm(data=request.POST)
        # 如果表单有值，is_valid 方法会对表单进行检查
        if form.is_valid():
            #将新加的主题给定owner
            new_topic = form.save(commit=False)
            new_topic.owner = request.user # 将主题owner设为当前用户
            new_topic.save()
            return redirect('learning_logs:topics')  # 最后返回到topics视图
    context = {'form':form}
    return  render(request,'learning_logs/new_topic.html',context)

def new_entry(request,topic_id):
    #在特定主题中添加条目
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id=topic_id)

    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

def edit_entry(request,entry_id):
    #修改已有条目
    entry = Entry.objects.get(id=entry_id) # 获取已有条目
    topic = entry.topic # 条目关联的主题
    if request.method != 'POST':
        form = EntryForm(instance=entry) # 初始显示之前的条目信息
    else:
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)