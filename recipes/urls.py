from django.urls import include, path
from rest_framework import routers
from . import views



app_name = "recipes"
urlpatterns = [
    path('', views.index, name="index"),
    path("create/", views.createRecipe, name="create"),
    path("update/<slug:slug>/", views.updateRecipe, name="update"),
    path("delete/<slug:slug>/", views.deleteRecipe, name="delete"),
    path("view/<slug:slug>/", views.viewRecipe, name="view"),
    path("view/comment/<slug:slug>/", views.createComment, name="comment"),
    path('', include('django.contrib.auth.urls')),
    path('login/', views.loginView, name="login"),
    path('demo-login/', views.demoLogin, name="demo-login"),
]
