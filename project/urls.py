"""cereal URL Configuration

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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cereal_list/$', 'main.views.cereal_list'),
    url(r'^cereal_detail/(?P<pk>\d+)/$', 'main.views.cereal_detail'),
    url(r'^cereal_create/$', 'main.views.cereal_create'),
    url(r'^cereal_edit(?P<pk>\d+)/$', 'main.views.cereal_edit'),
    url(r'^manufacturer_create/$', 'main.views.manufacturer_create'),
    url(r'^manufacturer_detail/(?P<pk>\d+)/$', 'main.views.manufacturer_detail'),
    url(r'^manufacturer_edit/(?P<pk>\d+)/$', 'main.views.manufacturer_edit'),
    url(r'^contact_view/$', 'main.views.contact_view'),
]
