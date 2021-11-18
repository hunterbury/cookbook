from django.db import models
from recipes.choices import *

class Ingredient(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    quantity = models.FloatField(null=True, blank=True)
    measurement = models.CharField(null=True, blank=True, max_length=20, choices=MEASUREMENT_CHOICES, default='None')

    def __str__(self):
        return self.name

class Recipe(models.Model):        
    title = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True, upload_to="images/", default="images/default.jpg")
    cuisine = models.CharField(null=True, blank=True, max_length=20, choices=CUISINE_CHOICES, default='None')
    meal = models.CharField(null=True, blank=True, max_length=20, choices=MEAL_CHOICES, default='None')
    info = models.CharField(max_length=500)
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    servings = models.IntegerField()
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE, default='None')

    def __str__(self):
        return self.title



class Instruction(models.Model):
    instruction = models.CharField(null=True, blank=True, max_length=300)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="instructions", null=True)


    def __str__(self):
        return self.instruction

