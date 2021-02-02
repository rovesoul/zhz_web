from django.contrib import admin
from ZHZ_DATABASH.models import User,Project_Detail,ProjectDevice,Contracts,TradeContracts,Device,Person,LuggageCompany, FriendWebsit, Thing_end_line
# Register your models here.
@admin.register(User)
class USER(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('chinesename','name','password','email','sex','c_time','phone')
    search_fields = ('chinesename','name','password','email','sex','c_time','phone')  #可搜索字段
    list_editable = ('name','password','phone','email','sex') #默认可编辑字段
    ordering = ('name',)

@admin.register(Project_Detail)
class PROJECT_DETAIL(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('p_name','p_no','longitude','latitude','provence','region','use_cate','construction_situation','run_length','run_class','terminal_area','throughput','aircraft_sorties')
    search_fields = ('p_name','p_no','provence','region','use_cate','construction_situation')  #可搜索字段
    list_editable = ('provence','region','use_cate','construction_situation','terminal_area','throughput','aircraft_sorties') #默认可编辑字段
    ordering = ('region','p_no',)
    list_filter = ('region','provence','use_cate','construction_situation')  # 过滤器
    date_hierarchy='active_time'

@admin.register(Device)
class DEVICE(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('d_name','d_type','quantity','append','usefor','standard','manual','ups_time',)
    search_fields = ('d_name','d_type','quantity','append','usefor','standard','manual','ups_time')  #可搜索字段
    list_editable = ('d_type','quantity','append','usefor','standard','manual',) #默认可编辑字段
    ordering = ('d_name','-ups_time')
    list_filter = ('d_name', 'quantity','standard')  # 过滤器
    date_hierarchy = 'ups_time'

@admin.register(Contracts)
class ZHZContracts(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('name','no','amount','add_money','aready_get_income','project_status','signing_date','p_name','p_no','manager_name','proof','project_status','project_closed','contract_content','first_party','c_time',)
    search_fields = ('name','no','amount','signing_date','p_name','p_no','project_status','manager_name','proof','project_status','project_closed','contract_content','first_party','c_time',)  #可搜索字段
    list_editable = ('first_party','aready_get_income','project_status','project_closed','manager_name','proof','project_closed',) #默认可编辑字段
    ordering = ('no','signing_date')
    list_filter = ('p_name','first_party','manager_name','project_status','project_closed','proof',)  # 过滤器
    date_hierarchy = 'signing_date'

@admin.register(Person)
class Person(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('name','phone','sex','title','company','ups_time','p_name','p_no')
    search_fields = ('name','phone','sex','title','company','ups_time','p_name','p_no')  #可搜索字段
    list_editable = ('phone','sex','title','company','p_name','p_no') #默认可编辑字段
    ordering = ('-ups_time','name',)
    list_filter = ('p_name', 'company','title','sex')  # 过滤器
    date_hierarchy = 'ups_time'

@admin.register(LuggageCompany)
class Luggage(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('company_name','legal_person','registered_money','address','phone','key_person','certificates','establishDate')
    search_fields = ('company_name','legal_person','address','phone','key_person','certificates','establishDate',)  #可搜索字段
    list_editable = ('phone','key_person') #默认可编辑字段
    ordering = ('-c_time','company_name',)
    list_filter = ('company_name','address','key_person','certificates','establishDate')  # 过滤器
    date_hierarchy = 'c_time'

@admin.register(FriendWebsit)
class FriendWebs(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('websit_name','websit_link','webType','c_time','webDoc')
    search_fields = ('websit_name','websit_link','webType','c_time','webDoc',)  #可搜索字段
    # list_editable = ('phone','key_person') #默认可编辑字段
    ordering = ('-c_time','websit_name',)
    list_filter = ('websit_name','webType')  # 过滤器
    date_hierarchy = 'c_time'


@admin.register(Thing_end_line)
class ThingNameAndDate(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('id','thing_name','thing_date','thing_location','thing_class')
    search_fields = ('exam_name','exam_date','exam_location','exam_class')  #可搜索字段
    list_editable = ('thing_name','thing_date','thing_location','thing_class') #默认可编辑字段
    list_filter = ('thing_class','thing_location')  # 过滤器
    date_hierarchy = 'thing_date'

# 以下未编辑
admin.site.register(ProjectDevice)
admin.site.register(TradeContracts)



# 下边这三行直接删了也没事，只是修改标题而已
admin.site.site_header='ZHZ数据管理系统'
admin.site.site_title='ZHZ系统'
admin.site.index_title='商务管理'
