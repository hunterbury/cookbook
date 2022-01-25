from rest_framework.response import Response
from ..recipes.models import Recipe, Comment
from .serializers import RecipeSerializer
from django.shortcuts import render, redirect
from ..recipes.filters import RecipeFilter
from django.core.paginator import Paginator
from ..recipes.forms import RecipeForm, CommentForm


def getRecipesList(request):
    filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
    recipes = filter.qs

    paginator = Paginator(recipes, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "recipes/index.html", {
        "recipes": recipes,
        "filter": filter,
        'page_obj':page_obj
    })
    # recipes = Recipe.objects.all().order_by('-date')
    # serializer = RecipeSerializer(recipes, many=True)
    # return Response(serializer.data)


def getRecipeDetail(request, pk):
    filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
    recipe = Recipe.objects.get(id=pk)

    comments = recipe.comments.filter(active=True)

    new_comment = None
    comment_form = CommentForm()

    return render(request, 'recipes/view.html', {
        "recipe": recipe,
        "filter": filter,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })

    # recipes = Recipe.objects.get(id=pk)
    # serializer = RecipeSerializer(recipes, many=False)
    # return Response(serializer.data)


def createRecipe(request):
    # form = RecipeForm(request.POST, request.FILES)

    # if form.is_valid():
    #     form.save()
    #     recipe = form.cleaned_data.get("recipe")
    #     # serializer = RecipeSerializer(instance=recipe, data=recipe)
    #     request.session["recipes"] += [recipe]
    #     return redirect('/')
    data = request.data
    recipe = Recipe.objects.create(data)
    serializer = RecipeSerializer(recipe, many=False)
    return Response(serializer.data)

def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)

    # if request.method == 'GET':

    # data = request.data
    # serializer = RecipeSerializer(instance=recipe, data=data)

        # form = RecipeForm(initial = {
        #     'title': 'recipe.title',
        #     'image': 'recipe.image',
        #     'cuisine': 'recipe.cuisine',
        #     'meal': 'recipe.meal',
        #     'description': 'recipe.description', 
        #     'prep_time': 'recipe.prep_time',
        #     'cook_time': 'recipe.cook_time',
        #     'servings': 'recipe.servings',
        #     'ingredients"' 'recipe.ingredients'
        #     'instructions': 'recipe.instructions',
        # })


        # return render(request, "recipes/add.html", {
        #     "form": form,
        # })

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            recipe = form.cleaned_data.get("recipe")
            # serializer = RecipeSerializer(instance=recipe, data=recipe)
            request.session["recipes"] += [recipe]
            return redirect('/')

    # if serializer.is_valid():
    #     serializer.save()

    # return Response(serializer.data)


def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe.delete()
    return Response('Recipe was deleted!')

def createComment(request, pk):
    recipe = Recipe.objects.get(id=pk)
    new_comment = None
    # A comment was posted
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        # Create Comment object but don't save to database yet          
        new_comment = comment_form.save(commit=False)
        # Assign the current post to the comment
        new_comment.recipe = recipe
        # Save the comment to the database
        new_comment.save()
    
    comments = recipe.comments.filter(active=True)

    return render(request, 'recipes/view.html', {
        "recipe": recipe,
        "filter": filter,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })