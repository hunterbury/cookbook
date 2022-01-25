from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.getRecipes, name="get-recipes"),
    path('create/', views.createRecipe, name="create-recipe"),
    path('view/<str:pk>/', views.viewRecipe, name="view-recipe"),
    path('delete/<str:pk>/', views.deleteRecipe, name="delete-recipe"),
    path('update/<str:pk>/', views.updateRecipe, name="update-recipe"),
    path('view/<str:pk>/comment/', views.createComment, name="create-comment"),
]