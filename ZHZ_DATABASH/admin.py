from django.contrib import admin
from ZHZ_DATABASH.models import User,Project_Detail,ProjectDevice,Contracts,TradeContracts,Device,Person
# Register your models here.
@admin.register(User)
class USER(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('id','name','password','email','sex','c_time','phone')
    search_fields = ('id','name','password','email','sex','c_time','phone')  #可搜索字段
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
    list_display = ('name','no','amount','signing_date','p_name','p_no','first_party','c_time',)
    search_fields = ('name','no','amount','signing_date','p_name','p_no','first_party','c_time',)  #可搜索字段
    list_editable = ('first_party',) #默认可编辑字段
    ordering = ('no','signing_date')
    list_filter = ('p_name', 'first_party',)  # 过滤器
    date_hierarchy = 'signing_date'

@admin.register(Person)
class Person(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('id','name','phone','sex','title','company','ups_time','p_name','p_no')
    search_fields = ('name','phone','sex','title','company','ups_time','p_name','p_no')  #可搜索字段
    list_editable = ('phone','sex','title','company','p_name','p_no') #默认可编辑字段
    ordering = ('-ups_time','name',)
    list_filter = ('title', 'company','p_name','sex')  # 过滤器
    date_hierarchy = 'ups_time'


# 以下未编辑
admin.site.register(ProjectDevice)
admin.site.register(TradeContracts)

