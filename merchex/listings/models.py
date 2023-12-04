from asyncio.windows_events import NULL
from dataclasses import Field
from xmlrpc.client import boolean
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class Band(models.Model):
    def __str__(self):
      return f'{self.name}' 
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5,default='pas de genre specifié')
    biography = models.fields.CharField(max_length=1000,default='Biographie indisponible')
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    ,default=2000,null=True)
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
class contact(models.Model):
    email = models.fields.CharField(max_length=100)
    number = models.IntegerField()
class Annonce(models.Model):
    class Type(models.TextChoices):
        Clothing = 'CL'
        Posters = 'PS'
        Miscellaneous = 'MI'     
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=10000)
    sold = models.fields.BooleanField(null=True)
    type =  models.fields.CharField(choices=Type.choices, max_length=5,default='pas de type specifié')
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)