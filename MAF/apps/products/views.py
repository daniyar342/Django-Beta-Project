from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics
from .models import Product
from .serializer import ProductSeializer

class Index(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeializer
    context_object_name = 'products'
