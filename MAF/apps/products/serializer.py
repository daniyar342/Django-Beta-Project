from rest_framework import serializers
from .models import Product, Order


class ProductSeializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'date']