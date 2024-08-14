from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from users.models import User


class Category(models.Model):
    """ Модель категории """
    title = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(verbose_name='Слаг', unique=True, blank=True)
    image = models.ImageField(upload_to='category/', verbose_name='Изображение', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs): # функция для автоматического формирования слага при создании экземпляра модели

        if not self.slug:
            count = 1
            # Генерируем slug на основе title, если его нет
            self.slug = slugify(unidecode(self.title))
            # Убедимся, что slug уникален
            if Category.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-{count}'
                count += 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    """ Модель подкатегории """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=50, verbose_name='Подкатегория')
    slug = models.SlugField(verbose_name='Слаг', unique=True, blank=True)
    image = models.ImageField(upload_to='subcategory/', verbose_name='Изображение', blank=True, null=True)

    def __str__(self):
        return f'{self.title} ({self.category})'

    def save(self, *args, **kwargs): # функция для автоматического формирования слага при создании экземпляра модели

        if not self.slug:
            count = 1
            # Генерируем slug на основе title, если его нет
            self.slug = slugify(unidecode(self.title))
            # Убедимся, что slug уникален
            if Subcategory.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-{count}'
                count += 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    """ Модель товара """
    title = models.CharField(max_length=150, verbose_name='Название')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    price = models.PositiveIntegerField(verbose_name="Цена")
    image_small = models.ImageField(upload_to='products/small/', verbose_name='превью', blank=True, null=True)
    image_medium = models.ImageField(upload_to='products/medium/', verbose_name='изображение средний размер', blank=True, null=True)
    image_large = models.ImageField(upload_to='products/large/', verbose_name='изображение большой размер', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Cart(models.Model):
    """ Модель корзины """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='покупатель')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создана')
    products = models.ManyToManyField(Product, through='CartItem')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"Cart for {self.user}"


class CartItem(models.Model):
    """ Модель позиции в корзине """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='анализ')
    count = models.PositiveIntegerField(default=1, verbose_name="Кол-во")

    class Meta:
        verbose_name = 'Позиция в корзине'
        verbose_name_plural = 'Позиции в корзине'

    @property
    def position_cost(self) -> int:
        return self.count * self.product.price
