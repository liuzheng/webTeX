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
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib import auth

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


# Create your views here.
def index(request):
    if request.method=='GET':
        if request.user.is_authenticated():
            return render_to_response('index.html')
        else:
            return render_to_response('registration/login.html')
    elif request.method=='POST':
        post = simplejson.loads(request.body)
        username = post.get('username', '')
        password = post.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponse('1')
        else:
            return HttpResponse('0')

# @csrf_exempt
def MakeTexFile(request):
    post = simplejson.loads(request.body)
    csrfmiddlewaretoken = request.COOKIES.get('csrftoken', None)
    timestamp = str(int(time.mktime(time.localtime())))
    if post.get('texfile', False):
        ff = open(os.path.join(TEMPLATE, csrfmiddlewaretoken + '-' + timestamp + '.tex'), 'w')
        ff.write(post.get('texfile', None).encode('utf8'))
        ff.close()
        return HttpResponse('1')
    else:
        return HttpResponse('0')


def UserAddPage(request):
    return render_to_response('registration.html')


def UserAdd(request):
    post = simplejson.loads(request.body)
    UserName = post.get('username', None)
    PassWord = post.get('pwd', None)
    Email = post.get('email', None)
    if UserName and PassWord and Email:
        user = User.objects.create_user(UserName, PassWord, Email)
        # print user.is_staff #True
        user.save()
        return HttpResponse('1')
    else:
        return HttpResponse('0')


if __name__ == '__main__':
    print 'tex.view'
