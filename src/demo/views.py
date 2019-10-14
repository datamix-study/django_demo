from django.http import HttpResponse
from django.shortcuts import render

from .models import User


def index(request):
    return render(request, 'demo/login.html')


def login(request):

    try:
        user = User.objects.get(username=request.POST['username'], password=request.POST['password'])
        # print(request.POST['username'])
        # print(request.POST['password'])
        # user = User.objects.get(pk=1)

        context = {"username":user.username}
        return render(request, 'demo/top.html', context)

    except User.DoesNotExist:
        context = {"message":"User DoesNotExist"}
        return render(request, 'demo/login.html', context)

    except User.MultipleObjectsReturned:
        context = {"message":"Multiple User found"}
        return render(request, 'demo/login.html', context)


def top(request):
    return render(request, 'demo/top.html')
