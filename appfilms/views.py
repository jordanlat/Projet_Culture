from urllib.request import Request
from django.shortcuts import redirect, render
from django.template import RequestContext

from .filmForm import  FilmForm
#from .filmForm import FilmFormset

def filmView(request):
    form = FilmForm()
    #print(request.user.username)
    #print("Welcome to appFilms")
    return render(request, 'appfilms/appfilms.html', {"form": form})


def saveFilm(request):
    form = FilmForm()
    print('SUBMITTED')


    if request.method == 'POST':
        print('-----SUBMIT OK----')
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save(commit=False)
            film.par_qui = request.user
            film_formset = FilmForm(request.POST, instance=film)
            if film_formset.is_valid():
                film_formset.save()
            return redirect('films')
    else :
        print('******NO SUBMIT******')

    return render(request, 'appfilms/appfilms.html',{'form': form})


