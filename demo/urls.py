from django.conf.urls import url
from django.urls import path
from . import views, sql_views, view_login_out_register

"""demo 的url"""

urlpatterns = [
    url(r'^bar_cs/$', views.cs_api, name='demo'),  # 通过它返回一个建设情况的json文件
    url(r'^bar_region/$', views.region_api, name='demo'),  # 通过它返回一个建设情况的json文件
    url(r'^bar_province/$', views.province_api, name='demo'),  # 通过它返回一个建设情况的json文件
    url(r'^geo_api/$', views.guo_report, name='demo'),  # 通过它返回一个建设情况的json文件
    url(r'af/$', views.all_flight),
    # url(r'^datas/$', views.IndexView.as_view(), name='demo'),# 通过它返回一个html文件
    url(r'^dataspage/$', views.datasPage, name='demo'),  # 通过它返回一个html文件
    url(r'^device/$', views.devicePage, name='device'),  # 通过它返回一个html文件
    url(r'^person/$', views.personPage, name='person'),  # 通过它返回一个html文件
    url(r'^trade/$', views.tradePage, name='trade contract and device'),  # 通过它返回一个html文件

    url(r'^contract/$', sql_views.all_contract, name='contract'),  # 通过它返回一个api文件
    url(r'^tables/$', views.tables_html, name='contract'),  # 通过它返回一个html文件

    # 来自sqlview
    # get的
    url(r'^zhz_device/$', sql_views.all_zhz_device, name='zhz_device'),  # 通过它返回一个html文件
    url(r'^device_get/$', sql_views.device_sql_change, name='device变化查询'),  # 通过它返回一个html文件
    url(r'^person_get/$', sql_views.person_sql_change, name='person变化查询'),  # 通过它返回一个html文件
    url(r'^all_person/$', sql_views.all_person, name='all_person'),  # 通过它返回一个html文件

    # add的
    url(r'^add_device/$', sql_views.add_device_sql, name='add_device'),  # 通过它返回一个html文件
    url(r'^add_contract/$', sql_views.add_contract_sql, name='add_contract'),  # 通过它返回一个html文件
    url(r'^add_person/$', sql_views.add_person_sql, name='add_person'),  # 通过它返回一个html文件

    url(r'^device_amb_get/$', sql_views.device_sql_amb, name='device模糊查询'),  # 通过它返回一个html文件
    url(r'^person_amb_get/$', sql_views.person_sql_amb, name='人模糊查询'),  # 通过它返回一个html文件
    url(r'^contract_amb_get/$', sql_views.contract_sql_amb, name='合同模糊查询'),  # 通过它返回一个html文件
    url(r'^p_no_amb_get/$', sql_views.get_p_no_sql_amb, name='项目编号查询'),  # 通过它返回一个html文件

    url(r'^databash_api/$', sql_views.count_together, name='databash数据汇总'),  # 通过它返回一个html文件

    url(r'^$', views.home, name='主页'),
    url(r'^login/$', view_login_out_register.login, name='登录页面'),
    url(r'^logout/$', view_login_out_register.logout, name='登出页面'),

]
