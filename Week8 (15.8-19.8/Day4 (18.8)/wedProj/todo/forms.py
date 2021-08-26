from django import forms
from django.db import models
from .models import Category
# from django.utils import timezone



class ToDoForm(forms.Form):
    title = models.CharField(default='', max_length=200)
    details = models.CharField(default='', max_length=500)
    date_creation = models.DateTimeField(default='1/1/2000')
    date_completion = models.DateTimeField(default='1/1/2000')
    deadline_date = models.DateTimeField(default='1/1/2000')
    address = forms.ModelChoiceField(queryset=Category.objects.all())