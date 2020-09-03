import json
# Create your models here.
import mysql.connector
import  pandas as pd
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
from pyecharts import options as opts
from django.db import models

class User(models.Model):
    '''demo民航系统用户'''
    gender = (
        ('male', "男"),
        ('female',"女"),
    )
    name = models.CharField(unique=True,max_length=200,verbose_name='用户名')
    password = models.CharField(max_length=200,verbose_name='密码')
    email = models.CharField(unique=True,max_length=200,verbose_name='邮箱')
    sex = models.CharField(max_length=20,choices=gender,verbose_name='性别')
    c_time = models.DateTimeField(auto_now_add=True,verbose_name='注册时间')
    def __str__(self):
        return self.__doc__+':'+self.name
    class Meta:
        ordering=['-c_time']
        verbose_name_plural='用户名'


config = {
    "host" :'49.233.23.230',
    "port" :'3306',
    "user" :'root',
    "password" :'WvT0FAwOvQ',
    "database" :'zhz_database'
}


def get_status(sqlword):
    """从mysql取数程序,返回dataframe"""
    con = mysql.connector.connect(**config)
    try:
        cursor = con.cursor()
        # 按结果降序排列取建设状态名称和数量统计
        sql = sqlword
        cursor.execute(sql)
        data = cursor.fetchall()
        frame = pd.DataFrame(list(data))
        print(frame.head())
        return frame


    except Exception as e:
        con.rollback()
        print(e)
        return None

    finally:
        """关闭连接"""
        if "con" in dir():
            con.close()

def get_status_withname(sqlword):
    """从mysql取数程序,带列名的dataframe"""
    con = mysql.connector.connect(**config)
    try:
        cursor = con.cursor()
        # 按结果降序排列取建设状态名称和数量统计
        sql = sqlword
        cursor.execute(sql)
        data = cursor.fetchall()
        cols = cursor.description  # 类似 desc table_name返回结果
        col = []  # 创建一个空列表以存放列名
        for v in cols:
             col.append(v[0])  # 循环提取列名，并添加到col空列表
        frame = pd.DataFrame(data, columns=col)  # 将查询结果转换成DF结构，并给列重新赋值

        return frame


    except Exception as e:
        con.rollback()
        print(e)
        return None

    finally:
        """关闭连接"""
        if "con" in dir():
            con.close()

def catch_geo(request):
    df_zaijian = get_status_withname('select * from project_detail where construction_situation ="在建" ;')
    df_new = get_status_withname('select * from project_detail where construction_situation ="新增" ;')
    df_jiyou = get_status_withname('select * from project_detail where construction_situation ="既有" ;')
    df_plan = get_status_withname('select * from project_detail where construction_situation ="研究布局" ;')
    c = (Geo().add_schema(maptype="china"))
    def add_points(df_data):
        points_list = df_data.values.tolist()
        print("pointlist:",points_list)
        for num in points_list:
            print("num:",num)
            c.add_coordinate(num[0], (num[2]), num[3])

            # print('加值')
            c.add(
                num[7],
                [(num[0], f'<br>航站楼面积:{num[8]}㎡<br>跑道长度:{num[12]}<br>跑道等级:{num[13]}<br>启用时间:{str(num[9])[0:10]}')],
                print("封装:",[(num[0], f'<br>航站楼面积:{num[8]}<br>跑道长度:{num[12]}<br>跑道等级:{num[13]}<br>启用时间:{num[9]}')]),
                # type_=ChartType.SCATTER,
                point_size=5,
                label_opts=opts.LabelOpts(is_show=False, ),
                is_selected=True,
                symbol_size=9,
            )
    add_points(df_jiyou,)
    add_points(df_new, )
    add_points(df_zaijian, )
    add_points(df_plan, )
    c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    c.dump_options_with_quotes()
    print(json.loads(c))

def insert_status(sqlword):
    """插入函数"""
    con = mysql.connector.connect(**config)
    try:
        cursor = con.cursor()
        # 按结果降序排列取建设状态名称和数量统计
        # sql = 'INSERT INTO zhz_device (d_name,d_type,quantity,append,usefor,standard,ups_date ) VALUES ( "asdf","asdf","4","asdf","asdf","asdf","2020-8-13");'
        cursor.execute(sqlword)
        d = cursor.rowcount
        con.commit()
        # 返回的d仅为状态
        return d




    except Exception as e:
        con.rollback()
        print(e)
        return None

    finally:
        """关闭连接"""
        if "con" in dir():
            con.close()