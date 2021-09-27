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


class NewNoteForm(forms.ModelForm):
    # text_content = forms.CharField(blank=True, editable=True, widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    text_content = forms.CharField(blank=True, editable=True, widget=forms.Textarea)