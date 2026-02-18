from django.db import models
from ..common.models import BaseModel


class Discount(BaseModel):
    short_description = models.CharField(max_length=50, verbose_name="Короткое описание")
    main_text = models.CharField(max_length=100, verbose_name="Основной текст")
    image = models.ImageField(upload_to='discount_images/', null=True, blank=True)

    def __str__(self):
        return self.main_text

    class Meta:
        verbose_name = 'Скидка на данный момент'
        verbose_name_plural = 'Скидки на данный момент'
        ordering = ['-created_at']

