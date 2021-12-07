from django.db import models
from recipes.choices import *

class Details(models.Model):        
    title = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True, upload_to="images/", default="images/default.jpg")
    cuisine = models.CharField(null=True, blank=True, max_length=20, choices=CUISINE_CHOICES, default='None')
    meal = models.CharField(null=True, blank=True, max_length=20, choices=MEAL_CHOICES, default='None')
    info = models.CharField(max_length=500)
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    servings = models.IntegerField()

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    quantity = models.FloatField(null=True, blank=True)
    measurement = models.CharField(null=True, blank=True, max_length=20, choices=MEASUREMENT_CHOICES, default='None')

    def __str__(self):
        return self.name

class Instruction(models.Model):
    instruction = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return self.instruction

class Recipe(Details, Ingredient, Instruction):
    pass

    def __str__(self):
        return self.id
