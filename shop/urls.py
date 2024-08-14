from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop.apps import ShopConfig
from shop.views import CategoryCreateAPIView, CategoryListAPIView,  \
    SubcategoryCreateAPIView, SubcategoryListAPIView, CartViewSet, \
    ProductViewSet

app_name = ShopConfig.name
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    # работа с категориями
    path('category/create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),

    # работа с подкатегорями
    path('subcategory/create/', SubcategoryCreateAPIView.as_view(), name='category_create'),
    path('subcategory/', SubcategoryListAPIView.as_view(), name='category_list'),

    # работа с продуктами
    path('', include(router.urls)),
    # работа с корзиной
    path('cart/', CartViewSet.as_view({'get': 'list'})),
    path('cart/add/<int:product_id>/', CartViewSet.as_view({'post': 'add_product'})),
    path('cart/remove/<int:product_id>/', CartViewSet.as_view({'delete': 'remove_product'})),
    path('cart/clear/', CartViewSet.as_view({'delete': 'clear_cart'})),

]
