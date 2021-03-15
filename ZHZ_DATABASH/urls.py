from django.conf.urls import url
from django.urls import path
from . import views,dataView,NewProjectView

"""exam 的url"""

urlpatterns = [
    # 下边直接浏览页面
    url(r'^$', views.roots, name='a'),
    url(r'^choice$', views.choice, name='选择页面'),
    url(r'^person$', dataView.person_info, name='联系人表'),
    url(r'^weakdevice$', dataView.airport_weak_device, name='弱电设备'),
    # 新项目管理统计页面
    url(r'^newproject$',NewProjectView.New_project,name="新项目汇总列表页面"),
    # 新建项目获取数据接口
    url(r'^newprojectjson$',NewProjectView.New_project_json,name="新项目列表json接口"),
    # 新建项目独立页面
    url(r'^newprojectone/(.+)/$',NewProjectView.New_project_oneself,name="NP项目对应独立主页"),
    # 新建项目
    url(r'^np_creat_NEWPROJECT$',NewProjectView.NP_create_NP_Page,name="新建项目页面"),
    url(r'^np_creat_NP_post$',NewProjectView.NP_create_NP_POST,name="新建项目post接口"),
    url(r'^newprojectfind/(.+)/$',NewProjectView.NP_NPS_json,name="NP项目搜索"),
    url(r'^airportfind/(.+)/$',NewProjectView.AirPortMessage_json,name="机场项目搜索"),

    # 新建项目过程记录json接口
    url(r'^np_notes_json/(.+)/$',NewProjectView.NP_NOTE_json,name="NP项目对应note接口"),
    url(r'^np_creat_person$',NewProjectView.NP_create_person,name="NP对应创建人员接口"),
    url(r'^np_creat_log$',NewProjectView.NP_create_log,name="NP对应创建log日志接口"),
    url(r'^np_all_new_notes_json$',NewProjectView.get_near_project_note,name="新日志列表"),




    ## 拿页面


]