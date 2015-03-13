#! /usr/bin/env python
# -*- coding:utf-8 -*- #
__author__ = 'liuzheng'
from django.conf.urls import patterns, include, url
from django.contrib import admin
import os

urlpatterns = patterns('tex.views',
                       # Examples:
                       # url(r'^$', 'webTeX.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       ('^$', 'index'),
)

urlpatterns += patterns('',
                        # Examples:
                        # url(r'^$', 'weibo.views.home', name='home'),
                        # url(r'^blog/', include('blog.urls')),
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^css/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': os.path.join(os.path.dirname(__file__), '../templates/css').replace('\\',
                                                                                                                  '/')}),
                        url(r'^js/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': os.path.join(os.path.dirname(__file__), '../templates/js').replace('\\',
                                                                                                                 '/')}),
                        url(r'^img/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': os.path.join(os.path.dirname(__file__), '../templates/img').replace('\\',
                                                                                                                  '/')}),
                        # (r'^api/', include('api.urls')),
)