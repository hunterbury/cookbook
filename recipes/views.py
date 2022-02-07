from django.http.response import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import RecipeForm, CommentForm
from .filters import RecipeFilter
from django.core.paginator import Paginator
from .models import Recipe, Comment
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.response import Response

def index(request):
    recipes = Recipe.objects.all().order_by('-date')

    if request.user.is_authenticated:
            return render(request, "recipes/index.html", {
            "recipes": recipes,
        })
    else:
        return redirect('/login/')
    

def blog(request):
    recipes = Recipe.objects.all().order_by('date')
    if "recipes" not in request.session:
        request.session["recipes"] = []

    filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
    recipes = filter.qs

    paginator = Paginator(recipes, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    return render(request, "recipes/blog.html", {
        "recipes": recipes,
        "filter": filter,
        'page_obj':page_obj
    })

def viewRecipe(request, slug):
    filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
    recipe = Recipe.objects.get(slug=slug)

    comments = recipe.comments.filter(active=True)
    comment_form = CommentForm()
    new_comment = None

    return render(request, 'recipes/view.html', {
            "recipe": recipe,
            "filter": filter,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form
        })

def createRecipe(request):
    recipes = Recipe.objects.all()
    filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())

    if request.method == "GET":
        form = RecipeForm(initial = {
            'ingredients': "- ",
            'instructions': "1. ",
        })
        return render(request, "recipes/add.html", {
            "form":form,
            "filter": filter
        })

    elif request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            recipe = form.cleaned_data.get("recipe")
            return redirect('/')

        else:    
            return render(request, "recipes/add.html", {
                "form": form,
        })

    return render(request, "recipes/add.html", {
        "filter": filter
    })

def updateRecipe(request, slug):
    recipe = Recipe.objects.get(slug=slug)

    if request.method == 'GET':
        form = RecipeForm(initial = {
            'title': recipe.title,
            'image': recipe.image,
            'cuisine': recipe.cuisine,
            'meal': recipe.meal,
            'description': recipe.description, 
            'prep_time': recipe.prep_time,
            'cook_time': recipe.cook_time,
            'servings': recipe.servings,
            'ingredients': recipe.ingredients,
            'instructions': recipe.instructions,
        })
    elif request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)

        if form.is_valid():
            form.save()
            recipe = form.cleaned_data.get("recipe")
            return redirect('recipes:view', slug)

        else:    
            return render(request, "recipes/update.html", {
                "form": form,
                "recipe": recipe,
        })

    return render(request, "recipes/update.html", {
        "form": form,
        "recipe": recipe,
    })

def deleteRecipe(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    comments = recipe.comments.filter(active=True)
    comment_form = CommentForm()
    new_comment = None

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        recipe.delete()
        
        return redirect('/')

def createComment(request, slug):
    filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
    recipe = Recipe.objects.get(slug=slug)
    new_comment = None
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.recipe = recipe
        new_comment.save()
    
    comments = recipe.comments.filter(active=True)

    return render(request, 'recipes/view.html', {
        'recipe': recipe,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
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
    return render(request, 'recipes/index.html', {'form': form})

def demoLogin(request):
    if request.method == 'POST':
        username = 'demo_user'
        password = 'demo_password'
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('/')

def logout(request):
    return render(request, 'recipes/index.html', {})





