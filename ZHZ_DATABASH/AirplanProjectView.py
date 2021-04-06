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
from .AirPortsView import get_map

# from django.core import serializers
# from .AirPortsView import airport_map
# -----------------------------page部分---

# def maps(request):
#     HttpResponse(airport_map.render_embed())




def AirPort_Page(request):
    """
    新项目，
    """
    FridenWeb = models.FriendWebsit.objects.all()
    dicts = {
        'pagename': '机场信息查看',
        'page_title': '各机场信息',
        'FriendWeb': FridenWeb.values_list(),
        'right_title': '备用、后台改',
        'airportsmap':get_map(),
    }
    return render(request, 'ZHZ_AirportProjectMessage.html', dicts)


def All_Airport_json(request):
    """
    获取所有立项项目列表
    """
    NewProjectS = models.Project_Detail.objects.all().values()
    data = {}
    data["Allairports"] = list(NewProjectS)
    return JsonResponse(data, safe=False)



def Airport_findone_json(request, findtext):
    """
    新项目日志的的接口
    """
    print("Airportsfind Json 接口中", findtext, )
    try:
        NPfindtext = models.Project_Detail.objects.filter(
            Q(p_name__icontains=findtext) | Q(p_no__icontains=findtext) | Q(
                provence__icontains=findtext) | Q(region__icontains=findtext) | Q(
                use_cate__icontains=findtext) | Q(construction_situation__icontains=findtext) | Q(
                run_length__icontains=findtext) | Q(run_class__icontains=findtext) | Q(
                terminal_area__icontains=findtext) | Q(active_time__icontains=findtext)  | Q(throughput__icontains=findtext) | Q(
                aircraft_sorties__icontains=findtext)
        ).values()
        print(NPfindtext)
    except Exception as e:
        print(e)
        NPfindtext = ""
    data = {}
    data["airportsfinded"] = list(NPfindtext)
    return JsonResponse(data, safe=False)

# 分界，上边用了-----------------------------------------------------------

# -----------------------------api部分---
