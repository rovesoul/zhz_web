from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
from django.db.models import Q
from django.http import JsonResponse

from django.views.decorators import csrf
import json
import datetime


# from django.core import serializers

# -----------------------------page部分---
def Person_Page(request):
    """
    新项目，
    """
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    FridenWeb = models.FriendWebsit.objects.all()
    dicts = {
        'pagename': '联系人管理查看',
        'page_title': '各项目干系人',
        'FriendWeb': FridenWeb.values_list(),
        'right_title': '干系人可从NP项目页面创建，也可从本页创建。【想法：项目编号点进项目】备用、后台改'
    }
    return render(request, 'ZHZ_Persons.html', dicts)


def All_Persons_json(request):
    """
    获取所有立项项目列表
    """
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    NewProjectS = models.Person.objects.all().values()
    data = {}
    data["persons"] = list(NewProjectS)
    return JsonResponse(data, safe=False)



def Person_findone_json(request, findtext):
    """
    新项目日志的的接口
    """
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    print("NPNOTE Json 接口中", findtext, )
    try:
        NPfindtext = models.Person.objects.filter(
            Q(p_name__icontains=findtext) | Q(p_no__icontains=findtext) | Q(
                NewProjectID__icontains=findtext) | Q(name__icontains=findtext) | Q(
                title__icontains=findtext) | Q(area__icontains=findtext) | Q(
                address__icontains=findtext) | Q(company__icontains=findtext) | Q(
                email__icontains=findtext) | Q(idNO__icontains=findtext) | Q(
                up_name__icontains=findtext)  | Q(phone__icontains=findtext) | Q(sex__icontains=findtext)
        ).values()
        print(NPfindtext)
    except:
        NPfindtext = ""
    data = {}
    data["personsfinded"] = list(NPfindtext)
    return JsonResponse(data, safe=False)

# 分界，上边用了-----------------------------------------------------------
# NP独立页面
def New_project_oneself(request, NPID):
    """
    新项目独立页面
    """
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    try:
        NP_message = models.NewCompanyProject.objects.filter(NewProjectID=NPID).values().first()
    except:
        NP_message = 'Null'
    try:
        NP_persons = models.Person.objects.filter(NewProjectID=NPID).values()

    except:
        NP_persons = ""
    print("独立页面", NP_persons)
    FridenWeb = models.FriendWebsit.objects.all()
    dicts = {
        'pagename': '项目详情页面',
        'page_title': '新立项项目日志',
        'FriendWeb': FridenWeb.values_list(),
        'right_title': '项目背景及日志记录',
        'NPID': NPID,  # new project项目号
        'NP_message': NP_message,  # new project项目名等
        'NP_Person': NP_persons,

    }
    return render(request, 'ZHZ_NP_Note.html', dicts, )


def NP_NOTE_json(request, NPID):
    """
    新项目日志的的接口
    """
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    print("NPNOTE Json 接口中", NPID, )
    try:
        NPOneselfNotes = models.NP_Note.objects.filter(NewProjectID=NPID).values()
    except:
        NPOneselfNotes = ""
    data = {}
    data["notes"] = list(NPOneselfNotes)
    return JsonResponse(data, safe=False)


def NP_create_person(request):
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    if request.method == 'POST':
        try:
            p_name = request.POST.get('p_name')
            p_no = request.POST.get('p_no')
            New_projectID = request.POST.get('NewProjectID')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            sex = request.POST.get('sex')
            title = request.POST.get('title')
            area = request.POST.get('area')
            address = request.POST.get('address')
            company = request.POST.get('company')
            email = request.POST.get('email')
            idNO = request.POST.get('idNO')
            up_name = request.POST.get('up_name')
            ups_time = datetime.datetime.now()

            print(p_name, name, New_projectID, email, phone, )
            if name != '':
                models.Person.objects.create(
                    p_name=p_name,
                    p_no=p_no,
                    NewProjectID=New_projectID,
                    name=name,
                    phone=phone,
                    sex=sex,
                    title=title,
                    area=area,
                    address=address,
                    company=company,
                    idNO=idNO,
                    email=email,
                    up_name=up_name,
                    ups_time=ups_time,
                )
                returntext = f'{New_projectID}项目,{name},性别{sex}，电话{phone}信息创建成功，请关闭此页。'
                return HttpResponse(returntext)
            else:
                return HttpResponse("姓名为必填项目，请填写!点击浏览器返回继续。")
        except Exception as e:
            print(e)
            return HttpResponse("提交失败,请好好填写，点击浏览器返回继续。")
    else:
        print('没拿到')
    return HttpResponse("获取失败")
    pass


