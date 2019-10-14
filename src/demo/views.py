from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'demo/login.html')

def top(request):
    return HttpResponse("this is top.")