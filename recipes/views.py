from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .forms import NewRecipeForm, IngredientFormSet
from .models import Recipe, Ingredient

def index(request):
    if "recipes" not in request.session:
        request.session["recipes"] = []

    return render(request, "recipes/index.html", {
        "recipes": Recipe.objects.all()
    })

def add(request):
    form = NewRecipeForm()
    if request.method == "POST":
        form = NewRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            recipe = form.cleaned_data.get("recipe")
            request.session["recipes"] += [recipe]
            return HttpResponseRedirect(reverse("recipes:index"))
    else:    
        return render(request, "recipes/add.html", {
            "form": form
    })

    return render(request, "recipes/add.html", {
        "form": form
    })

def update(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = NewRecipeForm(instance=recipe)

    if request.method == "POST":
        form = NewRecipeForm(request.POST, instance=recipe)
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