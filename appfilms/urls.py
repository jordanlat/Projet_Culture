from django.urls import path
from . import views

app_name = 'appfilms'

urlpatterns = [
    path('films', views.filmView, name='filmView'),
    #path('saveFilm', views.saveFilm, name='saveFilm'),
]   