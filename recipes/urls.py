from django.urls import include, path
from rest_framework import routers
from . import views



app_name = "recipes"
urlpatterns = [
    path('', views.index, name="index"),
    path("create/", views.createRecipe, name="create"),
    path("update/<str:pk>/", views.updateRecipe, name="update"),
    path("delete/<str:pk>/", views.deleteRecipe, name="delete"),
    path("view/<str:pk>/", views.viewRecipe, name="view"),
    path("view/<str:pk>/comment/", views.createComment, name="comment"),
    path('', include('django.contrib.auth.urls')),
    path('login/', views.loginView, name="login"),
    path('demo-login/', views.demoLogin, name="demo-login"),
]
