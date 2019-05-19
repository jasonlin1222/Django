from django.db import models

class Member(models.Model):
    Account = models.CharField(primary_key=True, max_length=20, unique=True)
    Password = models.CharField(blank=False, max_length=20)
    Username = models.CharField(max_length=20)
    Birthday = models.CharField(null=False, max_length=20)
    Email = models.EmailField(max_length=64, blank=True, default="")
    Phone = models.CharField(max_length=20)
    def __str__(self):
        return self.Username