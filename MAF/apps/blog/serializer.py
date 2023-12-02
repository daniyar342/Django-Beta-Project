from rest_framework import serializers
from .models import Events, Public, New_Products


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Public
        fields = '__all__'


class NewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_Products
        fields = '__all__'
