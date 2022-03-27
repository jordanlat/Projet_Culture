from urllib.request import Request
from django.shortcuts import redirect, render
from django.template import RequestContext

from .filmForm import  FilmForm
#from .filmForm import FilmFormset

""""""
def filmView(request):
    form = FilmForm()
    print(request.user.username)
    print("Welcome to appFilms")
    return render(request, 'appfilms/appfilms.html', {"form": form})







def saveFilm(request):
    form = FilmForm()
    print(form)


    if request.POST:
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save()
            film_formset = FilmForm(request.POST, instance=film)
            if film_formset.is_valid():
                film_formset.save()
            return redirect('film')
    return render('appfilms.html',{
        'form': form, 'formset': film_formset
    },
    context_instance=RequestContext(request)
    )


