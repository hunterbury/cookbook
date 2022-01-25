from django.urls import include, path
from rest_framework import routers
from . import views



app_name = "recipes"
urlpatterns = [
    path('', views.recipes, name="recipes"),
    path('create/', views.createRecipe, name="create-recipe"),
    path('recipes/<str:pk>/', views.viewRecipe, name="view-recipe"),
    path('recipes/<str:pk>/update', views.updateRecipe, name="update-recipe"),
    path('recipes/<str:pk>/delete', views.deleteRecipe, name="delete-recipe"),

    # path("add/", views.add, name="add"),
    # path("update/<str:pk>", views.update, name="update"),
    # path("delete/<str:pk>", views.delete, name="delete"),
    # path("view-recipe/<str:pk>", views.viewRecipe, name="view-recipe"),
    path('', include('django.contrib.auth.urls')),
    path('login/', views.loginView, name="login"),
    path('demo-login/', views.demoLogin, name="demo-login"),
]
