from django.contrib import admin

# Register your models here.
from . import  models
from demo.models import User


# 注册可以有两种方式，下边这个语法糖的或者下边那行注释掉的
@admin.register(User)
class ControUser(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('name','password','email','sex','c_time')
    search_fields = ('name','password')  #可搜索字段
    list_editable = ['password','email','sex'] #默认可编辑字段
# admin.site.register(models.User,ControUser)


# 下边这三行直接删了也没事，只是修改标题而已
admin.site.site_header='ZHZ数据库项目管理系统'
admin.site.site_title='登录系统后台'
admin.site.index_title='后台管理'