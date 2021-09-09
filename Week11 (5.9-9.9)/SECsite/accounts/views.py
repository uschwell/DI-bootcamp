from django.http import request
from django import template
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method=='POST':
        print('request POST error')
        print(request.method.POST)

    return render(request,'login.html') 


class onLogin():
    pass

def main_page(request):
    if request.method=='POST':
        print('request POST error')
        print(request.method.POST)

    render(request, 'mainPage.html')
