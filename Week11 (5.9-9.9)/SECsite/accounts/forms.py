from django import forms
from django.db.models import fields
from .models import Client



class NewUserForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200, widget=forms.PasswordInput)





class NewClientForm(forms.ModelForm):
    class Meta:
        model=Client
        exclude=['firm']