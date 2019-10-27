from django.db import models
from django.conf import settings
# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    title = models.TextField(max_length=100)
    body = models.TextField()

class BlogPic(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete = models.CASCADE)
    myimage = models.ImageField(upload_to='images', default = "null")
    desc = models.CharField(max_length=100)

class BlogFile(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default= 1, on_delete=models.CASCADE)
    myfile = models.FileField(upload_to='files', blank = False, null = False)
    desc = models.CharField(max_length=100)