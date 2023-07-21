from django.db import models
from django.utils import timezone
from . import Chef
from . import Ingredient
from . import Category

class Recipe(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True)