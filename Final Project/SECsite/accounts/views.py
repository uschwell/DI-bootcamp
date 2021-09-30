from django.http import request
from django import forms, template
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, decorators
from .forms import NewUserForm, NewClientForm, NewNoteForm
from .models import Client, Profile
from django.contrib.auth.models import User

def login_view(request):
    if request.method=='POST':
        print('request POST error')
        print(request.POST)
        user=authenticate(username=request.POST.get('userNameInput'), password=request.POST.get('passwordInput'))
        if user:
            login(request, user)
             #send us to relevant company page
            return redirect('company_page')

    return render(request,'login.html')


def main_page(request):
    if request.method=='POST':
        print('request POST error')
        print(request.POST)

    return render(request, 'mainPage.html')

@decorators.login_required
def register(request):
    form = NewUserForm()
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=User.objects.create_user(**form.cleaned_data)
            profile=Profile.objects.create(user=user, employed_by=request.user.profile.employed_by)
             #redirect to relevant company page
            return redirect('company_page')

    return render(request, 'register.html', {'f':form, 'object_type':'new Employee'})


@decorators.login_required
def company_page(request):

    form = NewClientForm()
    if request.method=='POST':
        form=NewClientForm(request.POST)
        if form.is_valid():
            client= form.save(commit=False)
            client.firm=request.user.profile.employed_by
            client.save()
            #redirect to relevant company page
            return redirect('mainPage')

    return render(request, 'companyPage.html', {'f':form, 'object_type':'client'})



@decorators.login_required
def new_note(request):

    form = NewNoteForm()
    if request.method=='POST':
        form=NewNoteForm(request.POST)
        if form.is_valid():
            note= form.save(commit=False)
            # note.Profile=request.user.profile.employed_by
            note.save()
            #redirect to relevant company page
            return redirect('mainPage')

    return render(request, 'companyPage.html', {'f':form, 'object_type':'client'})





@decorators.login_required
def settings_page(request):
    return render(request, 'settings.html')