"""质量管理web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from . import views


urlpatterns = [
    url(r'admin/', admin.site.urls),
    path('', views.roots),  # 跟目录
    url(r'^demo/', include('demo.urls')),  # <--- demo指app
    url(r'^kaoshi/', include('exam.urls')),  # <--- demo指app
    url(r'^ZHZ/', include('ZHZ_DATABASH.urls')),  # <--- ZHZ_DATABASH指app
    url(r'^404/', views.page_not_found),  # <--- ZHZ_DATABASH指app
    path('captcha/', include('captcha.urls'))  # 增加这一行
]


handler404 = views.page_not_found
handler403 = views.permission_denied
handler500 = views.page_error