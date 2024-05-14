from asyncio import tasks

from django.shortcuts import render
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task

def index(request):
    task = Task.objects.order_by('-id')
    return render(request, "main/index.html", {'title': 'Главная страница', 'tasks': task})

def about(request):
    return render(request, "main/about.html")

def create(request):
    form = TaskForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, "main/create.html")

def shablon(request):
    return render(request, "main/1SHABLON.html")
