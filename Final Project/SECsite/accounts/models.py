# from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
# Create your models here.

class Notes(models.Model):
    text_content = models.CharField(blank=True, editable=True)


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    employed_by=models.ForeignKey('Firm', on_delete=models.PROTECT)
    # notes = models.ForeignKey(Notes, blank=True, null=True, on_delete=models.CASCADE, Required=False)
    notes = models.ForeignKey(Notes, blank=True, null=True, on_delete=models.CASCADE)

class Firm(models.Model):
    name=CharField(max_length=200)


class Client(models.Model):
    name=CharField(max_length=200)
    firm=ForeignKey(Firm, on_delete=models.CASCADE)


