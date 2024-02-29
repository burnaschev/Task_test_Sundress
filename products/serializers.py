from rest_framework import serializers

from products.models import Category, SubCategory, Product, Basket, BasketProducts


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('name', 'slug', 'image')


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True, source='subcategory_set')

    class Meta:
        model = Category
        fields = ('name', 'slug', 'image', 'subcategory')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'slug', 'subcategory', 'category', 'price', 'image_small', 'image_medium', 'image_large')


class BasketCreateSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(read_only=True)

    class Meta:
        model = Basket
        fields = '__all__'

    def validate(self, instance):
        user = self.context['request'].user
        existing_basket = Basket.objects.filter(user=user).first()
        if existing_basket:
            raise serializers.ValidationError("Корзина уже существует для данного пользователя.")
        return instance


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('user',)


class BasketProductSerializer(serializers.ModelSerializer):
    basket_user = BasketSerializer(many=True, read_only=True)

    class Meta:
        model = BasketProducts
        fields = ('basket', 'product', 'quantity', 'basket_user')


class BasketProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketProducts
        fields = ['product', 'quantity']

    def validate(self, data):
        product = data.get('product')
        user = self.context['request'].user
        basket = Basket.objects.get(user=user)
        if basket.basket_products.filter(product=product).exists():
            raise serializers.ValidationError("Этот продукт уже добавлен в корзину.")
        return data


class BasketUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketProducts
        fields = ('quantity',)


class BasketProductsRetrieveSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = BasketProducts
        fields = ('product_count', 'total_amount',)

    def get_product_count(self, obj):
        return obj.basket_products.count()

    def get_total_amount(self, obj):
        total_amount = 0
        for item in obj.basket_products.all():
            total_amount += item.product.price * item.quantity
        return total_amount
