from django.db import models

# Create your models here.
class DockerContainer(models.Model):
    UserName = models.CharField(max_length=20)
    ContainerID = models.CharField(max_length=64)
    # PassWord = models.CharField()

class UserTexJob(models.Model):
    UserName = models.CharField(max_length=20)
    JobName =  models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)




