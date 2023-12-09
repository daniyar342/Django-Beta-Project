from django.http import HttpResponse
from rest_framework import filters, mixins
from .models import Product, Order
from rest_framework import viewsets
from .serializer import ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import CanPostProductPermission



class ProductViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CanPostProductPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]


class OrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self,request, *args, **kwargs):
        response = super().create(request,args,**kwargs)
        return response


