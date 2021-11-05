from django.contrib import admin
from .models import Recipe, Ingredient

class IngredientInLine(admin.TabularInline):
    model = Ingredient

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInLine, ]
