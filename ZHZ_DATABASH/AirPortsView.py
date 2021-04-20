from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
from django.db.models import Q
from django.http import JsonResponse
import mysql.connector
from django.views.decorators import csrf

import datetime

from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.template import  loader
from . import  models
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse
from pyecharts import options as opts
from pyecharts.charts import  Geo,Tab
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker
from pyecharts.globals import ChartType

from pyecharts import options as opts
from pyecharts.charts import Bar

# from django.core import serializers
from django.db import connection, connections

# cursor = connections['default'].cursor()

# -----------------------------page部分---

def close_old_connections():
    """关闭连接池函数"""
    connnum = 0
    for conn in connections.all():
        connnum += 1
        conn.close_if_unusable_or_obsolete()
        print('close conn', connnum)

# 数据源


def get_map():

    df_jiyou = models.Project_Detail.objects.filter(construction_situation="既有")
    df_zaijian = models.Project_Detail.objects.filter(construction_situation="在建")
    df_xinzeng = models.Project_Detail.objects.filter(construction_situation="新增")
    df_yanjiubuju = models.Project_Detail.objects.filter(construction_situation="研究布局")
    # 时间转换
    def change2date(dates):
        if str(dates) == "NaT": return "待补充"
        try:
            dates = str(dates)[0:10]
            return dates  # 制定输出日期的格式
        except:
            # print(f'没转换{dates}')
            return dates

    c = (
        Geo({"title_pos": "center", 'width':'98%','theme': ThemeType.WESTEROS, }, )
            .add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(
                color="white", border_color="#666", color0='#222'),

            label_opts=opts.LabelOpts(
                color='#404a59', border_color='#404a59', font_size=12, position='center'),

        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="全国机场分布", ), )

    )

    def add_points(df_data, colors='red'):
        points_list = df_data
        for num in points_list:
            try:
                c.add_coordinate(num.p_name, num.longitude, num.latitude)

                # print('加值')
                c.add(
                    num.construction_situation,
                    [(num.p_name, f'编号{num.p_no}<br>航站楼面积:{num.terminal_area}<br>跑道长度:{num.run_length}<br>跑道等级:{num.run_class}<br>启用时间:{change2date(num.active_time)}<br>吞吐量：{num.throughput}')],
                    type_=ChartType.SCATTER,
                    point_size=5,
                    # SCATTER 单独点
                    # color=colors,
                    label_opts=opts.LabelOpts(is_show=False, ),
                    is_selected=True,
                    symbol_size=9,
                )
            except:print('加点失败')


    print('准备加点')
    add_points(df_jiyou,)
    add_points(df_zaijian,)
    add_points(df_xinzeng,)
    add_points(df_yanjiubuju,)


    return c.render_embed

def get_zhz_map():
    cursor = connection.cursor()
# def get_zhz_map(request):
    # df_zhz = models.Project_Detail.objects.filter(construction_situation="在建")
    # df_zhz = models.Project_Detail.objects.raw('SELECT contracts.p_name,  project_detail.longitude, project_detail.latitude,project_detail.terminal_area,project_detail.run_length,project_detail.run_class,project_detail.active_time,contracts.contract_name from contracts,project_detail where contracts.p_name=project_detail.p_name;')
    cursor.execute('SELECT ZHZ_DATABASH_contracts.p_name, ZHZ_DATABASH_project_detail.longitude,ZHZ_DATABASH_project_detail.latitude,ZHZ_DATABASH_project_detail.terminal_area,ZHZ_DATABASH_project_detail.run_length,ZHZ_DATABASH_project_detail.run_class,ZHZ_DATABASH_project_detail.active_time,ZHZ_DATABASH_contracts.name from ZHZ_DATABASH_contracts,ZHZ_DATABASH_project_detail where ZHZ_DATABASH_contracts.p_no=ZHZ_DATABASH_project_detail.p_no;')
    df_zhz =cursor.fetchall()
    # 时间转换
    def change2date(dates):
        if str(dates) == "NaT": return "待补充"
        try:
            dates = str(dates)[0:10]
            return dates  # 制定输出日期的格式
        except:
            # print(f'没转换{dates}')
            return dates

    c = (
        Geo({"title_pos": "center", 'width':'98%', }, )
            .add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(
                color="#404a59", border_color="#999", color0='#333'),

            label_opts=opts.LabelOpts(
                color='#dark', border_color='#404a59', font_size=13, position='center'),

        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="中航质项目分布", ), )

    )

    def add_points(df_data, colors='red'):
        points_list = df_data
        print(points_list)
        for num in points_list:
            print(num)
            try:
                c.add_coordinate(num[0], num[1], num[2])

                # print('加值')
                c.add(
                    "中航质检测项目",
                    [(num[0], f'<br>航站楼面积:{num[3]}<br>跑道长度:{num[4]}<br>跑道等级:{num[5]}<br>启用时间:{change2date(num[6])}<br>合同名:{num[7][0:18]}')],
                    #
                    type_=ChartType.SCATTER,
                    point_size=5,
                    # SCATTER 单独点
                    color="yellow",
                    label_opts=opts.LabelOpts(is_show=False, ),
                    is_selected=True,
                    symbol_size=9,
                )
            except:print('加点失败')


    print('准备加点')
    add_points(df_zhz,)


    close_old_connections()
    return c.render_embed
    # return HttpResponse(c.render_embed())

