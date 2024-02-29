from rest_framework import generics
from rest_framework.response import Response

from products.models import Category, Product, BasketProducts, Basket
from products.paginators import CategoryPaginator, ProductPaginator
from rest_framework.permissions import AllowAny, IsAuthenticated

from products.permission import IsUser
from products.serializers import CategorySerializer, ProductSerializer, \
    BasketProductsRetrieveSerializer, BasketCreateSerializer, BasketProductSerializer, BasketUpdateSerializer, \
    BasketProductCreateSerializer


class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPaginator
    permission_classes = [AllowAny]


class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPaginator
    permission_classes = [AllowAny]


class BasketCreateApiView(generics.CreateAPIView):
    serializer_class = BasketCreateSerializer
    model = Basket.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class BasketProductUpdateApiView(generics.UpdateAPIView):
    queryset = BasketProducts.objects.all()
    serializer_class = BasketUpdateSerializer
    permission_classes = [IsUser]


class BasketProductCreateApiView(generics.CreateAPIView):
    serializer_class = BasketProductCreateSerializer
    permission_classes = [IsUser]

    def perform_create(self, serializer):
        basket = Basket.objects.get(user=self.request.user)
        serializer.save(basket=basket)


class BasketProductDeleteCreateApiView(generics.DestroyAPIView):
    serializer_class = BasketProductSerializer
    queryset = BasketProducts.objects.all()
    permission_classes = [IsUser]


class BasketRetrieveApiView(generics.RetrieveAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketProductsRetrieveSerializer
    permission_classes = [IsUser]

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)


class BasketClearApiView(generics.DestroyAPIView):
    permission_classes = [IsUser]

    def delete(self, request, *args, **kwargs):
        user = request.user
        basket_products = BasketProducts.objects.filter(basket__user=user)
        basket_products.delete()
        return Response({"message": "Корзина успешно очищена."})
