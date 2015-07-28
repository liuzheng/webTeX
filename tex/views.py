#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013
# Gmail:liuzheng712
#
__author__ = 'liuzheng'
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import os
import sys
from django.views.decorators.csrf import csrf_exempt
from webTeX.settings import TEMPLATE
import simplejson
import time

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


# Create your views here.

def index(request):
    return render_to_response('index.html')


# @csrf_exempt
def MakeTexFile(request):
    post = simplejson.loads(request.body)
    csrfmiddlewaretoken = request.COOKIES.get('csrftoken', None)
    timestamp = str(int(time.mktime(time.localtime())))
    if post.get('texfile', False):
        ff = open(os.path.join(TEMPLATE, csrfmiddlewaretoken + '-' + timestamp+'.tex'), 'w')
        ff.write(post.get('texfile', None).encode('utf8'))
        ff.close()
        return HttpResponse('1')
    else:
        return HttpResponse('0')


if __name__ == '__main__':
    print 'tex.view'
