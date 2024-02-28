from django.urls import path

from products.apps import ProductsConfig
from products.views import CategoryListApiView, ProductListApiView, BasketUpdateApiView, BasketRetrieveApiView

app_name = ProductsConfig.name


urlpatterns = [
    path('category/list/', CategoryListApiView.as_view(), name='category-list'),
    path('product/list/', ProductListApiView.as_view(), name='product-list'),
    path('basket/<int:pk>/', BasketUpdateApiView.as_view(), name='update-basket'),
    path('basket/view/<int:pk>', BasketRetrieveApiView.as_view(), name='basket-view')
]
