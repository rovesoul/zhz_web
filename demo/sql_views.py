# Create your views here.
# demo/urls.py


from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse

# CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./demo/templates"))

import json
from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader
from . import models
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse
from pyecharts import options as opts
from pyecharts.charts import Geo, Tab
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker
from pyecharts.globals import ChartType
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar

# 固定sql语法合集
sqls = {'1': "select d_name,d_type from zhz_device GROUP BY d_name,d_type ORDER BY d_name;",
        '2': "select standard from zhz_device GROUP BY standard ORDER BY standard;",
        '3': "select d_name,d_type,usefor,standard from zhz_device GROUP BY d_name,d_type ,usefor,standard ORDER BY d_name desc;",
        '4': "select standard,d_name,d_type,usefor from zhz_device GROUP BY standard, d_name,d_type ,usefor ORDER BY standard desc;",
        '5': "select * from zhz_device ORDER BY d_name desc; ",
        '6': "",
        '7': "SELECT p_name,person_name,person_phone ,person_title,company,sex,DATE_FORMAT(ups_date,'%Y-%m-%d') as ups_date  FROM person ORDER BY convert(p_name using utf8) ASC,convert(person_name using utf8) DESC ;",
        '8': "SELECT person_name ,p_name,person_phone ,person_title,company,sex,DATE_FORMAT(ups_date,'%Y-%m-%d') as ups_date  FROM person ORDER BY  convert(person_name using gbk) ASC,convert(p_name using utf8) DESC  ;",
        '9': "SELECT person_title,person_name ,p_name,person_phone ,company,sex,DATE_FORMAT(ups_date,'%Y-%m-%d') as ups_date  FROM person ORDER BY  convert(person_title using gbk) asc,convert(p_name using gbk) ASC ;",
        '10': "SELECT company,person_name ,person_title,person_phone ,sex,p_name,DATE_FORMAT(ups_date,'%Y-%m-%d') as ups_date  FROM person ORDER BY  convert(company using gbk) asc,convert(person_name using gbk) ASC ;",
        '11': "SELECT COUNT(*) from contracts;",  # datashbash 的合同数
        '12': "SELECT COUNT(DISTINCT d_name) FROM zhz_device;",  # datashbash 的zhz设备数，去重
        '13': "SELECT COUNT(*) FROM person;",  # datashbash 的联系人数数
        '14': "SELECT COUNT(DISTINCT company_name) FROM trade_contract;",  # datashbash 的公司数，去重
        '15': "SELECT COUNT(DISTINCT company_name) FROM trade_contract;",  # datashbash 的多少个机场的弱电设备
        '16': "SELECT COUNT(d_name) FROM project_device;",  # datashbash 机场的弱电设备已有统计数
        '17': "select * from (SELECT COUNT(*) 合同数 from contracts) a,(SELECT COUNT(DISTINCT d_name) 设备数 FROM zhz_device  ) b,(SELECT COUNT(*) 联系人数 FROM person) c,(SELECT COUNT(DISTINCT company_name) 行业公司数 FROM trade_contract) d,(SELECT COUNT(DISTINCT p_name) 已有弱电设备机场数 FROM project_device) e,(SELECT COUNT(d_name) 机场弱电设备数  FROM project_device)  f ;"
        }


# Create your views here.
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


JsonResponse = json_response
JsonError = json_error


def all_zhz_device(request):
    """中航质所有设备信息"""
    dic = {}
    if request.method == 'GET':
        sql = "select d_name,d_type from zhz_device GROUP BY d_name,d_type ORDER BY d_name;"
        df = models.get_status_withname(sql)
        columns = df.columns.tolist()
        df = df.to_dict(orient='index')
        print('all_device:', len(df))
        return JsonResponse(df, columns=columns)
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        return JsonResponse(json.dumps(dic, ensure_ascii=False))


