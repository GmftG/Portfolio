from django.db import models
from datetime import date
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length = 100)
    timescooked = models.IntegerField()

    def __str__(self) -> str:
        return  self.name
    
    

class Recipe(models.Model):
    name = models.CharField(max_length = 100)
    products = models.ManyToManyField(Product, through = "Enrollment")
    def __str__(self) -> str:
        return  self.name
    


class Enrollment(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    weight = models.IntegerField()