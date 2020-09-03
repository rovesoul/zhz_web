import json
# Create your models here.
import mysql.connector
import  pandas as pd
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
from pyecharts import options as opts
from django.db import models

class User(models.Model):
    '''ZHZdatabash民航系统用户'''
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

class Project_Detail(models.Model):
    """机场信息"""
    usetype = (
        ('民用', "民用"),
        ('军用', "军用"),
        ('军民合用', "军民合用"),
    )
    construction_situation = (
        ('既有', "既有"),
        ('新增', "新增"),
        ('研究布局', "研究布局"),
        ('在建', "在建"),
    )
    regions=(
        ('华北', "华北"),
        ('华东', "华东"),
        ('东北', "东北"),
        ('华南', "华南"),
        ('西北', "西北"),
        ('新疆', "新疆"),
    )
    p_name = models.CharField(unique=True, max_length=200, verbose_name='机场名称')
    p_no = models.IntegerField(unique=True,  verbose_name='机场编号')
    longitude = models.DecimalField(unique=False, max_digits=9,decimal_places=6, verbose_name='经度')
    latitude  = models.DecimalField(unique=False, max_digits=9,decimal_places=6, verbose_name='纬度')
    provence  = models.CharField(unique=False, max_length=200, verbose_name='所在省份')
    region    = models.CharField(unique=False, max_length=100,choices=regions, verbose_name='所属管理区')
    use_cate  = models.CharField(max_length=20, choices=usetype, verbose_name='使用性质')
    construction_situation = models.CharField(max_length=12, choices=construction_situation, verbose_name='建设情况')
    run_length = models.CharField(max_length=200, verbose_name='跑道长度')
    run_class  = models.CharField(max_length=200, verbose_name='跑道等级')
    terminal_area = models.DecimalField(unique=False, max_digits=12,decimal_places=2, verbose_name='航站楼面积')
    active_time = models.DateField(auto_now_add=False, verbose_name='启用时间')
    throughput = models.CharField(max_length=255, verbose_name='吞吐量')
    aircraft_sorties = models.CharField(max_length=255, verbose_name='架次/日')

    def __str__(self):
        return self.__doc__ + ':' + self.p_name

    class Meta:
        ordering = ['p_name']
        verbose_name_plural = '全国机场项目详情'


class Contracts(models.Model):
    """contracts合同信息"""
    usetype = (
        ('民用', "民用"),
        ('军用', "军用"),
        ('军民合用', "军民合用"),
    )
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(unique=True, max_length=200, verbose_name='合同名称')
    no = models.CharField(unique=True, max_length=200, verbose_name='合同编号')
    amount = models.DecimalField(unique=False, max_digits=12,decimal_places=2,verbose_name='合同金额')
    signing_date = models.DateField(auto_now_add=False, null=True,verbose_name='签订日期')
    p_name = models.CharField(unique=False, max_length=200, verbose_name='对应机场名称')
    p_no = models.IntegerField(unique=False,verbose_name='对应机场编号')
    person_name = models.CharField(unique=False,null=True, max_length=200, default="-",verbose_name='联系人姓名')
    person_phone = models.CharField(max_length=20,null=True,default="-", verbose_name='联系人电话')
    sex = models.CharField(max_length=20, choices=gender, null=True,verbose_name='联系人性别')
    person_title = models.CharField(max_length=100, null=True,verbose_name='联系人职位信息')
    first_party = models.CharField(max_length=200, null=True,verbose_name='甲方单位')
    notes = models.TextField(max_length=200, null=True,verbose_name='备注信息')
    c_time = models.DateField(auto_now_add=True, null=True,verbose_name='登记时间')

    def __str__(self):
        return self.__doc__ + ':' + self.p_name

    class Meta:
        ordering = ['signing_date']
        verbose_name_plural = 'ZHZ合同详情'


