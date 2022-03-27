

from django.forms import ModelForm, inlineformset_factory, modelform_factory, modelformset_factory

from .models import Film


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields= '__all__'


FilmFormset = modelformset_factory(
    Film,
    #fields=('tittre','type','acteurs','plateforme', 'statut', 'par_qui', 'liens')
    form=FilmForm,
    extra=1
    )
