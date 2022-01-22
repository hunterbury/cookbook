from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .forms import RecipeForm, CommentForm
from .models import Recipe, Comment
from .filters import RecipeFilter
from django.db.models import Q
from rest_framework import viewsets
from .serializers import RecipeSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def index(request):
    recipes = Recipe.objects.all().order_by('date')
    if "recipes" not in request.session:
        request.session["recipes"] = []

    filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
    recipes = filter.qs

    # recipes = Recipe.objects.all().order_by('-date')
    paginator = Paginator(recipes, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    return render(request, "recipes/index.html", {
        "recipes": recipes,
        "filter": filter,
        'page_obj':page_obj
    })


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
    paginator = Paginator(recipes, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    return render(request, "recipes/index.html", {
        "recipes": recipes,
        "filter": filter,
        'page_obj':page_obj
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
    filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())

    if request.method == "GET":
        form = RecipeForm()
        # ingredient_formset = IngredientFormSet()
        # instruction_formset = InstructionFormSet()
        return render(request, "recipes/add.html", {
            "form":form,
            "filter": filter
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
        "filter": filter
    })

def update(request, pk):
    filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
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
        "form": form,
        "filter": filter
    })

def delete(request, pk):
    filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
    recipe = Recipe.objects.get(id=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect('/')

    return render(request, 'recipes/delete.html', {
        "form": recipe,
        "filter": filter
    })

def viewRecipe(request, pk):
    filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
    recipe = Recipe.objects.get(id=pk)

    comments = recipe.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet          
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.recipe = recipe
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm() 

    return render(request, 'recipes/view.html', {
        "recipe": recipe,
        "filter": filter,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })
