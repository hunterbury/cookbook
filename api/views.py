from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RecipeSerializer, CommentSerializer
from recipes.models import Recipe, Comment


@api_view(['GET'])
def getRecipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(recipe, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createRecipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(instance=recipe, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET','POST'])
def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe.delete()
    return Response('Recipe was deleted!')

@api_view(['POST'])
def createComment(request, pk):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