def device_sql_change(request):
    """中航质所有设备信息"""
    dic = {}
    if request.method == 'GET':
        num = request.GET.get("num")
        print(num)
        sql = sqls[num]
        print('sql is -->:', sql)
        df = models.get_status_withname(sql)
        columns = df.columns.tolist()
        df = df.to_dict(orient='index')
        print('device_sql_change:', len(df))
        return JsonResponse(df, columns=columns)
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        return JsonResponse(json.dumps(dic, ensure_ascii=False))


def device_sql_amb(request):
    """中航质所有设备信息"""
    dic = {}
    if request.method == 'GET':
        text = request.GET.get("text")
        text = str(text).replace(" ", "%")

        print('查找关键字:', text)
        sql_left = 'SELECT d_name,d_type,usefor,standard FROM zhz_device WHERE CONCAT(d_name,d_type,usefor,standard) LIKE "%'
        sql_rigth = '%"  ORDER BY standard ;'
        sqls = sql_left + text + sql_rigth

        df = models.get_status_withname(sqls)
        columns = df.columns.tolist()
        df = df.to_dict(orient='index')
        print('模糊搜索出个数:', len(df))
        return JsonResponse(df, columns=columns)
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        return JsonResponse(json.dumps(dic, ensure_ascii=False))


def add_device_sql(request):
    """中航质所有设备信息"""
    dic = {}
    if request.method == 'GET':
        d_name = str(request.GET.get("d_name"))
        d_type = request.GET.get("d_type")
        quantity = request.GET.get("quantity")
        append = request.GET.get("append")
        usefor = request.GET.get("usefor")
        standard = request.GET.get("standard")
        todays = request.GET.get("todays")
        if len(d_name) != 0:
            print(d_name, d_type, quantity, append, usefor, standard, todays)
            # insert 语句
            sqlx = f'INSERT INTO zhz_device ( d_name,d_type,quantity,append,usefor,standard,ups_date ) VALUES ( "{d_name}","{d_type}","{quantity}","{append}","{usefor}","{standard}","{todays}");'
            print(sqlx)
            #
            d = models.insert_status(sqlx)
            print(d)
            dic['insert_status'] = str(d)
            # print('add_device:',dic)
            # columns = df.columns.tolist()
            # print('add_device:',len(df))
            return JsonResponse(json.dumps(dic, ensure_ascii=False), msg="提交插入数据成功")
        else:
            dic['未知'] = 500
            dic['asdf'] = 800
            dic['insert_status'] = '0'
            return JsonResponse(json.dumps(dic, ensure_ascii=False), msg="提交插入数据失败，设备名不能为空")
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        dic['insert_status'] = '0'
        return JsonResponse(json.dumps(dic, ensure_ascii=False), msg="提交插入数据失败，设备名不能为空")


def all_person(request):
    """中航质所有人员信息"""
    dic = {}
    if request.method == 'GET':
        sql = "SELECT p_name,person_name,person_phone ,person_title,company,sex,DATE_FORMAT(ups_date,'%Y-%m-%d') as ups_date  FROM person ORDER BY convert(p_name using utf8) ASC,convert(person_name using utf8) DESC ;"
        df = models.get_status_withname(sql)
        columns = df.columns.tolist()
        df = df.to_dict(orient='index')
        print('all_person:', len(df))
        return JsonResponse(df, columns=columns)
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        return JsonResponse(json.dumps(dic, ensure_ascii=False))


def person_sql_change(request):
    """变换语法查人内容sql"""
    if request.method == 'GET':
        num = request.GET.get("num")
        print(num)
        sql = sqls[num]
        print('sql is -->:', sql)
        df = models.get_status_withname(sql)
        print(df)
        columns = df.columns.tolist()
        df = df.to_dict(orient='index')
        print('device_sql_change:', len(df))
        print('拿到返回了')

        return JsonResponse(df, columns=columns)
    else:
        pass
        data = {}
        data['未知'] = 500
        data['asdf'] = 800
        return JsonResponse(json.dumps(data, ensure_ascii=False))