class Person(models.Model):
    """行业联系人"""
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    p_name = models.CharField(unique=False, max_length=200,null=True, verbose_name='项目名称')
    p_no = models.IntegerField(unique=False, null=True, verbose_name='项目编号')
    name = models.CharField(unique=False, max_length=200, null=True,verbose_name='联系人姓名')
    phone = models.CharField(max_length=20, null=True,verbose_name='电话')
    sex = models.CharField(max_length=20, choices=gender, null=True,verbose_name='性别')
    title = models.CharField(max_length=100, null=True,verbose_name='职位信息')
    area = models.CharField(max_length=200, null=True,verbose_name='籍贯或活动省市')
    company = models.CharField(max_length=200, null=True,verbose_name='公司名称')
    email = models.CharField(unique=False, max_length=200,null=True, verbose_name='邮箱')
    idNO = models.CharField(unique=False, max_length=18,null=True, verbose_name='身份证号')
    up_name = models.CharField(unique=False, max_length=20, null=True,verbose_name='登记人')
    ups_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')

    def __str__(self):
        return self.__doc__ + ':' + self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = '行业联系人'

class Device(models.Model):
    """公司设备信息"""
    d_name = models.CharField(unique=False, max_length=200, verbose_name='设备')
    d_type = models.CharField(unique=False, max_length=200, null=True,verbose_name='设备型号')
    quantity = models.CharField(unique=False, max_length=18, null=True,verbose_name='设备数量')
    append = models.CharField(unique=False, max_length=255, null=True,verbose_name='设备附件')
    usefor = models.TextField(max_length=200, null=True,verbose_name='测量目的')
    standard = models.TextField(max_length=200, null=True,verbose_name='适应标准')
    manual = models.TextField(max_length=4000, null=True,verbose_name='设备说明')
    ups_time = models.DateField( null=True,verbose_name='注册时间')

    def __str__(self):
        return self.__doc__ + ':' + self.d_name

    class Meta:
        ordering = ['d_name','d_type']
        verbose_name_plural = '中航质设备'

class TradeContracts(models.Model):
    """行业contracts合同信息"""

    p_name = models.CharField(unique=True, max_length=200, verbose_name='机场项目名称')
    company_name = models.CharField(unique=False, max_length=200, verbose_name='公司名称')
    contract_name = models.CharField(unique=False,null=True, max_length=200, verbose_name='合同名称')
    contract_amount = models.DecimalField(unique=False, max_digits=12, decimal_places=2, null=True,verbose_name='合同金额')
    contract_content = models.TextField(max_length=800, null=True,verbose_name='合同范围内容')
    person_name = models.CharField(unique=False, null=True,max_length=200,  verbose_name='合同负责人名字')
    tenderr=models.CharField(unique=False, max_length=200, verbose_name='招标人')
    contract_date = models.DateField(auto_now_add=False, null=True,verbose_name='签订日期')
    location = models.CharField(unique=False, null=True, max_length=200, verbose_name='公司地址')
    chairman = models.CharField(unique=False, null=True, max_length=200,  verbose_name='法人/董事长/老大')
    c_time = models.DateField(null=True,default='2020-08-01',verbose_name='记录时间')

    def __str__(self):
        return self.__doc__ + ':' + self.p_name

    class Meta:
        ordering = ['p_name','contract_date']
        verbose_name_plural = '各机场施工单位信息'

class ProjectDevice(models.Model):
    """各机场设备信息"""
    systems = (
        ('航显', "航显"),
        ('布线', "布线"),
        ('安防', "安防"),
        ('广播', "广播"),
    )
    madeCountry=(
        ('中国', "中国"),
        ('外国', "外国"),
        ('未知', "未知"),
    )
    p_name = models.CharField(unique=False, max_length=200, verbose_name='机场名称')
    sys_name = models.CharField(unique=False, choices=systems,max_length=30, verbose_name='系统名称')
    d_name = models.CharField(unique=False, max_length=200, verbose_name='设备名')
    d_type = models.CharField(unique=False, max_length=200,null=True,verbose_name='设备型号')
    d_quantity = models.CharField(unique=False, max_length=18,null=True, verbose_name='设备数量')
    madeCountryClass = models.CharField(unique=False, max_length=8,choices=madeCountry, null=True, verbose_name='made by')
    madeCountry = models.CharField(unique=False, max_length=18,null=True,verbose_name='制造国家名')
    set_date = models.DateField(auto_now_add=True,null=True,verbose_name='大概安装年月')
    alarmDate = models.DateField(auto_now_add=True,null=True, verbose_name='提醒年月')
    alarmLeft = models.DecimalField(unique=False, max_digits=2, decimal_places=1,null=True,verbose_name='安装后计时年')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')

    def __str__(self):
        return self.__doc__ + ':' + self.d_name

    class Meta:
        ordering = ['p_name','sys_name','-c_time']
        verbose_name_plural = '各机场设备统计'