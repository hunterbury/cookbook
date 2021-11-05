from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=150)
    into = models.TextField()
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    servings = models.IntegerField()

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return self.name