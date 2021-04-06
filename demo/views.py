# Create your views here.
# demo/urls.py


from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse

# CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./demo/templates"))

import json
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
import pandas as pd
import  numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar


def home(request):
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    return render(request, 'home.html', locals())






# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200,columns='待输入'):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
        "columns":columns,
        'lens':len(data),
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

"""1个柱状的柱状图"""
def bar1yaxis(sqlword,titlename="请输入标题名字",subtitlename="请输入副标题") -> Bar:
    """全国机场建设情况"""
    print('sql is:',sqlword)
    df=models.get_status(sqlword)  # 得到数据表
    xas=df[0].tolist()
    yas=df[1].tolist()
    c = (
        Bar()
            .add_xaxis(xas)
            .add_yaxis("", yas)
            .set_global_opts(title_opts=opts.TitleOpts(title=titlename, subtitle=subtitlename,))
            .dump_options_with_quotes()
    )
    return c

def bar4yaxis(sqlword,titlename="请输入标题名字",subtitlename="请输入副标题") -> Bar:
    """全国各区域机场建设情况"""
    print('sql is:',sqlword)
    jiyou_sql = 'SELECT * from (select region,count(region) m FROM project_detail GROUP BY region) a LEFT JOIN  (SELECT region  ,count(region) 在建  FROM project_detail where construction_situation = "在建" GROUP BY (region)) b  ON a.region = b.region  LEFT JOIN  (SELECT region ,count(region) 新增  FROM project_detail where construction_situation = "新增" GROUP BY (region)) c ON a.region = c.region LEFT JOIN (SELECT region ,count(region) 既有  FROM project_detail where construction_situation = "既有" GROUP BY (region)) d ON a.region = d.region LEFT JOIN  (SELECT region ,count(region) 研究布局  FROM project_detail where construction_situation = "研究布局" GROUP BY (region)) e ON a.region = e.region LEFT JOIN (select region , count(DISTINCT(project_detail.p_name)) 我司合同数 from project_detail,contracts where project_detail.p_no = contracts.p_no GROUP BY region) f ON  a.region=f.region ORDER BY m DESC ;'
    df=models.get_status(jiyou_sql)  # 得到数据表
    xaxis=df[0].tolist()
    # print(xaxis)
    y1=df[3].tolist() #在建
    y2=df[5].tolist() #新增
    y3=df[7].tolist() #既有
    y4=df[9].tolist() #布局
    y5=df[11].tolist() #我司参与

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(xaxis)
            .add_yaxis("既有", y3, stack="stack1")
            .add_yaxis("在建", y1, stack="stack1")
            .add_yaxis("新增", y2, stack="stack1")
            .add_yaxis("布局", y4, stack="stack1")
            .add_yaxis("我司参与机场", y5, stack="stack2")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False,))
            .set_global_opts(title_opts=opts.TitleOpts(title=titlename, subtitle=subtitlename,),
                             toolbox_opts=opts.ToolboxOpts(),)
            .dump_options_with_quotes()
    )
    return c


def bar2yaxis(sqlword,titlename="请输入标题名字",subtitlename="请输入副标题") -> Bar:
    """全国各区域机场建设情况"""
    print('sql is:',sqlword)
    jiyou_sql = 'select a.province,省总数,我司参与数 from (SELECT province ,count(province) as 省总数 FROM project_detail  GROUP BY (province) order BY 省总数 DESC) a LEFT JOIN (select province , count(DISTINCT(project_detail.p_name)) 我司参与数 from project_detail,contracts where project_detail.p_no = contracts.p_no GROUP BY province ) b  ON a.province = b.province;'
    df=models.get_status(jiyou_sql)  # 得到数据表
    xaxis=df[0].tolist()
    # print(xaxis)
    y1=df[1].tolist() #省市总数
    y2=df[2].tolist() #我司参与项目
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(xaxis)
            .add_yaxis("机场数量", y1, stack="stack1")
            .add_yaxis("我司参与机场", y2, stack="stack2")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True,))
            .set_global_opts(title_opts=opts.TitleOpts(title=titlename, subtitle=subtitlename,),
                             toolbox_opts=opts.ToolboxOpts(),
                             datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],)
            .dump_options_with_quotes()
    )
    return c


"""带缩放调节的"""
def bar_province() -> Bar:
    """全国机场建设情况"""
    sqlword = 'SELECT province ,count(*) as ct FROM project_detail  GROUP BY (province) order BY ct DESC;'
    df=models.get_status(sqlword)  # 得到数据表
    xas=df[0].tolist()
    yas=df[1].tolist()
    c = (
        Bar()
            .add_xaxis(xas)
            .add_yaxis("", yas)
            .set_global_opts(title_opts=opts.TitleOpts(title="", subtitle="ZHZ",),#全国省市机场数量统计
                             datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
                             )

            .dump_options_with_quotes()
    )
    return c




# ----------------------------API部分
# 这个固定了
def cs_api(request):
    """一个json的api案例模板
    全国机场数据"""
    dic = {}
    if request.method == 'GET':
        sqlword = 'SELECT construction_situation ,count(*) as ct  FROM project_detail  GROUP BY (construction_situation) order by ct desc ;'
        titlename = ''#全国机场统计
        subname='ZHZ'
        return JsonResponse(json.loads(bar1yaxis(sqlword,titlename,subname)))
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        return HttpResponse(json.dumps(dic, ensure_ascii=False))


# 这个固定了
def region_api(request):
    """一个json的api案例模板
    区域数据
    """
    dic = {}
    if request.method == 'GET':
        sqlword = 'SELECT region ,count(*) as ct  FROM project_detail GROUP BY (region) order by ct desc ;'
        titlename = ''# 各区域机场数量统计
        subname = 'ZHZ'
        return JsonResponse(json.loads(bar4yaxis(sqlword,titlename,subname)))
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        return HttpResponse(json.dumps(dic, ensure_ascii=False))

