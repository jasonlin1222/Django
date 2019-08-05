from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Album(models.Model):
    Topic = models.TextField(max_length=30, unique=True)
    Description = models.TextField(max_length=100)
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    CreateDate = models.DateField(auto_now=True)
    ShowPhoto = models.TextField(max_length=255)
    location = models.TextField(max_length=255)

    def __str__(self):
        return self.Topic

class Photo(models.Model):
    Path = models.TextField(max_length=255)
    Filename = models.TextField(max_length=255)
    Album = models.ForeignKey('Album',on_delete=models.CASCADE)
    PhotoDesc = models.TextField(max_length=255)
    UploadDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Filename
