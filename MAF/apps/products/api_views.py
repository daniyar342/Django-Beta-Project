from django.http import HttpResponse

from .models import Product, Order
from rest_framework import viewsets
from .serializer import ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import CanPostProductPermission



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CanPostProductPermission]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self,request, *args, **kwargs):
        response = super().create(request,args,**kwargs)
        return response


