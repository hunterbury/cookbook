from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# app_name = "recipes"
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("add/", views.add, name="add"),
#     path("update/", views.update, name="update"),
#     path("delete/", views.delete, name="delete"),
#     path("view_recipe/<str:pk>", views.view_recipe, name="view_recipe"),
#     path("about/", views.about, name="about"),
# ]
