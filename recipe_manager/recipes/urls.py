from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('category/', views.category, name="category"),
    path('chef/<int:pk>/', views.chef, name="chef")
    ]