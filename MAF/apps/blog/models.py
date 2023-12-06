from django.db import models
from django.utils import timezone

from .. products.models import Product


class Events(models.Model):
    title = models.CharField(verbose_name='События', max_length=150)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    image = models.CharField(verbose_name='Картинка', max_length=150)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Событиe'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.title


class Public(models.Model):
    title = models.CharField(verbose_name='Публикации', max_length=150)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    image = models.CharField(verbose_name='Картинка', max_length=200)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title


class New_Products(models.Model):
    product_name = models.CharField(verbose_name='Имя продукта', max_length=150)
    slug = models.SlugField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name = 'Новинка')

    class Meta:
        verbose_name = 'Новинка'
        verbose_name_plural = 'Новинки'

    def __str__(self):
        return self.product_name


class Enxibitation_Calendar(models.Model):
    name_exhibition = models.TextField(verbose_name='Календарь выставок')
    period = models.CharField(verbose_name='Период', max_length=100)
    data_of_participation = models.CharField(verbose_name='Дата участия', max_length=100)
    location = models.CharField(verbose_name='Место проведения выставки', max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Календарь выставки'
        verbose_name_plural = 'Календарь выставок'

    def __str__(self):
        return self.name_exhibition