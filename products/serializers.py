from rest_framework import serializers

from products.models import Category, SubCategory, Product, Basket


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('name', 'slug', 'image', 'category')


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ('name', 'slug', 'image', 'subcategory')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'slug', 'subcategory', 'category', 'price', 'image_small', 'image_medium', 'image_large')


class BasketUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('product', 'quantity')


class BasketRetrieveSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField(read_only=True)
    total_amount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Basket
        fields = ('product_count', 'total_amount')

    def get_product_count(self, obj):
        return obj.product.count()

    def get_total_amount(self, obj):
        total_amount = 0
        for item in obj.product.all():
            total_amount += item.price * item.quantity
        return total_amount