def add_person_sql(request):
    """添加人员"""
    dic = {}
    if request.method == 'GET':
        person_name = str(request.GET.get("person_name"))
        person_phone = str(request.GET.get("person_phone"))
        person_title = str(request.GET.get("person_title"))
        company = str(request.GET.get("company"))
        email = str(request.GET.get("email"))
        sex = str(request.GET.get("sex"))
        area = str(request.GET.get("area"))
        id = str(request.GET.get("id"))
        p_name = str(request.GET.get("p_name"))
        todays = request.GET.get("todays")
        if person_phone == '': person_phone = "None"
        if person_title == '': person_title = "None"
        if company == '': company = "None"
        if email == '': email = "None"
        if area == '': area = "None"
        if id == '': id = "None"
        if p_name == '': p_name = "None"

        if len(person_name) != 0:
            print(person_name, person_phone, person_title, p_name, company, email, sex, area, id, todays)
            # insert 语句
            sqlx = f'INSERT INTO person ( p_name, person_name,person_phone,person_title,company,sex,id ,area,email,ups_date) VALUES ( "{p_name}", "{person_name}","{person_phone}", "{person_title}", "{company}", "{sex}", "{id}", "{area}","{email}","{todays}" );'
            print(sqlx)
            #
            d = models.insert_status(sqlx)
            print(d)
            dic['insert_status'] = str(d)
            # print('add_device:',dic)
            # columns = df.columns.tolist()
            # print('add_device:',len(df))
            return JsonResponse(json.dumps(dic, ensure_ascii=False), msg="提交插入数据成功")
        else:
            dic['未知'] = 500
            dic['asdf'] = 800
            dic['insert_status'] = '0'
            return JsonResponse(json.dumps(dic, ensure_ascii=False), msg="提交插入数据失败，设备名不能为空")
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        dic['insert_status'] = '0'
        return JsonResponse(json.dumps(dic, ensure_ascii=False), msg="提交插入数据失败，设备名不能为空")


def person_sql_amb(request):
    """人员模糊搜索"""
    dic = {}
    if request.method == 'GET':
        text = request.GET.get("text")
        text = str(text).replace(" ", "%")

        print('查找关键字:', text)
        sql_left = 'select person_name,person_phone ,person_title,company,sex,p_name,area,id,DATE_FORMAT(ups_date,"%Y-%m-%d") as ups_date,email FROM person where CONCAT(person_name,person_phone ,person_title,company,sex,p_name,area,id,ups_date,email) like"%'
        sql_rigth = '%" ORDER BY convert(person_name using utf8) ASC ;'
        sqls = sql_left + text + sql_rigth

        df = models.get_status_withname(sqls)
        columns = df.columns.tolist()
        df = df.to_dict(orient='index')
        print('模糊搜索出个数:', len(df))
        return JsonResponse(df, columns=columns)
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        return JsonResponse(json.dumps(dic, ensure_ascii=False))

def all_contract(request):
    """合同信息"""
    dic = {}
    if request.method == 'GET':
        sql = "select project_detail.p_name,project_detail.p_no, contract_name,contract_no, DATE_FORMAT(signing_date,'%Y-%m-%d') as signing_date ,first_party,province,region,DATE_FORMAT(active_time,'%Y-%m-%d') as active_time  from contracts, project_detail where contracts.p_name = project_detail.p_name or contracts.p_no = project_detail.p_no ORDER BY signing_date DESC, province DESC;"
        df = models.get_status_withname(sql)
        columns = df.columns.tolist()
        df = df.to_dict(orient='index')
        print(df)
        return JsonResponse(df,columns=columns)
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        return JsonResponse(json.dumps(dic, ensure_ascii=False))

