from django.db import models
from ..common.models import BaseModel
from ..shop.models import Product
from ..users.models import User


class CartItem(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return int(self.product.price) * self.quantity

    def __str__(self):
        return f'{self.product} - {self.quantity}'


class Checkout(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} -- {self.phone_number}. Статус оплаты: {self.is_paid}'


class CheckoutProducts(models.Model):
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.title} -- X{self.quantity}'