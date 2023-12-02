from django.db import models
from django.utils import timezone

from .. products.models import Product


class Events(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=150)


class Public(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=200)


class New_Products(models.Model):
    product_name = models.CharField(verbose_name='Новинки продукции', max_length=150)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


class Enxibitation_Calendar(models.Model):
    period = models.CharField(max_length=100)
    data_of_participation = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    name_exhibition = models.TextField()
