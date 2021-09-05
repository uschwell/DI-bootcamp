from django.db import models
import datetime

# Create your models here.
class Country(models.Model):
    name = models.CharField(default='', max_length=200)

class Category(models.Model):
    name = models.CharField(default='', max_length=200)

class Director(models.Model):
    first_name = models.CharField(default='', max_length=200)
    last_name = models.CharField(default='', max_length=200)

class Film(models.Model):
    title = models.CharField(default='', max_length=200)
    release_date  = models.DateField(auto_now_add=True, blank=True)
    created_in_country = models.ForeignKey(Country, on_delete = models.CASCADE, related_name = "countries")
    available_in_countries = models.ManyToManyField(Country)
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)

