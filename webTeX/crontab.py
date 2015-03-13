#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2014
# Gmail:liuzheng712
#
__author__ = 'liuzheng'
import os
import sys
from django.db import connection

cursor = connection.cursor()
# HADOOP_MASTER = cursor.execute('select HADOOP_MASTER from api_info').fetchall()
# HADOOP_MASTER = '127.0.0.1'

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
import json
import time

try:
    import cPickle as pkl
except:
    import pickle as pkl


def something():
    print('do something')


if __name__ == '__main__':
    something()