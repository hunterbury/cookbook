from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .forms import NewRecipeForm, IngredientFormSet

def index(request):
    if "recipes" not in request.session:
        request.session["recipes"] = []

    return render(request, "recipes/index.html", {
        "recipes": request.session["recipes"]
    })

def add(request):
    if request.method == "POST":
        form = NewRecipeForm(request.POST or None)
        if form.is_valid():
            recipe = form.save()
            formset = IngredientFormSet(request.POST, instance=recipe)
            if formset.is_valid():
                formset.save()
            return HttpResponseRedirect(reverse("recipes:index"))

    elif request.method == "GET":
        form = NewRecipeForm()
        formset = IngredientFormSet()
        return render(request, "recipes/add.html", {
            "form": form,
            "formset":formset
        })

    else:    
        return render(request, "recipes/add.html", {
            "form": form
    })

    return render(request, "recipes/add.html", {
        "form": NewRecipeForm()
    })