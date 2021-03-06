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
from django.conf.urls import url
from django.contrib import admin
from express_site import views

urlpatterns = [
    # url(r'', views.test, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^index/$', views.index, name='index'),
    url(r'^complete/$', views.complete, name='complete'),
    url(r'^parcel/$', views.parcel, name='parcel'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^search/$', views.search, name='search'),
    url(r'^settle/$', views.settle, name='settle'),
    url(r'^record/$', views.record, name='record'),
    url(r'^test/$', views.test, name='test'),
    url(r'^receive/$', views.receive, name='receive'),
    url(r'^receive_query/$', views.receive_query, name='receive_query'),
    url(r'^receive_query/(?P<action>(\w+))', views.receive_query),
    url(r'^$', views.login),

]

admin.site.site_header = u'快递资源管理系统'
admin.site.index_title = u'快递资源管理'
admin.site.site_title = u'快递资源管理系统'