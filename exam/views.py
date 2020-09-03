import random
import json
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from. import models


# Create your views here.
def choice_page(request):
    """考试选择页面"""
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    return render(request, "choice.html", {'name':'考试主页'})

def gjdg(request):
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    view_name = '公共基础大纲'
    return render(request, "公共基础大纲.html",)

def jtml(request):
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    view_name = '交通工程目录'
    return render(request, "交通工程目录.html",)

def gjzsdjj(request):
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    view_name = '公共基础知识点精简'
    return render(request, "公共基础知识点精简.html",)


# 刷题
def ggjc(request):
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    view_name = '公共基础正序刷题页面'
    indexlist = get_GGJCindex_list()
    return render(request, "vuejichu.html", {"name": view_name, "index_list": indexlist, "count":len(indexlist)})

def ggjc_random(request):
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    view_name = '公共基础正序刷题页面'
    indexlist = get_GGJCindex_list()
    return render(request, "vuejichu_random.html",{"name": view_name, "index_list": indexlist, "count":len(indexlist)})

def jtgc(request):
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    view_name = '交通工程正序刷题页面'
    indexlist = get_JTindex_list()
    return render(request, "vuejiaotong.html",{"name": view_name, "index_list": indexlist, "count":len(indexlist)})

def jtgc_random(request):
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    view_name = '交通工程乱序刷题页面'
    indexlist = get_JTindex_list()
    return render(request, "vuejiaotong_random.html",{"name": view_name, "index_list": indexlist, "count":len(indexlist)})

def get_ggjc_question(request):
    """这个是公共基础的拿取题目的api"""
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    if request.method == 'GET':
        num = request.GET.get("num")
        print(num)
        dic  = {}
        try:
            publisher_obj = models.GGJC_question.objects.get(id=num)
            dic['id']=publisher_obj.id
            dic['question']=publisher_obj.question_title
            dic['q_count']=publisher_obj.q_count
            dic['answer']=str(publisher_obj.answer).replace("\n", '').split("，")
            dic['belong']=publisher_obj.where
            dic['pages']=publisher_obj.page
            print(dic)
            return JsonResponse(dic)
        except Exception as e:
            dic['id'] = '超范围'
            dic['question'] = '超范围'
            dic['q_count'] = '超范围'
            dic['answer'] =['超范围']
            dic['belong'] ='超范围'
            dic['pages'] ='超范围'
            print(e)
            return JsonResponse(dic)
    # return HttpResponse("这是test,无它")

def get_jtgc_question(request):
    """这个是交通工程的拿取题目的api"""
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    if request.method == 'GET':
        num = request.GET.get("num")
        print(num)
        dic  = {}
        try:
            publisher_obj = models.JTGC_question.objects.get(id=num)
            dic['id']=publisher_obj.id
            dic['question']=publisher_obj.question_title
            dic['q_count']=publisher_obj.q_count
            dic['answer']=str(publisher_obj.answer).replace("\n", '').split("，")
            dic['belong']=publisher_obj.where
            dic['pages']=publisher_obj.page
            print(dic)
            return JsonResponse(dic)
        except:
            dic['id'] = '超范围'
            dic['question'] = '超范围'
            dic['q_count'] = '超范围'
            dic['answer'] =['超范围']
            dic['belong'] ='超范围'
            dic['pages'] ='超范围'
            print(dic)
            return JsonResponse(dic)

def get_JTindex_list():
    """交通工程所有题号"""
    JTindexlist= models.JTGC_question.objects.all()
    JTindexlist = [i[0] for i in JTindexlist.values_list()]
    return JTindexlist

def get_GGJCindex_list():
    """公共基础所有题号"""
    GGJCindexlist= models.GGJC_question.objects.all()
    GGJCindexlist = [i[0] for i in GGJCindexlist.values_list()]
    return GGJCindexlist


def get_document(request):
    """获得考试页面说明的信息接口"""
    print('in doc api')
    if request.method == 'GET':
        type = request.GET.get("type")
        print(type)
        if type=='ggjc':
            doc_ggjc=models.Document.objects.get(type=type)
            # print(doc_ggjc.content)
            return HttpResponse(doc_ggjc.content)
        elif type=='jtgc':
            doc_jtgc=models.Document.objects.get(type=type)
            # print(doc_jtgc.content)
            return HttpResponse(doc_jtgc.content)

        elif type=="":return HttpResponse(type+'信息获取错误，缺少type字段或字段错误')
        else:
            return HttpResponse('信息获取错误，缺少type字段或字段错误')

