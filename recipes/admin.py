from django.contrib import admin
from .models import Recipe

# class IngredientInline(admin.TabularInline):
#     model = Ingredient

# class InstructionInline(admin.TabularInline):
#     model = Instruction 

admin.site.register(Recipe)
# class RecipeAdmin(admin.ModelAdmin):
#     inlines = [IngredientInline, InstructionInline]

