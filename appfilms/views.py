from django.shortcuts import render
from .models import Film
from .filmForm import  FilmForm


def filmView(request):
    database = Film.objects.all()
    a={"film_list": database}

    return render(request, 'appfilms/appfilms.html', a)


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



def sort_films(request, col_name):
    sort_data = Film.objects.order_by(col_name)
    a={"film_list": sort_data}

    return render(request, 'appfilms/appfilms.html', a)