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

app_name = "recipes"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("update/<str:pk>", views.update, name="update"),
    path("delete/<str:pk>", views.delete, name="delete"),
    path("view-recipe/<str:pk>", views.viewRecipe, name="view-recipe"),
    path('', include('django.contrib.auth.urls')),
    path('login/', views.loginView, name="login"),
    path('demo-login/', views.demoLogin, name="demo-login"),
]
