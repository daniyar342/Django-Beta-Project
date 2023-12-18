from rest_framework.response import Response

from .models import Product, Order
from rest_framework import viewsets, generics
from rest_framework import mixins
from .serializer import ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import CanPostProductPermission


from rest_framework.permissions import IsAuthenticated
from .permissions import CanPostProductPermission


class ProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CanPostProductPermission]
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name',]


class ProductRetrieveView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


    def get(self,request,pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)



class OrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self,request, *args, **kwargs):
        response = super().create(request,args,**kwargs)
        return response


