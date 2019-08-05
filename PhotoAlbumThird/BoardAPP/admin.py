from django.contrib import admin
from BoardAPP import models
# Register your models here.

admin.site.register(models.Board)
admin.site.register(models.Message)