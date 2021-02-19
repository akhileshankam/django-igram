from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50, default=2)
    username=models.CharField(max_length=50,default=1)
    image=models.ImageField(upload_to='images/')
    likes2=models.ManyToManyField(User)


    def __str__(self):
        return self.title
class comment(models.Model):
    text = models.CharField(max_length=1500, default=2)
    title = models.CharField(max_length=50, default=2)
    username = models.CharField(max_length=50, default=1)
    def __str__(self):
        return self.text

class messages(models.Model):
    fromusername = models.CharField(max_length=50, default=1)
    mssg = models.CharField(max_length=5000, default=1)
    tousername = models.CharField(max_length=50, default=1)
    def __str__(self):
        return self.mssg


