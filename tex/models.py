from django.db import models

# Create your models here.
class weibo(models.Model):
    APP_KEY = models.CharField(max_length=15, primary_key=True)
    NAME = models.CharField(max_length=20)
    APP_SECRET = models.CharField(max_length=32)
    CALLBACK_URL = models.TextField(null=True, default=None)
    ACCESS_TOKEN = models.CharField(max_length=32, null=True, default=None)
    OPENID = models.CharField(max_length=32, null=True, default=None)
    OPENKEY = models.CharField(max_length=32, null=True, default=None)
    ALIVE = models.BooleanField(default=True)


class info(models.Model):
    HADOOP_MASTER = models.CharField(max_length=20, default='127.0.0.1')




