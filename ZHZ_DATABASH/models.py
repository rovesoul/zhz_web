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
    name = models.CharField(unique=True,max_length=200,verbose_name='登录用户名')
    chinesename = models.CharField(unique=True,max_length=200,null=True,blank=True,verbose_name='中文名')
    password = models.CharField(max_length=200,verbose_name='密码')
    email = models.CharField(unique=True,max_length=200,null=True,blank=True,verbose_name='邮箱')
    phone = models.CharField(unique=True,max_length=25,null=True,blank=True,verbose_name='电话')
    sex = models.CharField(max_length=20,choices=gender,null=True,blank=True,verbose_name='性别')
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
        ('西南', "西南"),
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
    # 性别
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    # 项目经理业绩证明
    proofs = (
        ('有', "有"),
        ('无', "无"),
    )
    # 项目是否闭合
    project_close = (
        ('是', "是"),
        ('否', "否"),
        ('已作废', "已作废"),
    )
    # 中标通知书
    confirm_papers = (
        ('有', "有"),
        ('无', "无"),
    )


    name = models.CharField(unique=False, max_length=200,null=True,blank=True, verbose_name='合同名称')
    no = models.CharField(unique=True, max_length=200, verbose_name='合同编号')
    amount    = models.DecimalField(unique=False, max_digits=12,decimal_places=2,verbose_name='合同金额')
    add_money = models.DecimalField(unique=False, max_digits=12,decimal_places=2,null=True,blank=True)  #,verbose_name='补充协议金额'
    aready_get_income = models.DecimalField(unique=False,null=True,blank=True, max_digits=12,decimal_places=2,verbose_name='已收款金额')
    project_status = models.CharField(unique=False, max_length=200,  null=True, blank=True, verbose_name='项目当前状态')
    project_closed = models.CharField(max_length=10, choices=project_close,  null=True, blank=True, verbose_name='项目是否闭合')
    confirm_paper = models.CharField(max_length=100, choices=confirm_papers,null=True,blank=True,verbose_name='中标通知书')
    proof          = models.CharField(max_length=20, choices=proofs,         null=True, blank=True, verbose_name='项目经理业绩证明')
    signing_date = models.DateField(auto_now_add=False, null=True,verbose_name='签订日期')
    p_name = models.CharField(unique=False, max_length=200, verbose_name='对应机场名称')
    p_no = models.IntegerField(unique=False,verbose_name='对应机场编号')
    contract_content = models.TextField(max_length=2000, null=True,blank=True,verbose_name='合同范围内容')
    person_name = models.CharField(unique=False,null=True,blank=True, max_length=200, verbose_name='联系人姓名')
    person_phone = models.CharField(max_length=20,null=True,blank=True,verbose_name='联系人电话')
    manager_name = models.CharField(unique=False, null=True, blank=True, max_length=200, verbose_name='项目经理')
    sex = models.CharField(max_length=20, choices=gender,null=True,blank=True,verbose_name='联系人性别')
    person_title = models.CharField(max_length=100, null=True,blank=True,verbose_name='联系人职位信息')
    first_party = models.CharField(max_length=200, null=True,verbose_name='甲方单位')
    notes = models.TextField(max_length=200, null=True,blank=True,verbose_name='备注信息')
    c_time = models.DateField(auto_now_add=True,null=True,blank=True,verbose_name='登记时间')

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
    NewProjectID = models.CharField(unique=False, max_length=200, null=True,blank=True,verbose_name='新立项项目编号')
    name = models.CharField(unique=False, max_length=200, null=True,verbose_name='联系人姓名')
    phone = models.CharField(max_length=20, null=True,blank=True,verbose_name='电话')
    sex = models.CharField(max_length=20, choices=gender, null=True,blank=True,verbose_name='性别')
    title = models.CharField(max_length=100, null=True,blank=True,verbose_name='职位信息')
    area = models.CharField(max_length=200, null=True,blank=True,verbose_name='籍贯或活动省市')
    address = models.CharField(max_length=200, null=True,blank=True,verbose_name='邮寄地址')
    company = models.CharField(max_length=200, null=True,blank=True,verbose_name='公司名称')
    email = models.CharField(unique=False, max_length=200,null=True,blank=True, verbose_name='邮箱')
    idNO = models.CharField(unique=False, max_length=18,null=True,blank=True, verbose_name='身份证号')
    up_name = models.CharField(unique=False, max_length=20, null=True,blank=True,verbose_name='登记人')
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
    usefor = models.TextField(max_length=200, null=True,blank=True,verbose_name='测量目的')
    standard = models.TextField(max_length=200, null=True,blank=True,verbose_name='适应标准')
    manual = models.TextField(max_length=4000, null=True,blank=True,verbose_name='设备说明')
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
    contract_name = models.CharField(unique=False,null=True,blank=True, max_length=200, verbose_name='合同名称')
    contract_amount = models.DecimalField(unique=False, max_digits=12, decimal_places=2, null=True,blank=True,verbose_name='合同金额')
    contract_content = models.TextField(max_length=2000, null=True,blank=True,verbose_name='合同范围内容')
    person_name = models.CharField(unique=False, null=True,blank=True,max_length=200,  verbose_name='合同负责人名字')
    tenderr=models.CharField(unique=False, null=True,blank=True,max_length=200, verbose_name='招标人')
    contract_date = models.DateField(auto_now_add=False,null=True,blank=True,verbose_name='签订日期')
    location = models.CharField(unique=False,null=True,blank=True, max_length=200, verbose_name='公司地址')
    chairman = models.CharField(unique=False, null=True,blank=True, max_length=200,  verbose_name='法人/董事长/老大')
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
    id = models.AutoField(primary_key=True)
    p_name = models.CharField(unique=False, max_length=200, verbose_name='机场名称')
    sys_name = models.CharField(unique=False, choices=systems,max_length=30, verbose_name='系统名称')
    d_name = models.CharField(unique=False, max_length=200, verbose_name='设备名')
    d_type = models.CharField(unique=False, max_length=200,null=True,blank=True,verbose_name='设备型号')
    d_quantity = models.CharField(unique=False, max_length=18,null=True,blank=True, verbose_name='设备数量')
    madeCountryClass = models.CharField(unique=False, max_length=8,choices=madeCountry, null=True,blank=True, verbose_name='made by')
    madeCountry = models.CharField(unique=False, max_length=18,null=True,blank=True,verbose_name='制造国家名')
    set_date = models.DateField(auto_now_add=True,null=True,blank=True,verbose_name='大概安装年月')
    alarmDate = models.DateField(auto_now_add=True,null=True,blank=True, verbose_name='提醒年月')
    alarmLeft = models.DecimalField(unique=False, max_digits=2, decimal_places=1,null=True,blank=True,verbose_name='安装后计时年')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')

    def __str__(self):
        return self.__doc__ + ':' + self.d_name

    class Meta:
        ordering = ['p_name','sys_name','-c_time']
        verbose_name_plural = '各机场设备统计'


