import django_filters
from django import forms
from .models import Recipe, CUISINE_CHOICES, MEAL_CHOICES
from .choices import CUISINE_CHOICES, MEAL_CHOICES
from django_filters import ChoiceFilter, CharFilter

class RecipeFilter(django_filters.FilterSet):
    cuisine = ChoiceFilter(field_name="cuisine", choices=CUISINE_CHOICES, lookup_expr='icontains', label='Cuisine:', widget=forms.Select(attrs={'class': 'form-control'}))
    meal = ChoiceFilter(field_name="meal", choices=MEAL_CHOICES, lookup_expr='icontains', label='Meal:', widget=forms.Select(attrs={'class': 'form-control'}))
    search = CharFilter(field_name="title", lookup_expr='icontains', label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search'}))

    class Meta:
        model = Recipe
        fields = ['cuisine', 'meal', 'search']