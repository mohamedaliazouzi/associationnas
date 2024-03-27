from django.db import models


# Create your models here.
class Agriculteurs(models.Model):
    nom_agriculteur = models.CharField(max_length=15)
    prenom_agriculteur = models.CharField(max_length=15)
    borne = models.IntegerField()
    solde_en_dt = models.FloatField(default=0.0)
    nbre_des_versements = models.IntegerField(default=0)

    def __str__(self):
        return self.nom_agriculteur
