import django_filters
from .models import Product, CUISINE_CHOICES, MEAL_CHOICES
from .choices import CUISINE_CHOICES, MEAL_CHOICES
from django_filters import ChoiceFilter

class ProductFilter(django_filters.FilterSet):
    cuisine = ChoiceFilter(field_name="cuisine", choices=CUISINE_CHOICES, lookup_expr='icontains', label='Cuisine:')
    meal = ChoiceFilter(field_name="meal", choices=MEAL_CHOICES, lookup_expr='icontains', label='Meal:')

    class Meta:
        model = Product
        fields = ['cuisine', 'meal']