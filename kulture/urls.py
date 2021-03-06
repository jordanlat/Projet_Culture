"""kulture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import include, path
from hub import views as hubView
from login import views as loginView
from appfilms import views as appfilmsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('hub/', include('hub.urls')),
    path('hub/', hubView.hubView, name='hub'),
    path('', loginView.logoutView, name="logout"),
    path('films', appfilmsView.filmView, name='films'),
    path('films/ok', appfilmsView.saveFilm, name='saveFilm'),
    path('films/sort_films/<str:col_name>', appfilmsView.sort_films, name='sort_films'),
    path('films/search', appfilmsView.search, name='search'),
    path('films/delete/<int:id>', appfilmsView.delete, name='delete'),
    path('films/reload', appfilmsView.reload, name='reload'),
    path('films/redirect/<int:id>', appfilmsView.redirect, name='redirect'),
]
