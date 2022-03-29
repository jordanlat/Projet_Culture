

from django.forms import ModelForm, modelformset_factory

from .models import Film


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = [
            'titre','date','type','acteurs','moy_note','plateforme','resume','statut','liens'
            ]


FilmFormset = modelformset_factory(
    Film,
    form=FilmForm,
    extra=1
    )
