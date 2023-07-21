from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import Http404
from .models import *

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/home.html', {"recipes":recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'recipes/category.html', {'category': category})

def chef(request, pk):
    chef = get_object_or_404(Chef, pk=pk)
    return render(request, 'recipes/chef.html', {'chef': chef})