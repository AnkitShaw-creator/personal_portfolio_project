from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    datestamp = models.DateField()
    description = models.TextField(max_length=500)