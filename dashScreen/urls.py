from django.conf.urls import url, include
from django.contrib import admin
from . import views

#from django.contrib.auth import views as auth_views


urlpatterns = [

    url(r'^$', views.dash_list),
    url(r'^sensors/$', views.dash_list),
    url(r'^login/$', views.login_view)

]
