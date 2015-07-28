#! /usr/bin/env python
# -*- coding:utf-8 -*- #
__author__ = 'liuzheng'
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = patterns('tex.views',
                       # Examples:
                       # url(r'^$', 'webTeX.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       ('^$', 'index'),
                       ('^post/texfile$', 'MakeTexFile'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('',
                        # Examples:
                        # url(r'^$', 'weibo.views.home', name='home'),
                        # url(r'^blog/', include('blog.urls')),
                        url(r'^admin/', include(admin.site.urls)),
                        # (r'^api/', include('api.urls')),
)