# luggage
class LuggageCompany(models.Model):
    """行李设备公司信息
    """
    systems = (
        ('行李', "行李"),
    )
    madeCountry=(
        ('中国', "中国"),
    )
    taxTypes = (
        ('小规模纳税人', "一般纳税人"),
    )
    company_name = models.CharField(unique=True, max_length=200, verbose_name='公司名称-必填')
    legal_person = models.CharField(unique=False, max_length=100,null=True,blank=True, verbose_name='法人-必填')
    registered_money = models.CharField(unique=False, max_length=200,null=True,blank=True, verbose_name='注册资本')
    establishDate = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name='成立日期')
    address = models.CharField(unique=False, max_length=255,null=True,blank=True, verbose_name='公司地址')
    phone   = models.CharField(unique=False, max_length=25, null=True, blank=True, verbose_name='联系电话')
    key_person = models.CharField(unique=False, null=True, blank=True, max_length=200, verbose_name='主要人员')
    social_credit_code = models.CharField(unique=True, null=True, blank=True, max_length=200, verbose_name='统一社会信用代码')
    taxName = models.CharField(unique=True, null=True, blank=True, max_length=200, verbose_name='纳税人名称')
    taxID = models.CharField(unique=True, null=True, blank=True, max_length=200, verbose_name='纳税人识别号')
    taxType = models.CharField(unique=True, choices=taxTypes,null=True, blank=True, max_length=60, verbose_name='纳税人类型')
    patents_name = models.CharField(unique=False,null=True, blank=True, max_length=200, verbose_name='专利名称')
    certificates = models.CharField(unique=False,null=True, blank=True, max_length=200, verbose_name='资质证书')
    business_scope = models.TextField(max_length=2500, null=True,blank=True,verbose_name='经营范围')
    product_intro = models.TextField(max_length=2500, null=True,blank=True,verbose_name='产品介绍')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')

    def __str__(self):
        return self.__doc__ + ':' + self.company_name

    class Meta:
        ordering = ['-c_time','company_name']
        verbose_name_plural = '行李设备厂家'

