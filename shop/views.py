from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shop.models import Product, Category, Subcategory, Cart, CartItem
from shop.paginators import ShopPaginator
from shop.permissions import IsCartOwner
from shop.serializers import CategorySerializer, SubcategorySerializer, ProductSerializer, CartSerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    ''' Generic представление для создания категории'''
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryListAPIView(generics.ListAPIView):
    ''' Generic представление для вывода списка категорий'''
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = ShopPaginator


class SubcategoryCreateAPIView(generics.CreateAPIView):
    ''' Generic представление для создания подкатегории'''
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()


class SubcategoryListAPIView(generics.ListAPIView):
    ''' Generic представление для вывода списка подкатегорий'''
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()
    pagination_class = ShopPaginator


class ProductViewSet(viewsets.ModelViewSet):
    ''' Набор представлений для создания, редактирования, удаления и вывода списка продуктов'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ShopPaginator


class CartViewSet(viewsets.ViewSet):
    ''' Набор представлений для работы с корзиной'''
    permission_classes = [IsAuthenticated, IsCartOwner] # разрешения для работы с корзиной

    def list(self, request): # вывод содержимого корзины
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def add_product(self, request, product_id: int): # добавление товара в корзину по id
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.count += 1
        cart_item.save()
        return Response(status=status.HTTP_200_OK)

    def remove_product(self, request, product_id: int): # удаление товара из корзины по id
        cart = Cart.objects.get(user=request.user)
        product = Product.objects.get(id=product_id)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def clear_cart(self, request): # очистка корзины
        cart = Cart.objects.get(user=request.user)
        cart.products.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

