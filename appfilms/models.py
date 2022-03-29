from django.db import models

class Film(models.Model):

    id         = models.AutoField   (primary_key=True)
    titre      = models.CharField   (max_length=124)
    date       = models.IntegerField   (null=True) 
    type       = models.CharField   (max_length=32, null=True)
    acteurs    = models.CharField   (max_length=124, null=True)
    moy_note   = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    plateforme  = models.CharField   (max_length=64, null=True)
    resume     = models.TextField   (null=True)
    statut     = models.CharField   (max_length=16, null=True)
    date_ajout = models.DateField   (auto_now=True)
    par_qui    = models.CharField   (max_length=254, null=True)
    liens      = models.CharField   (max_length=254, null=True)


class statut(models.Model):
    id           = models.AutoField(primary_key=True)
    label        = models.CharField   (max_length=124)
    film_titre   = models.CharField   (max_length=124)
    user_name    = models.CharField   (max_length=64)
    #user_id      = models.CharField   (max_length=32)