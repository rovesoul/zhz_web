from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
from django.db.models import Q
from django.http import JsonResponse
from .forms import RegistNPPerson
from django.views.decorators import csrf
import json
import datetime


# from django.core import serializers

# -----------------------------page部分---
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response

def json_response(datas, code=200, columns='待输入', msg='success'):
    data = {
        "code": code,
        "msg": msg,
        "data": datas,
        "columns": columns,
        'lens': len(datas),

    }
    return response_as_json(data)

def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)

JsonResponseBG = json_response
JsonErrorBG = json_error


def New_project(request):
    """
    新项目，
    """
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    FridenWeb = models.FriendWebsit.objects.all()
    dicts = {
        'pagename': '新立项项目管理',
        'page_title': '新立项项目管理',
        'FriendWeb': FridenWeb.values_list(),
        'right_title': '新立项项目列表'
    }
    return render(request, 'ZHZ_NewProject.html', dicts)


def New_project_json(request):
    """
    获取所有立项项目列表
    """
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    NewProjectS = models.NewCompanyProject.objects.all().values()
    data = {}
    data["projects"] = list(NewProjectS)
    return JsonResponse(data, safe=False)


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
                    NewProject_name=NewProject_name,
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


def NP_NPS_json(request, findtext):
    """
    新项目日志的的接口
    """
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    print("NPNOTE Json 接口中", findtext, )
    try:
        NPfindtext = models.NewCompanyProject.objects.filter(
            Q(NewProjectID__icontains=findtext) | Q(NewProject_name__icontains=findtext) | Q(
                NewProject_type__icontains=findtext) | Q(NewProject_status__icontains=findtext) | Q(
                p_name__icontains=findtext) | Q(p_no__icontains=findtext)).values()
        print(NPfindtext)
    except:
        NPfindtext = ""
    data = {}
    data["npsfinded"] = list(NPfindtext)
    return JsonResponse(data, safe=False)


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


def ChangeNP_BG(request,NPID):
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
        'page_title': '修改项目信息'+str(NPID),
        'FriendWeb': FridenWeb.values_list(),
        'right_title': NP_message['NewProject_name'],
        'NPID': NPID,  # new project项目号


    }
    return render(request, 'ZHZ_NP_ChangeBackground.html', dicts)


def CH_NP_NOTE_json(request, NPID):
    """
    获取项目背景信息，准备更新用
    """
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")
    print("CH_NP_NOTE_json Json 接口中", NPID, )
    try:
        NP_message = models.NewCompanyProject.objects.filter(NewProjectID=NPID).values().first()
    except:
        NP_message = 'Null'
    data = {}
    data["message"] =NP_message
    return JsonResponse(data, safe=False)


def CH_NP_NOTE(request):
    """提交新项目信息"""
    if not request.session.get("is_login", None):
        return redirect("/ZHZ/login")

    dic = {}
    print('prepare GET')
    if request.method == 'GET':
        try:
            NewProjectDoc = str(request.GET.get("NewProjectDoc"))
            NewProjectID = request.GET.get("NewProjectID")
            Contracts_no = request.GET.get("Contracts_no")
            NewProject_name = request.GET.get("NewProject_name")
            NewProject_status = request.GET.get("NewProject_status")
            NewProject_type = request.GET.get("NewProject_type")
            money_Bid_security_fee = request.GET.get("money_Bid_security_fee")
            money_Performance_bond = request.GET.get("money_Performance_bond")
            money_agency_service_fee = request.GET.get("money_agency_service_fee")
            money_price_control = request.GET.get("money_price_control")
            money_transaction_service_fee = request.GET.get("money_transaction_service_fee")
            money_use_room_fee = request.GET.get("money_use_room_fee")
            monney_buy_biddingDoc = request.GET.get("monney_buy_biddingDoc")
            chinesename = request.GET.get("chinesename")
            oneNP = models.NewCompanyProject.objects.get(NewProjectID=NewProjectID)
            # 增加log
            models.NP_Note.objects.create(
                NewProjectID=NewProjectID,
                NewProject_name=NewProject_name,
                note_one="修改项目背景信息",
                notename=chinesename,
                c_time=datetime.datetime.now(),
            )

            print('get in:::',NewProject_name,oneNP.NewProjectID)
            oneNP.NewProjectDoc=NewProjectDoc
            oneNP.Contracts_no=Contracts_no
            oneNP.NewProject_name=NewProject_name
            oneNP.NewProject_status=NewProject_status
            oneNP.NewProject_type=NewProject_type
            oneNP.money_Bid_security_fee=money_Bid_security_fee
            oneNP.money_Performance_bond=money_Performance_bond
            oneNP.money_agency_service_fee=money_agency_service_fee
            oneNP.money_price_control=money_price_control
            oneNP.money_transaction_service_fee=money_transaction_service_fee
            oneNP.money_use_room_fee=money_use_room_fee
            oneNP.monney_buy_biddingDoc=monney_buy_biddingDoc
            oneNP.save()

            print("更新ok")

            dic['insert_status'] = "upBG just ok"
            # print('add_device:',dic)
            # columns = df.columns.tolist()
            # print('add_device:',len(df))
            return JsonResponseBG(json.dumps(dic, ensure_ascii=False), msg="跟新信息成功")
        except Exception as e:
            print(e)
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        dic['insert_status'] = '0'
        return JsonResponseBG(json.dumps(dic, ensure_ascii=False), msg="提交插入数据失败，设备名不能为空")



# -----------------------------api部分---
