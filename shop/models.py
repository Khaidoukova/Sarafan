from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(verbose_name='Слаг', unique=True)
    image = models.ImageField(upload_to='category/', verbose_name='Изображение', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(verbose_name='Слаг', unique=True)
    image = models.ImageField(upload_to='subcategory/', verbose_name='Изображение', blank=True, null=True)

    def __str__(self):
        return f'{self.title} ({self.category})'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    SIZES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large')
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    size = models.CharField(max_length=10, choices=SIZES)

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товара'

