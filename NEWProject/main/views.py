from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Hello</h4>")

def res(request):
    return HttpResponse("<h1>First URL adress</h1>")  #new views
