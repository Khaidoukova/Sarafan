from rest_framework import serializers

from shop.models import Product, Category, Subcategory, Cart, CartItem


class CategorySerializer(serializers.ModelSerializer):
    '''Сериализатор для категории товаров'''
    class Meta:
        model = Category
        fields = ('title', 'image')


class SubcategorySerializer(serializers.ModelSerializer):
    '''Сериализатор для подкатегории товаров'''
    class Meta:
        model = Subcategory
        fields = ('title', 'category', 'image')


class ProductSerializer(serializers.ModelSerializer):
    '''Сериализатор для товаров'''

    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    '''Сериализатор для товаров'''

    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    '''Сериализатор для товаров'''

    class Meta:
        model = CartItem
        fields = '__all__'