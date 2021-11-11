from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .forms import RecipeForm, IngredientForm, InstructionForm
from .models import Recipe, Ingredient, Instruction
from django.db.models import Q

def index(request):
    recipes = Recipe.objects.all()
    if "recipes" not in request.session:
        request.session["recipes"] = []
    query = request.GET.get('q', None)
    if query:
        recipes = recipes.filter(
            Q(title__icontains=query) | Q(cuisine__icontains=query)
        )

    return render(request, "recipes/index.html", {
        "recipes": recipes,
    })



def add(request):
    recipeForm = RecipeForm()
    ingredientForm = IngredientForm()
    instructionForm = InstructionForm()
    if request.method == "POST":
        recipeForm = RecipeForm(request.POST, request.FILES)
        if recipeForm.is_valid():
            recipeForm.save()
            recipe = recipeForm.cleaned_data.get("recipe")
            request.session["recipes"] += [recipe]
            return HttpResponseRedirect(reverse("recipes:index"))
    else:    
        return render(request, "recipes/add.html", {
            "recipeForm": recipeForm,
            "ingredientForm": ingredientForm,
            "instructionForm": instructionForm
    })

    return render(request, "recipes/add.html", {
        "recipeForm": recipeForm,
        "ingredientForm": ingredientForm,
        "instructionForm": instructionForm
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

def view(request, pk):
    recipe = Recipe.objects.get(id=pk)

    return render(request, 'recipes/view.html', {
        "recipe": recipe
    })

def about(request):
    return render(request, 'recipes/about.html', {})