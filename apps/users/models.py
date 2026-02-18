from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.shop.models import Product


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True, verbose_name='Никнейм')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    profile_image = models.ImageField(upload_to='users/profile_images', null=True, blank=True, default='base_images/default_user.webp')

    def __str__(self):
        return self.username


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ManyToManyField(Product, related_name='product')
