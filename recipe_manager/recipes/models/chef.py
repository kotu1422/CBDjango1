from django.db import models
class Chef(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()