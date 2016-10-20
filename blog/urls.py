# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:53:55 2016

@author: albrightke
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]