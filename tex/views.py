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
from tex.models import UserTexJob, DockerContainer

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
import docker

DockerClient = docker.Client(base_url='unix://var/run/docker.sock', timeout=10)


# Create your views here.
def index(request):
    if request.method == 'GET':
        print request.user
        if request.user.is_authenticated():
            containers = DockerClient.containers()
            Names =[]
            for i in containers:
                Names.append(i['Names'][0][1:])
            if str(request.user) not in Names:
                DockerClient.create_container(image="liuzheng712/texlive:2014", stdin_open=True, tty=True,
                                              volumes=['/data'],
                                              name=str(request.user))
                id = DockerClient.start(str(request.user),
                                   binds={'/data': {'bind': os.path.join(TEMPLATE, str(request.user)), 'rw': False}})
                DockerContainer(UserName=str(request.user),ContainerID=id['Id']).save()
            return render_to_response('index.html', {'user': request.user})
        else:
            return render_to_response('registration/login.html', {'user': request.user})
    elif request.method == 'POST':
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
    # 通过create_container方法创建容器，指定"yorko/webserver:v1"镜像名称，使用supervisord接管进程服务，挂载主宿机/data作为数据卷，容器监听80与22端口，容器的名称为webserver11
    post = simplejson.loads(request.body)
    csrfmiddlewaretoken = request.COOKIES.get('csrftoken', None)
    timestamp = str(int(time.mktime(time.localtime())))
    if post.get('texfile', False):
        ff = open(os.path.join(TEMPLATE, str(request.user), csrfmiddlewaretoken + '-' + timestamp + '.tex'), 'w')
        ff.write(post.get('texfile', None).encode('utf8'))
        ff.close()
        s = DockerClient.exec_create(DockerContainer.objects.filter(UserName=str(request.user)).first().ContainerID,
                                     'cd /data && latex ' + + csrfmiddlewaretoken + '-' + timestamp + '.tex',
                                     stdout=True, stderr=True, tty=True)
        d = DockerClient.exec_start(s['Id'])
        print d
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
