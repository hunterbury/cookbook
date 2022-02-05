from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.getRecipes, name="get-recipes"),
    path('create/', views.createRecipe, name="create-recipe"),
    path('view/<slug:slug>/', views.viewRecipe, name="view-recipe"),
    path('delete/<slug:slug>/', views.deleteRecipe, name="delete-recipe"),
    path('update/<slug:slug>/', views.updateRecipe, name="update-recipe"),
    path('view/<slug:slug>/comment/', views.createComment, name="create-comment"),
    path('comments/', views.getComments, name="comments")
]