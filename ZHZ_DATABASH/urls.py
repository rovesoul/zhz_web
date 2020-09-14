from django.conf.urls import url
from django.urls import path
from . import views,dataView

"""exam 的url"""

urlpatterns = [
    # 下边直接浏览页面
    url(r'^$', views.roots, name='a'),
    url(r'^choice$', views.choice, name='选择页面'),
    url(r'^person$', dataView.person_info, name='联系人表'),



    ## 拿页面


]