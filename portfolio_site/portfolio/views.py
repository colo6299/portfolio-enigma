from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('Home')

def contact(request):
    return HttpResponse('Contact me ')

def greet(request, name):
    return HttpResponse('Hello, %s' % name)

