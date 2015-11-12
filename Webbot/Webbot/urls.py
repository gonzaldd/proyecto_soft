"""Webbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from WB_app.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get/id=(?P<id_solicitud>\w{0,90})/$', get_id, name='GET_byID'),
    url(r'^get/list/', get_list, name='GET_all'),
     url(r'^get/autor=(?P<nombre>.+?)/$', get_autor, name='GET_byautor'),
]
