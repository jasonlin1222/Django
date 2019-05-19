from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    Topic = models.TextField(max_length=100, null=False)
    Discription = models.TextField(max_length=200)
    CreateData = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Topic
class Message(models.Model):
    Message = models.TextField(max_length=300)
    Tine = models.DateTimeField(auto_now=True)
    Resp = models.TextField(max_length=200, null=True, blank=True)
    Board = models.ForeignKey('Board', on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.Message