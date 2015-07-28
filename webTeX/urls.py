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
                       ('^regis$', 'UserAddPage'),
                       ('^post/texfile$', 'MakeTexFile'),
                       ('^post/regis$', 'UserAdd'),
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += patterns('',
                        # Examples:
                        # url(r'^$', 'weibo.views.home', name='home'),
                        # url(r'^blog/', include('blog.urls')),
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^login$', 'django.contrib.auth.views.login'),
                        url(r'^logout$', 'django.contrib.auth.views.logout'),
                        # (r'^api/', include('api.urls')),
                        )
