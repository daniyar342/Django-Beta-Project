# models.py in your app directory

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=130)
    slug = models.SlugField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    compound = models.TextField()
    description = models.TextField()
    applying = models.TextField()
    waiting_time = models.TextField()
    release = models.TextField()
    storage_date = models.TextField()
    storage_conditions = models.TextField()
    # category = models.ForeignKey(Category,null=True,blank=True)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name