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
    url(r'^newproject$',NewProjectView.New_project,name="新项目列表页面"),
    url(r'^newprojectjson$',NewProjectView.New_project_json,name="新项目列表json接口"),




    ## 拿页面


]