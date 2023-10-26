#coding=utf-8
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
from django.contrib import admin
from express_site import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    # url(r'', views.test, name='index'),
    path(r'^admin/', admin.site.urls),
    # path(r'^login/$', views.login, name='login'),
    path('login', views.login, name='login'),
    path(r'^logout/$', views.logout, name='logout'),
    path(r'^register/$', views.register, name='register'),
    # path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path(r'^complete/$', views.complete, name='complete'),
    path(r'^parcel/$', views.parcel, name='parcel'),
    path(r'^upload/$', views.upload, name='upload'),
    path(r'^search/$', views.search, name='search'),
    path(r'^settle/$', views.settle, name='settle'),
    path(r'^record/$', views.record, name='record'),
    path(r'^test/$', views.test, name='test'),
    path(r'^receive/$', views.receive, name='receive'),
    path(r'^receive_query/$', views.receive_query, name='receive_query'),
    path(r'^receive_query/(?P<action>(\w+))', views.receive_query),
    path('', views.login),

]

admin.site.site_header = u'快递资源管理系统'
admin.site.index_title = u'快递资源管理'
admin.site.site_title = u'快递资源管理系统'