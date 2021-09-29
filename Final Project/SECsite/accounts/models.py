from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField, EmailField
from django.db.models.fields.related import ForeignKey
# Create your models here.

class Note(models.Model):
    text_content = models.CharField(blank=True, editable=True, max_length=500)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    employed_by=models.ForeignKey('Firm', on_delete=models.PROTECT)
    

class Firm(models.Model):
    name=CharField(max_length=200)


class Client(models.Model):
    name=CharField(max_length=200)
    firm=ForeignKey(Firm, on_delete=models.CASCADE)
    yearly= DateField(blank=True, null=True)
    first_quarter= DateField(blank=True, null=True)
    second_quarter= DateField(blank=True, null=True)
    third_quarter= DateField(blank=True, null=True)
    client_mail= EmailField(blank=True, null=True)

