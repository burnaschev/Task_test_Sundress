from rest_framework import generics

from products.models import Category, Product, Basket
from products.paginators import CategoryPaginator, ProductPaginator
from products.serializers import CategorySerializer, ProductSerializer, BasketUpdateSerializer, \
    BasketRetrieveSerializer


class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPaginator


class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPaginator


class BasketUpdateApiView(generics.UpdateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketUpdateSerializer


class BasketRetrieveApiView(generics.RetrieveAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketRetrieveSerializer
