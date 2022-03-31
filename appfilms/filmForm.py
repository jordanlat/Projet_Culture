

from django import forms
from django.forms import ModelForm, modelformset_factory

from .models import Film

PLATEFORME_CHOICES = ['Netflix', 'Prime Video', 'Disney Plus', 'Autres']

class FilmForm(forms.Form):
    titre      = forms.CharField    (max_length=124)
    date       = forms.DateInput    (format='%Y') 
    type       = forms.CharField    (max_length=32)
    acteurs    = forms.CharField    (max_length=124)
    moy_note   = forms.DecimalField (max_digits=2, decimal_places=1)
    plateforme = forms.CharField    (max_length=64)
    resume     = forms.Textarea     ()
    statut     = forms.CharField    (max_length=16)
    par_qui    = forms.CharField    (max_length=254)
    liens      = forms.CharField    (max_length=254)


"""
class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = [
            'titre','date','type','acteurs','moy_note','plateforme','resume','statut','liens'
            ]
"""



FilmFormset = modelformset_factory(
    Film,
    form=FilmForm,
    fields = [
        'titre','date','type','acteurs','moy_note','plateforme','resume','statut','liens'
    ],
    extra=1
    )


