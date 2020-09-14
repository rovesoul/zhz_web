from django.shortcuts import render,redirect
from django.http import HttpResponse
from. import models

# Create your views here.
def roots(request):
    return HttpResponse("这是zhz首页,首页无它，需要探索")

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
        'count_airport_have_weak_device':lists[5],
        'count_airport_device':lists[6],
        'alarm_airport_count':lists[7],
        'count_luggage': lists[8],
    }
    return render(request, 'ZHZHome.html', plugintext)

def get_count_contract():
    """首页数据看板调取数据函数
    主要涵盖各统计参数值
    """
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
    # 有弱电设备信息的机场数量
    count_airport_have_weak_device= models.ProjectDevice.objects.all()
    have_weak_device_set = set([i[1] for i in count_airport_have_weak_device.values_list()]) # (1, '哈尔滨太平机场', '航显', '显.... 筛出机场名不重复
    # 有多少个弱电设备数量
    count_airport_device= models.ProjectDevice.objects.all()
    # 预警
    alarm_airport_count = [10 ] # 这个函数待写完善了，是统计提示日期，见当前日期小于365天，大于-180天的
    # 行李厂商
    count_luggage =[1,2] # 这个函数待写完善了，统计行李厂商数
    list=[len(count_contrast), # 0合同数
          len(devicecount), # 1设备数
          len(count_contact_person), # 2联系人数
          len(count_companys_contract), # 3行业公司合同数
          len(airplane_project), # 4库中机场信息数
          len(have_weak_device_set), # 5有多少机场有弱电设备
          len(count_airport_device), # 6弱电设备数
          len(alarm_airport_count), # 7需要提示机场数
          len(count_luggage),  # 8 需要提示机场数
    ]
    return list

