# from typing_extensions import NotRequired, Required
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(default='', max_length=200)
    image=models.ImageField(default='', blank=True)


class ToDo(models.Model):
    title = models.CharField(default='', max_length=200)
    details = models.CharField(default='', max_length=500)
    date_creation = models.DateTimeField(default='1/1/2000')
    date_completion = models.DateTimeField(default='1/1/2000')
    deadline_date = models.DateTimeField(default='1/1/2000')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)


    url = models.URLField(default='')
    uploader_name = models.CharField(default='',max_length=200)
    created_at = models.DateTimeField(default='1/1/2000')