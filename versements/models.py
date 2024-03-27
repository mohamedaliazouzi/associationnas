from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from agriculteurs.models import Agriculteurs


# Create your models here.
class Versements(models.Model):
    agriculteur = models.ForeignKey(Agriculteurs, on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    date_versement = models.DateTimeField(default=datetime.now(), validators=[
        MinValueValidator(limit_value=datetime.strptime('00:00', '%H:%M')),
        MaxValueValidator(limit_value=datetime.strptime('23:59', '%H:%M'))
    ])
    num_versement = models.IntegerField(default=0)
    montant_versement = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.date_versement
