from django.urls import path
from shop.apps import ShopConfig
from shop.views import CategoryCreateAPIView, CategoryListAPIView, CategoryRetrieveAPIView, CategoryUpdateAPIView

app_name = ShopConfig.name


urlpatterns = [
    path('category/create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_detail'),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category_update'),


]
