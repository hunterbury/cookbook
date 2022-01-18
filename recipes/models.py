from django.db import models
from recipes.choices import *
from django.contrib.auth.models import User


class Recipe(models.Model):        
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    image = models.URLField(null=True, blank=True, default="https://i0.wp.com/images-prod.healthline.com/hlcmsresource/images/AN_images/healthy-eating-ingredients-1296x728-header.jpg?w=1155&h=1528")
    cuisine = models.CharField(null=True, blank=True, max_length=20, choices=CUISINE_CHOICES, default='None')
    meal = models.CharField(null=True, blank=True, max_length=20, choices=MEAL_CHOICES, default='None')
    description = models.CharField(max_length=500)
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    servings = models.IntegerField()
    ingredients = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

# class Ingredient(models.Model):
#     name = models.CharField(null=True, blank=True, max_length=100)
#     quantity = models.FloatField(null=True, blank=True)
#     measurement = models.CharField(null=True, blank=True, max_length=20, choices=MEASUREMENT_CHOICES, default='None')

#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

#     def __str__(self):
#         return self.name

# class Instruction(models.Model):
#     instruction = models.CharField(null=True, blank=True, max_length=300)

#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="instructions")
    
#     def __str__(self):
#         return self.instruction

