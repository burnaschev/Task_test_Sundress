from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    slug = models.SlugField(unique=True, verbose_name='slug')
    image = models.ImageField(upload_to='category_images/', verbose_name='изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'


class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    slug = models.SlugField(unique=True, verbose_name='slug')
    image = models.ImageField(upload_to='subcategory_images/', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегорий'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    slug = models.SlugField(unique=True, verbose_name='slug')
    image = models.ImageField(upload_to='product_images/', verbose_name='изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категорий')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='подкатегорий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='корзина')
    quantity = models.PositiveIntegerField(default=1, verbose_name='количество')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
