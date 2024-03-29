
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.template import  loader
from . import  models
from . import forms
from jinja2 import Environment, FileSystemLoader
from django.http import HttpResponse



def login(request):
    # if request.session.get("is_login",None):
    #     print('重定向1')
    #     login_form = forms.UserForm(request.POST)
    #     return render(request, 'loginZHZ.html',locals())
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查输入内容！'
        print('重定向2')
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            #用户名名字的合法性验证
            #密码长度验证
            # len(password)>= 6
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name = username)
            except:
                message = "用户名不存在，请重新输入"
                return render(request, 'login.html',locals())
            if user.password == password:
                '''session添加数据'''
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                request.session['chinese_name'] = user.chinesename

                return redirect('/ZHZ/choice')
            else:
                message = '密码错误，请重新输入'
                return render(request, 'loginZHZ.html', locals())
        else:
             return render(request, 'loginZHZ.html', locals())
    login_form = forms.UserForm()
    return render(request, 'loginZHZ.html',locals())


def register(request):
    pass
    return render(request, 'register.html')

def logout(request):
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    # request.session.set_expiry(1)
    return redirect("/ZHZ/login/")