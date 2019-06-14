from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Board(models.Model):
    Topic = models.TextField(max_length=50)
    Description = models.TextField(max_length=100)
    CreateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Topic


class Message(models.Model):
    Message = models.TextField(max_length=200)
    Time = models.DateTimeField(auto_now=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Response = models.TextField(null=True, blank=True, max_length=200)
    Board = models.ForeignKey('Board',on_delete=models.CASCADE)

    def __str__(self):
        return self.Message
