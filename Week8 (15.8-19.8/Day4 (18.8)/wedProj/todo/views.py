from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.utils import timezone
# Create your views here.


def all_tasks(request):
	task_list = ToDo.objects.all().order_by('date_creation')
	return render(request, 'display_todos.html', {"task_list" : task_list})


def tasks(request,title):
	task = get_object_or_404(ToDo,id=title)
	return render(request, 'task.html', {'task' : task})



def add_task(request):	
	if request.method == 'POST':
		task = ToDo(title=request.POST.get('title'),details=request.POST.get('details'),date_creation=timezone.now(),date_completion=request.POST.get('date_completion'),deadline_date=request.POST.get('deadline_date'),category=request.POST.get('category'))
		task.save()
		return redirect('all_tasks')
	return render(request, 'add_task.html')
