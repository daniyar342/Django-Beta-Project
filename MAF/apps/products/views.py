from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class Index(ListView):
    model = Product
    template_name = 'index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'
