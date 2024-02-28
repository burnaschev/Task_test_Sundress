from rest_framework import serializers

from products.models import Category, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(source='subcategory', many=True)

    class Meta:
        model = Category
        fields = ('name', 'slug', 'image', 'subcategory')
