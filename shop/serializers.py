from rest_framework import serializers

from shop.models import Product, Category, Subcategory, Cart, CartItem


class CategorySerializer(serializers.ModelSerializer):
    '''Сериализатор для категории товаров'''
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'image')


class SubcategorySerializer(serializers.ModelSerializer):
    '''Сериализатор для подкатегории товаров'''
    class Meta:
        model = Subcategory
        fields = ('id', 'category', 'title', 'slug', 'image')


class ProductSerializer(serializers.ModelSerializer):
    '''Сериализатор для товаров'''
    subcategory_title = serializers.CharField(source='subcategory.title', read_only=True)
    category_title = serializers.CharField(source='subcategory.category.title', read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'title', 'subcategory', 'subcategory_title', 'category_title', 'price')
        extra_kwargs = {
            'subcategory': {'required': True}
        }


class CartItemSerializer(serializers.ModelSerializer):
    '''Сериализатор для позиции в корзине'''
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'count')


class CartSerializer(serializers.ModelSerializer):
    '''Сериализатор для корзины'''
    cartitems = CartItemSerializer(many=True, source='cartitem_set', read_only=True)
    total_cart_price = serializers.SerializerMethodField()
    total_count = serializers.SerializerMethodField()

    def get_total_cart_price(self, obj: Cart) -> int:
        ''' Рассчитываю общую стоимость корзины '''
        total = 0
        for item in obj.cartitem_set.all():
            total += item.product.price * item.count
        return total

    def get_total_count(self, obj: Cart) -> int:
        ''' Рассчитываю общую стоимость корзины '''
        return sum(item.count for item in obj.cartitem_set.all())

    class Meta:
        model = Cart
        fields = ('id', 'user', 'cartitems', 'total_cart_price', 'total_count')

