from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import Http404
from .models import Recipe

def home(request):
    recipes = Recipe.objects
    return render(request, 'recipes/home.html', {"recipes":recipes})