def NP_create_log(request):
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    if request.method == 'POST':
        try:
            NewProjectID = request.POST.get('NewProjectID')
            NewProject_name = request.POST.get('NewProject_name')
            note_one = request.POST.get('note_one')
            ups_time = datetime.datetime.now()

            print(NewProjectID, note_one, ups_time)
            if note_one != '':
                models.NP_Note.objects.create(
                    NewProjectID=NewProjectID,
                    NewProject_name=NewProject_name,
                    note_one=note_one,
                    c_time=ups_time,
                )
                returntext = f'{NewProjectID}项目,事项：{note_one},记录成功。<br><p>请关闭此页。</p>'
                return HttpResponse(returntext)
            else:
                return HttpResponse("如果有记录，事项为必填项，请返回输入。")
        except Exception as e:
            print(e)
            return HttpResponse("提交失败,请好好填写，点击浏览器返回继续。")
    else:
        print('没拿到')
    return HttpResponse("获取失败")
    pass


def get_near_project_note(request):
    """
    新项目的接口
    """
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    near_project_notes = models.NP_Note.objects.all().values()
    data = {}
    data["notes"] = list(near_project_notes)
    print(data["notes"])
    return JsonResponse(data, safe=False)


def NP_create_NP_Page(request):
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    FridenWeb = models.FriendWebsit.objects.all()
    dicts = {
        'pagename': '新建一个项目吧',
        'page_title': '尽可能填全信息创建项目',
        'FriendWeb': FridenWeb.values_list(),
        'right_title': '请填写表单后提交，以创建项目'
    }
    return render(request, 'ZHZ_createNP_Page.html', dicts)


def NP_create_NP_POST(request):
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    if request.method == 'POST':
        def get_new_NP_number():
            """获取新的项目编号"""
            yearNow = datetime.datetime.now().year
            try:
                latestID = models.NewCompanyProject.objects.filter(NewProjectID__contains=yearNow).values().first()
                lastsIDNum = int(latestID['NewProjectID'][-3::])
                new_num = str(lastsIDNum + 1).zfill(3)
                return "NEW-" + str(yearNow) + "-" + new_num
            except Exception as e:
                print(e)
                return "NEW-" + str(yearNow) + "-" + "001"

        try:
            NewProjectID = get_new_NP_number()
            NewProject_name = request.POST.get('NewProject_name')
            Contracts_no = request.POST.get('Contracts_no')
            NewProject_type = request.POST.get('NewProject_type')
            NewProject_status = request.POST.get('NewProject_status')

            money_price_control = request.POST.get('money_price_control')
            monney_buy_biddingDoc = request.POST.get('monney_buy_biddingDoc')
            money_Bid_security_fee = request.POST.get('money_Bid_security_fee')
            money_use_room_fee = request.POST.get('money_use_room_fee')
            money_agency_service_fee = request.POST.get('money_agency_service_fee')
            money_transaction_service_fee = request.POST.get('money_transaction_service_fee')
            money_Performance_bond = request.POST.get('money_Performance_bond')

            NewProjectDoc = request.POST.get('NewProjectDoc')
            p_name = request.POST.get('p_name')
            p_no = request.POST.get('p_no')
            c_time = datetime.datetime.now()

            print('项目创建 post 接口 从前端读取成功')
            if NewProject_name != '':
                models.NewCompanyProject.objects.create(
                    NewProject_name=NewProject_name,
                    NewProjectID=NewProjectID,
                    Contracts_no=Contracts_no,
                    NewProject_type=NewProject_type,
                    NewProject_status=NewProject_status,

                    money_price_control=          money_price_control,
                    monney_buy_biddingDoc=        monney_buy_biddingDoc,
                    money_Bid_security_fee=       money_Bid_security_fee,
                    money_use_room_fee=           money_use_room_fee,
                    money_agency_service_fee=     money_agency_service_fee,
                    money_transaction_service_fee=money_transaction_service_fee,
                    money_Performance_bond=       money_Performance_bond,

                    NewProjectDoc=NewProjectDoc,
                    p_name=p_name,
                    p_no=p_no,
                    c_time=c_time,
                )
                models.NP_Note.objects.create(
                    NewProjectID=NewProjectID,
                    note_one="创建此项目",
                    c_time=c_time,
                )
                returntext = f'{NewProject_name}项目,事项：{NewProject_type},记录成功<br><p>请关闭此页。</p>'
                # return HttpResponse(returntext)
                return HttpResponseRedirect(f"/ZHZ/newproject")
            else:
                return HttpResponse("项目名称为必填项，请返回输入。")
        except Exception as e:
            print(e)
            return HttpResponse(f"提交失败,请好好填写，点击浏览器返回继续。错误内容为{e}")
    else:
        print('没拿到')
    return HttpResponse("获取失败")
    pass





def AirPortMessage_json(request, findtext):
    """
    新项目日志的的接口
    """
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    print("NPNOTE Json 接口中", findtext, )
    try:
        AirPortfinded = models.Project_Detail.objects.filter(
            Q(p_name__icontains=findtext) | Q(p_no__icontains=findtext) | Q(
                provence__icontains=findtext) | Q(region__icontains=findtext) | Q(
                run_class__icontains=findtext) | Q(p_no__icontains=findtext)).values()
        print(AirPortfinded)
    except:
        AirPortfinded = ""
    data = {}
    data["AirPortfinded"] = list(AirPortfinded)
    return JsonResponse(data, safe=False)
# -----------------------------api部分---