def contract_sql_amb(request):
    """人员模糊搜索"""
    dic = {}
    if request.method == 'GET':
        text = request.GET.get("text")
        text = str(text).replace(" ", "%")

        print('查找关键字:', text)
        sql_left = 'select contract_name 合同名 , contract_no 合同编号, project_detail.p_name 项目名,terminal_area 航站楼面积, DATE_FORMAT(signing_date,"%Y-%m-%d") as 签约日期, DATE_FORMAT(active_time,"%Y-%m-%d") as 机场运营日,province 省份,region 区域 FROM contracts,project_detail where CONCAT(contract_name,contract_no,signing_date,contracts.p_name,active_time,region,province) like "%'
        sql_rigth = '%" and contracts.p_name = project_detail.p_name ORDER BY contract_name;'
        sqlx = sql_left + text + sql_rigth
        # print(sqlx)
        df = models.get_status_withname(sqlx)
        # print(df)
        columns = df.columns.tolist()
        df = df.to_dict(orient='index')
        print('模糊搜索出个数:', len(df))
        return JsonResponse(df, columns=columns)
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        return JsonResponse(json.dumps(dic, ensure_ascii=False))

def count_contract():
    sql = sqls['11']


def count_zhz_device():
    sql = sqls['12']


def count_person():
    sql = sqls['13']


def count_company():
    sql = sqls['14']


def count_weak_equipment_airport():
    sql = sqls['15']


def count_weak_equipment_all():
    sql = sqls['16']


def count_together(request):
    dic={}
    if request.method == 'GET':
        sql = sqls['17']
        df = models.get_status_withname(sql)
        print(df)
        columns = df.columns.tolist()
        df = df.to_dict(orient='index')
        print('all_person:', len(df))
        return JsonResponse(df, columns=columns)
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        return JsonResponse(json.dumps(dic, ensure_ascii=False))


def add_contract_sql(request):
    """中航质所有设备信息"""
    dic = {}
    if request.method == 'GET':
        contract_name = str(request.GET.get("contract_name"))
        contract_no = str(request.GET.get("contract_no"))
        contract_amount = str(request.GET.get("contract_amount"))
        signing_date = str(request.GET.get("signing_date"))
        p_name = str(request.GET.get("p_name"))
        p_no = str(request.GET.get("p_no"))
        first_party = str(request.GET.get("first_part"))
        notes = str(request.GET.get("notes"))
        todays = str(request.GET.get("todays"))

        if len(contract_name) != 0:
            print(contract_name, contract_no, contract_amount, signing_date, p_name, p_no, first_party,notes,todays)
            # insert 语句
            sqlx = f'INSERT INTO contracts ( contract_name,contract_no, contract_amount, signing_date, p_name, p_no, first_party,notes,ups_date ) VALUES ("{contract_name}","{contract_no}","{contract_amount}","{signing_date}","{p_name}","{p_no}","{first_party}","{notes}","{todays}" );'
            print(sqlx)
            # #
            d = models.insert_status(sqlx)
            print(d)
            dic['insert_status'] = str(d)
            # print('add_device:',dic)
            # columns = df.columns.tolist()
            # print('add_device:',len(df))
            return JsonResponse(json.dumps(dic, ensure_ascii=False), msg="提交插入数据成功")
        else:
            dic['未知'] = 500
            dic['asdf'] = 800
            dic['insert_status'] = '0'
            return JsonResponse(json.dumps(dic, ensure_ascii=False), msg="提交插入数据失败，设备名不能为空")
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        dic['insert_status'] = '0'
        return JsonResponse(json.dumps(dic, ensure_ascii=False), msg="提交插入数据失败，设备名不能为空")


def get_p_no_sql_amb(request):
    """人员模糊搜索"""
    dic = {}
    if request.method == 'GET':
        text = request.GET.get("text")
        text = str(text).replace(" ", "%")

        print('查找关键字:', text)
        sql_left = 'select p_name,p_no,province,region FROM project_detail where  CONCAT(p_name,p_no,province,region) like "%'
        sql_rigth = '%"  ORDER BY p_name asc;'
        sqlx = sql_left + text + sql_rigth
        print(sqlx)
        df = models.get_status_withname(sqlx)
        # print(df)
        columns = df.columns.tolist()
        df = df.to_dict(orient='index')
        print('模糊搜索出个数:', len(df))
        return JsonResponse(df, columns=columns)
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        return JsonResponse(json.dumps(dic, ensure_ascii=False))