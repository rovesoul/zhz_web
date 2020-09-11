from django.shortcuts import render,redirect
from django.http import HttpResponse
from. import models

# Create your views here.
def roots(request):
    return HttpResponse("这是zhz首页,首页无它")

def choice(request):
    if not request.session.get("is_login", None):
        return redirect("/demo/login")
    lists = get_count_contract()
    plugintext={
        'pagename':'ZHZ-数据信息统计',
        'page_title': 'ZHZ-数据信息统计',
        'left_title':'left title',
        'right_title':'right title',
        'count_contrast':lists[0],
        'count_self_device':lists[1],
        'count_contact_person':lists[2],
        'count_companys_contract':lists[3],
        'count_airplane_project':lists[4],
        'count_airport_have_weak_device':10,
        'count_airport_device':8000,
    }
    return render(request, 'ZHZHome.html', plugintext)

def get_count_contract():
    """拿到首页数据信息信息"""
    # 库里已有机场数
    airplane_project = models.Project_Detail.objects.all()
    # 合同数
    count_contrast= models.Contracts.objects.all()
    # 设备数
    count_self_device= models.Device.objects.all()
    devicecount =set([i[1] for i in count_self_device.values_list()])
    # 人员数
    count_contact_person= models.Person.objects.all()
    # 各机场公司数
    count_companys_contract= models.TradeContracts.objects.all()
    count_airport_have_weak_device= models.ProjectDevice.objects.all()
    count_airport_device= models.ProjectDevice.objects.all()

    list=[len(count_contrast),len(devicecount),len(count_contact_person),len(count_companys_contract),len(airplane_project)]
    return list

