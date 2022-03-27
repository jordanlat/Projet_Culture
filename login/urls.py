#from django import views
from django.urls import path
from . import urls
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.loginView, name='loginView'),
]