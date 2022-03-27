from . import views
from django.urls import path

app_name = 'hub'

urlpatterns = [
    path('', views.hubView, name='hubView'),
    path('', views.logoutView, name='logoutView'),
]   