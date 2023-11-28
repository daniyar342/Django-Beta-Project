# models.py in your app directory

from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Категории', max_length=150)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(verbose_name="Подкатегории",max_length=130)
    slug = models.SlugField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name="Название",max_length=255)
    compound = models.TextField(verbose_name="Состав")
    description = models.TextField(verbose_name="Описание")
    # Вооот здесь я поменял
    applying = models.TextField(verbose_name="Применение")
    waiting_time = models.TextField(verbose_name="Время ожидания")
    release_form = models.TextField(verbose_name="Форма выпуска")
    storage_date = models.TextField(verbose_name='Срок хранение')
    storage_conditions = models.TextField(verbose_name='Условия хранения ')
    # category = models.ForeignKey(Category,null=True,blank=True)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'

    def __str__(self):
        return self.name

