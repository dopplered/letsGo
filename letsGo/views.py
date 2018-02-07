from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


def homepage(request):
    return HttpResponse('homepage')


def sensors(request):
    # return HttpResponse('sensors')
    return render(request, 'sensors.html')