def province_api(request):
    """一个json的api案例模板
    省市数据
    """
    dic = {}
    if request.method == 'GET':
        return JsonResponse(json.loads(bar2yaxis("",'','zhz')))#全国省市机场数量统计
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        return HttpResponse(json.dumps(dic, ensure_ascii=False))


def guo_report(request):
    # select    province, difi_re_num    from REPORT_REG
    c=(Geo()
        .add_schema(
            maptype="china",
            )
        # .add_coordinate('朱日和机场', 87.349731, 31.768337)
        # .add("geo",[['朱日和机场','asdfasdfasdfasdf']])
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())],type_=ChartType.SCATTER,)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .dump_options_with_quotes())
    return JsonResponse(json.loads(c))

# -----------------------------------返回地图
# 数据源
df_zaijian = models.get_status_withname('select * from project_detail where construction_situation ="在建" ;')
df_new = models.get_status_withname('select * from project_detail where construction_situation ="新增" ;')
df_jiyou = models.get_status_withname('select * from project_detail where construction_situation ="既有" ;')
df_plan = models.get_status_withname('select * from project_detail where construction_situation ="研究布局" ;')
df_zhz = models.get_status_withname('SELECT contracts.p_name,  project_detail.longitude, project_detail.latitude,project_detail.terminal_area,project_detail.run_length,project_detail.run_class,project_detail.active_time,contracts.contract_name from contracts,project_detail where contracts.p_name=project_detail.p_name;')

# CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./demo/templates"))

# def allflight(request):
def allflight() -> Geo:
    # 时间转换
    def change2date(dates):
        if str(dates) =="NaT":return "待补充"
        try:
            dates = str(dates)[0:10]
            return dates  # 制定输出日期的格式
        except:
            # print(f'没转换{dates}')
            return dates



    c = (
        Geo({"title_pos": "center", "width": "1280px","height": "700px", 'theme': ThemeType.WESTEROS,}, )
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
        points_list = df_data.values.tolist()
        for num in points_list:
            # print('加点')
            c.add_coordinate(num[0], num[2], num[3])
            print(num[7])
            # print('加值')
            c.add(
                num[7],
                [(num[0], f'<br>航站楼面积:{num[8]}<br>跑道长度:{num[12]}<br>跑道等级:{num[13]}<br>启用时间:{change2date(num[9])}')],
                type_=ChartType.SCATTER,
                point_size=5,
                # SCATTER 单独点
                # color=colors,
                label_opts=opts.LabelOpts(is_show=False, ),
                is_selected=True,
                symbol_size=9,
            )

    add_points(df_jiyou, )
    add_points(df_new, )
    add_points(df_zaijian, )
    add_points(df_plan, )

    return c

# def zhzproject(request):
def zhz_p() -> Geo:
    def change2date(dates):
        try:
            dates = int(dates)
            delta = pd.Timedelta(str(dates) + 'D')
            real_time = pd.to_datetime('1899-12-30') + delta
            # 将1899-12-30转化为可以计算的时间格式并加上要转化的日期戳
            real_time = str(real_time)[0:7].replace('-', "年") + '月'
            return real_time  # 制定输出日期的格式
        except:
            # print(f'没转换{dates}')
            return dates



    c = (
        Geo({"title_pos": "center", "width": "1280px", "height": "700px"})
            .add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(
                color="#404a59", border_color="#999", color0='#333'),
            label_opts=opts.LabelOpts(
                color='dark', font_size=13, position='center'),
            #
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="中航质项目分布"))

    )
    def add_point(df_data):
        """数据源获取"""
        points_list = df_data.values.tolist()
        for num in points_list:
            # print('加点')
            c.add_coordinate(num[0], num[1], num[2])
            # print('加值')
            c.add(
                "中航质检测项目",
                [(num[0], f'<br>航站楼面积:{num[3]}<br>跑道长度:{num[4]}<br>跑道等级:{num[5]}<br>启用时间:{change2date(num[6])}<br>合同名:{num[7]}')],#
                type_=ChartType.EFFECT_SCATTER,
                point_size=15,
                # SCATTER 单独点
                color="yellow",
                label_opts=opts.LabelOpts(is_show=False,
                                          color='dark', font_size=13, position='center'),
            )
    add_point(df_zhz)
    return c

def all_flight(request): #接口调用
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")

    tab = Tab()
    tab.add(allflight(), "全国机场")
    tab.add(zhz_p(), "中航质项目")
    return HttpResponse(tab.render_embed())
# -----------------------------------返回网页部分
def datasPage(request):
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    """这是数据展示页面"""
    return render(request, "airpot_datas.html",locals())







def all_zhz_device(request):
    """中航质所有设备信息"""
    dic = {}
    if request.method == 'GET':
        sql = "select d_name,d_type from zhz_device GROUP BY d_name,d_type ORDER BY d_name;"
        df = models.get_status_withname(sql)
        columns = df.columns.tolist()
        df = df.to_dict(orient='index')
        print(df)
        return JsonResponse(df,columns=columns)
    else:
        dic['未知'] = 500
        dic['asdf'] = 800
        return JsonResponse(json.dumps(dic, ensure_ascii=False))



def tables_html(request):
    return render(request, "tables.html",)

def devicePage(request):
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    """中航质设备统计"""
    return render(request, "device.html",locals())

def personPage(request):
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    """行业内联系人，项目现场联系人等"""
    return render(request, "persons.html", locals())

def tradePage(request):
    if not request.session.get("is_login", None):
        return redirect("/demo/login/")
    return render(request, "project_device.html",locals() )