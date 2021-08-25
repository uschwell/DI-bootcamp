from django.db import models
import datetime

# Create your models here.
class Gif(models.Model):
    title = models.CharField(default='', max_length=200)
    url = models.URLField(default='')
    uploader_name = models.CharField(default='',max_length=200)
    created_at = models.DateTimeField(default='1/1/2000')


class Category(models.Model):
    name = models.CharField(default='',max_length=200)
    gifs = models.ManyToManyField(Gif, blank=True)
