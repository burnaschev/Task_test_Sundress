from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    slug = models.SlugField(unique=True, verbose_name='slug')
    image = models.ImageField(upload_to='category_images/', **NULLABLE, verbose_name='изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'


class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    slug = models.SlugField(unique=True, verbose_name='slug')
    image = models.ImageField(upload_to='subcategory_images/', **NULLABLE, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегорий'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    slug = models.SlugField(unique=True, verbose_name='slug')
    image_small = models.ImageField(upload_to='product_images/small/', **NULLABLE,
                                    verbose_name="маленький размер изображения")
    image_medium = models.ImageField(upload_to='product_images/medium/', **NULLABLE,
                                     verbose_name='средний размер изображения')
    image_large = models.ImageField(upload_to='product_images/large/', **NULLABLE,
                                    verbose_name='большой размер изображения')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='подкатегорий')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket',
                             verbose_name='пользователь')

    def __str__(self):
        return f"Корзина пользователя {self.user.email}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class BasketProducts(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket_products', verbose_name='корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    quantity = models.PositiveIntegerField(default=1, verbose_name='количество')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} в корзине {self.basket}"

    class Meta:
        verbose_name = 'Позиция в корзине'
        verbose_name_plural = 'Позиции в корзине'
