from django import forms
from django.forms import modelformset_factory
from .models import Recipe, Comment
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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

# class IngredientForm(forms.ModelForm):
#     class Meta:
#         model = Ingredient
#         exclude = ('recipe',)

# IngredientFormSet = forms.inlineformset_factory(Recipe, Ingredient, form=IngredientForm)

# class InstructionForm(forms.ModelForm):
#     class Meta:
#         model = Instruction
#         exclude = ('recipe',)

# InstructionFormSet = forms.inlineformset_factory(Recipe, Instruction, form=InstructionForm)