# big thing end date
class Thing_end_line(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    thing_name = models.CharField(max_length=225, verbose_name='事件名称')
    thing_date = models.DateField(auto_now_add=False, verbose_name='截至发生日期', null=True, blank=True)
    thing_location = models.CharField(max_length=20, null=True, blank=True, verbose_name='事件地点')
    thing_class = models.CharField(max_length=20, null=True, blank=True, verbose_name='事件分类')

    def __str__(self):
        return self.__doc__ + ':' + self.thing_name

    class Meta:
        ordering = ['thing_date']
        verbose_name_plural = '事件及时间设定'


# websit
class FriendWebsit(models.Model):
    """友情链接
    """
    web_types = (
        ('公司用', "公司用"),
        ('自己用', "自己用"),
        ('娱乐用', "娱乐用"),
    )
    id = models.AutoField(primary_key=True)
    websit_name = models.CharField(unique=True, max_length=150, verbose_name='网站名称')
    websit_link = models.CharField(unique=True, max_length=200,null=True,blank=True, verbose_name='网址')
    webType = models.CharField(unique=False, choices=web_types, null=True, blank=True, max_length=60,verbose_name='网站性质')
    webDoc = models.CharField(unique=False, max_length=255, null=True, blank=True, verbose_name='介绍')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    def __str__(self):
        return self.__doc__ + ':' + self.websit_name

    class Meta:
        ordering = ['-c_time','websit_name']
        verbose_name_plural = '友情链接'



# websit
class NewCompanyProject(models.Model):
    """
    新项目记录管理功能
    """
    project_types = (
        ('检测类', "检测类"),
        ('外包类', "外包类"),
        ('配合类', "配合类"),
        ('其他类', "其他类"),
    )
    project_status = (
        ('进行中', "进行中"),
        ('已签约', "已签约"),
        ('已作废', "已作废"),
        ('已配合完毕', "已配合完毕"),
    )

    id = models.AutoField(primary_key=True)
    NewProjectID = models.CharField(unique=True, max_length=200, verbose_name='新立项项目编号')
    NewProject_name = models.CharField(unique=True, max_length=150, verbose_name='新立项项目名称')
    Contracts_no = models.CharField(unique=False, max_length=200, null=True, blank=True, verbose_name='签约的合同编号')
    NewProject_type = models.CharField(unique=False, choices=project_types, null=True, blank=True, max_length=60,verbose_name='项目性质')
    NewProject_status = models.CharField(unique=False, choices=project_status, null=True, blank=True, max_length=60,verbose_name='项目状态')
    money_price_control = models.DecimalField(unique=False, max_digits=10,decimal_places=2,null=True, blank=True, max_length=60,verbose_name='招标控制价')
    monney_buy_biddingDoc = models.DecimalField(unique=False, max_digits=9,decimal_places=2,null=True, blank=True, max_length=60,verbose_name='招标文件费用')
    money_Bid_security_fee = models.DecimalField(unique=False, max_digits=9,decimal_places=2,null=True, blank=True, max_length=60,verbose_name='投标保证金')
    money_use_room_fee = models.DecimalField(unique=False, max_digits=7,decimal_places=2,null=True, blank=True, max_length=60,verbose_name='开标室费用')
    money_agency_service_fee = models.DecimalField(unique=False, max_digits=7,decimal_places=2,null=True, blank=True, max_length=60,verbose_name='招标代理服务费')
    money_transaction_service_fee = models.DecimalField(unique=False, max_digits=7,decimal_places=2,null=True, blank=True, max_length=60,verbose_name='交易服务费')
    money_Performance_bond = models.DecimalField(unique=False, max_digits=9,decimal_places=2,null=True, blank=True, max_length=60,verbose_name='履约保证金')
    NewProjectDoc = models.TextField(unique=False,max_length=2000, null=True,blank=True,verbose_name='此项目背景介绍')
    # 这俩固定的，机场库的
    p_name = models.CharField(unique=False, max_length=200, blank=True, null=True, verbose_name='机场项目名称')
    p_no = models.IntegerField(unique=False,blank=True, null=True, verbose_name='机场项目编号')

    c_time = models.DateTimeField(auto_now_add=True, verbose_name='项目创建时间')
    def __str__(self):
        return self.__doc__ + ':' + self.NewProject_name

    class Meta:
        ordering = ['-c_time','NewProject_name']
        verbose_name_plural = '新立项项目'


class NP_Note(models.Model):
    """
    每个项目的Tag\note功能
    """
    id = models.AutoField(primary_key=True)
    NewProjectID = models.CharField(unique=False, max_length=200, verbose_name='新立项项目编号')
    NewProject_name = models.CharField(unique=False,null=True,blank=True, max_length=150, verbose_name='新立项项目名称')
    note_one = models.TextField(max_length=5000, null=True,blank=True,verbose_name='事项记录')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='项目创建时间')
    def __str__(self):
        return self.__doc__ + ':' + self.NewProject_name

    class Meta:
        ordering = ['-c_time','NewProjectID']
        verbose_name_plural = '新立项项目NP事情记录'