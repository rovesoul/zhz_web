from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from django.views.decorators import csrf
import json
import datetime
from .AirPortsView import get_zhz_map

# from django.core import serializers
# from .AirPortsView import airport_map
# -----------------------------page部分---

# def maps(request):
#     HttpResponse(airport_map.render_embed())




def Contracts_page(request):
    """
    新项目，
    """
    FridenWeb = models.FriendWebsit.objects.all()
    dicts = {
        'pagename': '合同信息查看',
        'page_title': '各合同信息',
        'FriendWeb': FridenWeb.values_list(),
        'right_title': '备用、后台改',
        'airportsmap':get_zhz_map(),
    }
    return render(request, 'ZHZ_contractMessage.html', dicts)


def All_Contract_json(request):
    """
    获取所有立项项目列表
    """
    NewProjectS = models.Contracts.objects.order_by('-no').all().values()
    data = {}
    data["AllContracts"] = list(NewProjectS)
    return JsonResponse(data, safe=False)



def Contract_findone_json(request, findtext):
    """
    新项目日志的的接口
    """
    print("Airportsfind Json 接口中", findtext, )
    try:
        NPfindtext = models.Contracts.objects.filter(
            Q(p_name__icontains=findtext) | Q(p_no__icontains=findtext) | Q(
                name__icontains=findtext) | Q(no__icontains=findtext) | Q(
                project_status__icontains=findtext) | Q(project_closed__icontains=findtext) | Q(
                confirm_paper__icontains=findtext) | Q(proof__icontains=findtext) | Q(manager_name__icontains=findtext)| Q(
                contract_content__icontains=findtext) | Q(first_party__icontains=findtext)  | Q(notes__icontains=findtext)
        ).values()
        print(NPfindtext)
    except Exception as e:
        print(e)
        NPfindtext = ""
    data = {}
    data["contractsfinded"] = list(NPfindtext)
    return JsonResponse(data, safe=False)

# 分界，上边用了-----------------------------------------------------------

# -----------------------------api部分---
