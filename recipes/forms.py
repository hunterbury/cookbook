from django import forms
from django.forms import modelformset_factory
from .models import Ingredient, Recipe, Instruction
from recipes.choices import *


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    def clean_servings(self):
        value = self.cleaned_data.get("servings")
        print(value)
        if value < 1:
            raise forms.ValidationError("The number of servings must be greater than zero.")
        return value

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient 
        exclude = ('recipe',)

class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction 
        exclude = ('recipe',)

IngredientFormSet = modelformset_factory(Ingredient, form=IngredientForm, extra=2)
InstructionFormSet = modelformset_factory(Instruction, form=InstructionForm, extra=2)
