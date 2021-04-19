from django.conf.urls import url
from django.urls import path
from . import views,dataView,NewProjectView,PersonView,AirplanProjectView,AirPortsView,ZHZ_contractView,view_login_out_register

"""exam 的url"""

urlpatterns = [
    # 下边直接浏览页面
    url(r'^$', views.roots, name='a'),
    url(r'^choice$', views.choice, name='选择页面'),
    # 干系人页面
    url(r'^person$', PersonView.Person_Page, name='联系人表'),
    # 干系人json汇总（创建页面用）
    url(r'^allpersons$',PersonView.All_Persons_json,name="项目干系人json接口"),
    url(r'^personfind/(.+)/$',PersonView.Person_findone_json,name="干系人搜索"),

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

    # 机场项目信息
    url(r'^airports$',AirplanProjectView.AirPort_Page,name="机场项目页面"),
    url(r'^airportsJson$',AirplanProjectView.All_Airport_json,name="机场项目json接口"),
    url(r'^airportsfind/(.+)/$',AirplanProjectView.Airport_findone_json,name="机场项目搜索"),
    # url(r'^test/$',AirPortsView.get_zhz_map,name="机场项目搜索"),

    # 合同信息
    url(r'^contracts$',ZHZ_contractView.Contracts_page,name="合同页面"),
    url(r'^contractsJson$',ZHZ_contractView.All_Contract_json,name="机场项目json接口"),
    url(r'^contractsfind/(.+)/$',ZHZ_contractView.Contract_findone_json,name="合同项目搜索"),

    url(r'^login/$', view_login_out_register.login, name='登录页面'),
    url(r'^logout/$', view_login_out_register.logout, name='登出页面'),



    ## 拿页面


]