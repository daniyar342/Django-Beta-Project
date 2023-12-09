from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для продуктов"""
    class Meta:
        model = Product
        fields = ('id', 'name')

class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для заказов"""
    class Meta:
        model = Order
        fields = ('id', 'name', 'phone', 'email', 'date')
