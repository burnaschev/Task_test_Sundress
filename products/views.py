from rest_framework import generics

from products.models import Category
from products.paginators import CategoryPaginator
from products.serializers import CategorySerializer


class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPaginator
