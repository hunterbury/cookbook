from django.urls import path
from . import views

app_name = "recipes"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
    path("view_recipe/<str:pk>", views.view_recipe, name="view_recipe"),
    path("about/", views.about, name="about"),
]
