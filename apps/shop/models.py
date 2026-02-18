from django.db import models
from django.conf import settings

from ..common.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Слаг")
    image = models.ImageField(upload_to='category_images/', null=True, blank=True, verbose_name='Фотография')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_at']


class Product(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products',
    )
    preview = models.ImageField(upload_to='product_previews/', null=True, blank=True, verbose_name='Превью')
    main_image = models.ImageField(upload_to='product_images/', verbose_name='Главное фото')
    price = models.CharField(max_length=10, verbose_name='Цена (в долларах)')
    short_description = models.CharField(max_length=150, verbose_name='Краткое Описание')
    full_description = models.TextField(max_length=300, verbose_name='Полное описание')
    category = models.ManyToManyField(Category, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Продукт')
    image = models.ImageField(upload_to='product_images/gallery/', verbose_name='Дополнительное фото')

    class Meta:
        verbose_name = 'Дополнительное фото'
        verbose_name_plural = 'Дополнительные фото'


class Comment(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=120, verbose_name='Напишите отзыв о товаре здесь...')
