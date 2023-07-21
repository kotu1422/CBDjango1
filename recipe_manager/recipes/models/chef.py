from django.db import models
class Chef(models.Model):
    name = models.CharField(max_length=250)
    bio = models.TextField()