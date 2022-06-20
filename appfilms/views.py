from django.shortcuts import render
from .models import Film
from django.db.models import Q

# Actualise la liste des films
def database():
    database = Film.objects.all()
    return(database)


# Vue principale / on affiche la liste de film
def filmView(request):
    a={"film_list": database}
    return render(request, 'appfilms/main.app.film.html', a)




# Pour enregistrer un film
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
            a={"film_list": database}
    else :
        # Plus tard ajouté message erreur utilisateur
        print('******NO SUBMIT******')

    return render(request, 'appfilms/main.app.film.html',a)



def sort_films(request, col_name):
    sort_data = Film.objects.order_by(col_name)
    a={"film_list": sort_data}

    return render(request, 'appfilms/main.app.film.html', a)


def search(request):
    #words = request.POST.get('search')
    print('words = ')
    #print(words)

    #object_list = Film.objects.filter()
    #print(object_list)


    return render(request, 'appfilms/main.app.film.html')
