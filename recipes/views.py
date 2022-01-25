from django.http.response import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import RecipeForm, CommentForm
from .filters import RecipeFilter
from .models import Recipe, Comment
from django.db.models import Q
from .serializers import RecipeSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .utils import getRecipesList, getRecipeDetail, createRecipe, updateRecipe, deleteRecipe, createComment

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

# @api_view(['GET'])
# @permission_classes([AllowAny])
# @authentication_classes([CsrfExemptSessionAuthentication, BasicAuthentication])
# def getRoutes(request):
#     routes = [
#         {
#             'Endpoint': '/recipes/',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an array of recipes'
#         },
#         {
#             'Endpoint': '/recipes/id',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns a single recipe object'
#         },
#         {
#             'Endpoint': '/recipes/create/',
#             'method': 'POST',
#             'body': {'body': ""},
#             'description': 'Creates new recipe with data sent in post request'
#         },
#         {
#             'Endpoint': '/recipes/id/update/',
#             'method': 'PUT',
#             'body': {'body': ""},
#             'description': 'Creates an existing recipe with data sent in post request'
#         },
#         {
#             'Endpoint': '/recipes/id/delete/',
#             'method': 'DELETE',
#             'body': None,
#             'description': 'Deletes an exiting recipe'
#         },
#     ]
#     return Response(routes)


@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([CsrfExemptSessionAuthentication, BasicAuthentication])
def recipes(request):
    if request.method == 'GET':
        return getRecipesList(request)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@authentication_classes([CsrfExemptSessionAuthentication, BasicAuthentication])
def viewRecipe(request, pk):
    if request.method == 'GET':
        return getRecipeDetail(request, pk)
    if request.method == 'POST':
        return createComment(request, pk)


@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([CsrfExemptSessionAuthentication, BasicAuthentication])
def createRecipe(request):
    return createRecipe(request)

def updateRecipe(request, pk):
    if request.method == 'GET':
        form = RecipeForm(initial = {
            'title': 'recipe.title',
            'image': 'recipe.image',
            'cuisine': 'recipe.cuisine',
            'meal': 'recipe.meal',
            'description': 'recipe.description', 
            'prep_time': 'recipe.prep_time',
            'cook_time': 'recipe.cook_time',
            'servings': 'recipe.servings',
            'ingredients"' 'recipe.ingredients'
            'instructions': 'recipe.instructions',
        })


        return render(request, "recipes/add.html", {
            "form": form,
        })

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([CsrfExemptSessionAuthentication, BasicAuthentication])
def updateRecipe(request, pk):
    return updateRecipe(request, pk)

@api_view(['DELETE'])
# @permission_classes([AllowAny])
# @authentication_classes([CsrfExemptSessionAuthentication, BasicAuthentication])
def deleteRecipe(request, pk):
    return deleteRecipe(request, pk)

# @api_view(['GET', 'PUT', 'DELETE', 'POST'])
# def recipe(request, pk):
#     if request.method == 'GET':
#         return getRecipeDetail(request, pk)
    
#     if request.method == 'PUT':
#         return updateRecipe(request, pk)
    
#     if request.method == 'DELETE':
#         return deleteRecipe(request, pk)
    
#     if request.method == 'POST':
#         return createComment(request, pk)
    #     comments = recipe.comments.filter(active=True)

    #     new_comment = None
    #     # A comment was posted
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         # Create Comment object but don't save to database yet          
    #         new_comment = comment_form.save(commit=False)
    #         # Assign the current post to the comment
    #         new_comment.recipe = recipe
    #         # Save the comment to the database
    #         new_comment.save()

    # return render(request, 'recipes/view.html', {
    #     "recipe": recipe,
    #     "filter": filter,
    #     'comments': comments,
    #     'new_comment': new_comment,
    #     'comment_form': comment_form
    # })

    # filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
    # recipe = Recipe.objects.get(id=pk)

    # comments = recipe.comments.filter(active=True)

    # new_comment = None

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/recipes')
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

def index(request):
    return redirect('/')

# class RecipeViewSet(viewsets.ModelViewSet):
#     queryset = Recipe.objects.all().order_by('date')
#     serializer_class = RecipeSerializer

# def index(request):
#     recipes = Recipe.objects.all().order_by('date')
#     if "recipes" not in request.session:
#         request.session["recipes"] = []

#     filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
#     recipes = filter.qs

#     # recipes = Recipe.objects.all().order_by('-date')
#     paginator = Paginator(recipes, 15)

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)



#     return render(request, "recipes/index.html", {
#         "recipes": recipes,
#         "filter": filter,
#         'page_obj':page_obj
#     })

# def add(request):
#     filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())

#     if request.method == "GET":
#         form = RecipeForm()
#         # ingredient_formset = IngredientFormSet()
#         # instruction_formset = InstructionFormSet()
#         return render(request, "recipes/add.html", {
#             "form":form,
#             "filter": filter
#             # "ingredient_formset":ingredient_formset,
#             # "instruction_formset": instruction_formset
#         })

#     elif request.method == "POST":
#         form = RecipeForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
#             recipe = form.cleaned_data.get("recipe")
#             # recipe = form.cleaned_data.get("recipe")
#             # ingredient_formset = IngredientFormSet(request.POST, instance=recipe)
#             # instruction_formset = InstructionFormSet(request.POST, instance=recipe)
#             # if ingredient_formset.is_valid() and instruction_formset.is_valid():
#             #     ingredient_formset.save() and instruction_formset.save()

#             request.session["recipes"] += [recipe]
#             return redirect('/')

#         else:    
#             return render(request, "recipes/add.html", {
#                 "form": form,
#         })

#     return render(request, "recipes/add.html", {
#         "filter": filter
#     })

# def update(request, pk):
#     filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
#     recipe = Recipe.objects.get(id=pk)
#     recipeForm = RecipeForm(instance=recipe)

#     if request.method == "POST":
#         form = RecipeForm(request.POST, instance=recipe)
#         if form.is_valid():
#             form.save()
#             recipe = form.cleaned_data.get("recipe")
#             request.session["recipes"] += [recipe]
#             return redirect('/')

#     return render(request, "recipes/add.html", {
#         "form": form,
#         "filter": filter
#     })

# def delete(request, pk):
#     filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
#     recipe = Recipe.objects.get(id=pk)
#     if request.method == "POST":
#         recipe.delete()
#         return redirect('/')

#     return render(request, 'recipes/delete.html', {
#         "form": recipe,
#         "filter": filter
#     })

# def viewRecipe(request, pk):
#     filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
#     recipe = Recipe.objects.get(id=pk)

#     comments = recipe.comments.filter(active=True)

#     new_comment = None

#     if request.method == 'POST':
#         # A comment was posted
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet          
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.recipe = recipe
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm() 

#     return render(request, 'recipes/view.html', {
#         "recipe": recipe,
#         "filter": filter,
#         'comments': comments,
#         'new_comment': new_comment,
#         'comment_form': comment_form
#     })
