from django.contrib import admin
from exam.models import Document,GGJC_question,JTGC_question,Exam_end_line
# Register your models here.

@admin.register(Document)
class ControDocument(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('type','content')
    search_fields = ('type','content')  #可搜索字段
    list_editable = ('content',) #默认可编辑字段
    list_filter = ('type',)  # 过滤器

@admin.register(GGJC_question)
class GGJC(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('id','question_title','answer','where','page')
    search_fields = ('id','question_title','answer')  #可搜索字段
    list_editable = ('question_title','answer','where','page') #默认可编辑字段
    ordering = ('id',)

@admin.register(JTGC_question)
class JTGC(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('id','question_title','answer','where','page')
    search_fields = ('id','question_title','answer')  #可搜索字段
    list_editable = ('question_title','answer','where','page') #默认可编辑字段
    ordering = ('id',)


@admin.register(Exam_end_line)
class ExameNameAndDate(admin.ModelAdmin):
    '''设置显示字段,这是自己加的，如果不需要可以在下边register中删掉'''
    list_display = ('id','exam_name','exam_date','exam_location','exam_class')
    search_fields = ('exam_name','exam_date','exam_location','exam_class')  #可搜索字段
    list_editable = ('exam_name','exam_date','exam_location','exam_class') #默认可编辑字段
    # list_filter = ('',)  # 过滤器