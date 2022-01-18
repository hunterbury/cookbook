from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .forms import RecipeForm
from .models import Recipe
from .filters import RecipeFilter
from django.db.models import Q
from rest_framework import viewsets
from .serializers import RecipeSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('date')
    serializer_class = RecipeSerializer

def index(request):
    recipes = Recipe.objects.all().order_by('date')
    if "recipes" not in request.session:
        request.session["recipes"] = []

    filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
    recipes = filter.qs

    # recipes = Recipe.objects.all().order_by('-date')


    return render(request, "recipes/index.html", {
        "recipes": recipes,
        "filter": filter
    })

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def demoLogin(request):
    if request.method == 'POST':
        username = 'demo_user'
        password = 'demo_password'
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('/')

def add(request):
    if request.method == "GET":
        form = RecipeForm()
        # ingredient_formset = IngredientFormSet()
        # instruction_formset = InstructionFormSet()
        return render(request, "recipes/add.html", {
            "form":form,
            # "ingredient_formset":ingredient_formset,
            # "instruction_formset": instruction_formset
        })

    elif request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            recipe = form.cleaned_data.get("recipe")
            # recipe = form.cleaned_data.get("recipe")
            # ingredient_formset = IngredientFormSet(request.POST, instance=recipe)
            # instruction_formset = InstructionFormSet(request.POST, instance=recipe)
            # if ingredient_formset.is_valid() and instruction_formset.is_valid():
            #     ingredient_formset.save() and instruction_formset.save()

            request.session["recipes"] += [recipe]
            return redirect('/')

        else:    
            return render(request, "recipes/add.html", {
                "form": form,
        })

    return render(request, "recipes/add.html", {
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