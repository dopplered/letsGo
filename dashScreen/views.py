from django.shortcuts import render
from .models import DashScreen

# Create your views here.


def dash_list(request):
    dsc = DashScreen.objects.all().order_by('date')
    return render(request, 'dashScreen/dash_list.html', {'DashViews': dsc})


def login_view(request):
    dsc = DashScreen.objects.all().order_by('date')
    return render(request, 'dashScreen/login.html', {'DashViews': dsc})
