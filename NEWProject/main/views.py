from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "main/1SHABLON.html")

def about(request):
    return HttpResponse("<h1>About</h1>")
