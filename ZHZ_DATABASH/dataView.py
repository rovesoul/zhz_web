from django.shortcuts import render,redirect
from django.http import HttpResponse
from. import models

# -----------------------------page部分---
def airport_info(request):
    return HttpResponse("机场信息表")

def airport_map(request):
    return HttpResponse("机场地图")

def contracts_info(request):
    return HttpResponse("合同信息")

def contracts_map(request):
    return HttpResponse("合同地图")

def device_info(request):
    return HttpResponse("设备信息表")

def person_info(request):
    return HttpResponse("行业联系人表")

def airport_weak_device(request):
    return HttpResponse("各机场弱电设备，包含涵盖机场数、弱电设备数、-180--365d提示内容")

def luggage_company_info(request):
    return HttpResponse("行李厂商信息，包括厂名、地址、联系人、资质、生产内容、注册年份啥的")


# -----------------------------api部分---