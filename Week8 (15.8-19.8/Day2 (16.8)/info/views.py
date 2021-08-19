# from animals.info.models import Animal, Family
from django.shortcuts import render
from info.models import Animal, Family







def get_Family(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
    context["dataset"]=Family.objects.all()
    return render(request, "list_view.html", context)

def get_Animal(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
    context["dataset"]=Animal.objects.all()
    return render(request, "list_view.html", context)

def get_Animals_all(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
    context["dataset"]=Animal.objects.all()
    return render(request, "list_view.html", context)
