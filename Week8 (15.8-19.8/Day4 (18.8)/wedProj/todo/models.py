from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(default='John Doe', max_length=200)
    image=models.ImageField()


class ToDo(models.Model):
    title = models.CharField(default='', max_length=200)
    url = models.URLField(default='')
    uploader_name = models.CharField(default='',max_length=200)
    created_at = models.DateTimeField(default='1/1/2000')