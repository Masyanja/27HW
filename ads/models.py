from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
