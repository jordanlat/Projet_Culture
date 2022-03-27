from tkinter import HIDDEN
from django.db import models
from django.forms import HiddenInput

class Film(models.Model):
    id         = models.DecimalField(primary_key=True, max_digits=10, decimal_places=1, auto_created=True)
    titre      = models.CharField   (max_length=124)
    date       = models.DateField   ()
    type       = models.CharField   (max_length=32)
    acteurs    = models.CharField   (max_length=124)
    moy_note   = models.DecimalField(max_digits=2, decimal_places=1)
    platforme  = models.CharField   (max_length=64)
    resume     = models.TextField   ()
    statut     = models.CharField   (max_length=16)
    date_ajout = models.DateField   ()
    par_qui    = models.CharField   (max_length=32)
    liens      = models.CharField   (max_length=254)

class statut(models.Model):
    id           = models.DecimalField(primary_key=True, max_digits=5, decimal_places=1, auto_created=True)
    label        = models.CharField   (max_length=124)
    film_titre   = models.CharField   (max_length=124)
    user_name    = models.CharField   (max_length=64)
    #user_id      = models.CharField   (max_length=32)