from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .forms import IngredientFormSet, InstructionFormSet, RecipeForm
from .models import Recipe
from .filters import RecipeFilter
from django.db.models import Q
from rest_framework import viewsets
from .serializers import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('title')
    serializer_class = RecipeSerializer

def index(request):
    recipes = Recipe.objects.all()
    if "recipes" not in request.session:
        request.session["recipes"] = []

    filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
    recipes = filter.qs

    return render(request, "recipes/index.html", {
        "recipes": recipes,
        "filter": filter
    })



def add(request):
    if request.method == "GET":
        form = RecipeForm()
        ingredient_formset = IngredientFormSet()
        instruction_formset = InstructionFormSet()
        return render(request, "recipes/add.html", {
            "form":form,
            "ingredient_formset":ingredient_formset,
            "instruction_formset": instruction_formset
        })

    elif request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            recipe = form.save()
            # recipe = form.cleaned_data.get("recipe")
            ingredient_formset = IngredientFormSet(request.POST, instance=recipe)
            instruction_formset = InstructionFormSet(request.POST, instance=recipe)
            if ingredient_formset.is_valid() and instruction_formset.is_valid():
                ingredient_formset.save() and instruction_formset.save()

            request.session["recipes"] += [recipe]
            return HttpResponseRedirect(reverse("recipes:index"))
        else:    
            return render(request, "recipes/add.html", {
                "form": form,
        })

    return render(request, "recipes/add.html", {
        "form": form,
    })

def update(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipeForm = RecipeForm(instance=recipe)

    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            recipe = form.cleaned_data.get("recipe")
            request.session["recipes"] += [recipe]
            return redirect('/')

    return render(request, "recipes/add.html", {
        "form": form
    })

def delete(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect('/')

    return render(request, 'recipes/delete.html', {
        "form": recipe
    })

def view_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)

    return render(request, 'recipes/view.html', {
        "recipe": recipe
    })

def about(request):
    return render(request, 'recipes/about.html', {})