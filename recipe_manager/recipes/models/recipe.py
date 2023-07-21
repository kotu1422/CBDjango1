from django.db import models
from django.utils import timezone
from .chef import Chef
from .ingredient import Ingredient
from .category import Category

class Recipe(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(blank=True, null=True)