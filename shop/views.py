from django.shortcuts import render
from django.utils.text import slugify
from rest_framework import generics

from shop.models import Product, Category
from shop.serializers import CategorySerializer, SubcategorySerializer, ProductSerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryUpdateAPIView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

