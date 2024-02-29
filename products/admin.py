from django.contrib import admin

from products.models import Category, SubCategory, Product, Basket, BasketProducts


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'category')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_small', 'image_medium', 'image_large', 'subcategory')


@admin.register(BasketProducts)
class BasketProductsAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'product')


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user',)
