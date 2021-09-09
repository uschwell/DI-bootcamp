from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    employed_by=models.ForeignKey('Firm', on_delete=models.PROTECT)


class Firm(models.Model):
    name=CharField(max_length=200)


class Company(models.Model):
    name=CharField(max_length=200)
    firm=ForeignKey(Firm, on_delete=models.CASCADE)
