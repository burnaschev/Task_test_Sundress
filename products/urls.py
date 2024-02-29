from django.urls import path

from products.apps import ProductsConfig
from products.views import CategoryListApiView, ProductListApiView, BasketRetrieveApiView, \
    BasketCreateApiView, BasketProductUpdateApiView, BasketProductCreateApiView, \
    BasketProductDeleteCreateApiView, BasketClearApiView

app_name = ProductsConfig.name

urlpatterns = [
    path('category/list/', CategoryListApiView.as_view(), name='category-list'),
    path('product/list/', ProductListApiView.as_view(), name='product-list'),
    path('basket/create/', BasketCreateApiView.as_view(), name='basket-create'),
    path('basket/product/create/', BasketProductCreateApiView.as_view(), name='create-product-basket'),
    path('basket/product/update/<int:pk>/', BasketProductUpdateApiView.as_view(), name='update-product-basket'),
    path('basket/product/delete/<int:pk>/', BasketProductDeleteCreateApiView.as_view(), name='delete-product-basket'),
    path('basket/view/<int:pk>/', BasketRetrieveApiView.as_view(), name='basket-view'),
    path('basket/clear/', BasketClearApiView.as_view(), name='basket-clear')
]
