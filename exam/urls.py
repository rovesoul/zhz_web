from django.conf.urls import url
from django.urls import path
from . import views

"""exam 的url"""

urlpatterns = [

    # 下边直接浏览页面
    url(r'^$', views.choice_page, name='考试选择页面'),
    url(r'^gjdg/$', views.gjdg, name='公共基础大纲'),
    url(r'^jtml/$', views.jtml, name='交通工程目录'),
    url(r'^gjzsdjj/$', views.gjzsdjj, name='公共基础知识点精简'),
    url(r'^ggjc/$', views.ggjc, name='公共基础正序页面'),
    url(r'^ggjc/random/$', views.ggjc_random, name='公共基础乱序页面'),
    url(r'^jtgc/$', views.jtgc, name='交通工程正序页面'),
    url(r'^jtgc/random/$', views.jtgc_random, name='交通工程乱序页面'),
    url(r'^ggjc_api/$', views.get_ggjc_question, name='按id拿题页面'),
    url(r'^jtgc_api/$', views.get_jtgc_question, name='按id拿题页面'),
    url(r'^doc_api/$', views.get_document, name='doc 的 api'),
    url(r'^deadline/$', views.DeadLinePage, name='倒计时页面'),





    ## 拿页面


]
