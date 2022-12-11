from django.shortcuts import render,redirect
#login函数以便用户注册后让其自动登录
from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    #注册新用户
    if request.method != 'POST':
        #显示空的注册表
        form = UserCreationForm()
    else:
        #处理填好的注册表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #让新用户自动登录
            login(request,new_user)
            return redirect('learning_logs:index') # 登录后返回主页
    context= {'form':form}
    return render(request,'registration/register.html',context)