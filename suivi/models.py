from django.core.validators import MinValueValidator
from django.db import models

from agriculteurs.models import Agriculteurs


# Create your models here.
class Suivi(models.Model):
    agriculteur = models.OneToOneField(Agriculteurs, null=True, blank=True, on_delete=models.CASCADE)
    nbre_heures = models.FloatField(validators=[MinValueValidator(0.0)])
    date_debut_irrigation = models.DateTimeField

    def __str__(self):
        return self.nbre_heures
