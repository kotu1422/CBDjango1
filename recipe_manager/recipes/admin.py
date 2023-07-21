from django.contrib import admin
from .models import Recipe, Category, Chef, Ingredient

admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Chef)
admin.site.register(Ingredient)