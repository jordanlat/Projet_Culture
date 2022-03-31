from django.shortcuts import render
from .models import Film
from .filmForm import  FilmForm


def filmView(request):
    form = FilmForm()
    if(request.POST):
        saveFilm(request)
    return render(request, 'appfilms/appfilms.html', {"form": form})


def saveFilm(request):
    form = Film()

    if(request.POST):
        data = request.POST.dict()
        form = Film(
          titre      = data.get('titre'),
          type       = data.get('type'),
          date       = data.get('date'),
          plateforme = data.get('plateforme'),
          moy_note   = data.get('note'),
          statut     = data.get('statut'),
          liens      = data.get('lien'),
          acteurs    = data.get('acteurs'),
          par_qui    = request.user,
          resume     = data.get('resume')
        )

        if form:
            print('Form is valid')
            form.save()


    else :
        print('******NO SUBMIT******')

    return render(request, 'appfilms/appfilms.html',{'form': form})


