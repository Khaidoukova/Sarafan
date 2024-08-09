from django.db import models
from django.utils.text import slugify

from users.models import User


class Category(models.Model):
    """ Модель категории """
    title = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(verbose_name='Слаг', unique=True)
    image = models.ImageField(upload_to='category/', verbose_name='Изображение', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        ''' Сохранение поля slug по названию категории '''

        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Subcategory(models.Model):
    """ Модель подкатегории """
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
    """ Модель товара """
    title = models.CharField(max_length=150, verbose_name='Название')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    price = models.PositiveIntegerField(verbose_name="Цена")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    """ Модель изображения товара """
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


class Cart(models.Model):
    """ Модель корзины """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='покупатель')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создана')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"Cart for {self.user}"


class CartItem(models.Model):
    """ Модель позиции в корзине """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='анализ')
    count = models.PositiveIntegerField(verbose_name="Кол-во")

    class Meta:
        verbose_name = 'Позиция в корзине'
        verbose_name_plural = 'Позиции в корзине'

    @property
    def position_cost(self) -> int:
        return self.count * self.product.price
