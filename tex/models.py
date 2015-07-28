from django.db import models

# Create your models here.
class user(models.Model):
    UserName = models.CharField(max_length=20)
    # PassWord = models.CharField()


class info(models.Model):
    HADOOP_MASTER = models.CharField(max_length=20, default='127.0.0.1')




