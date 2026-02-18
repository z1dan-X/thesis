from django.contrib import admin
from .models import CartItem, Checkout, CheckoutProducts


class CheckoutProductsInline(admin.TabularInline):
    model = CheckoutProducts
    readonly_fields = ['product', 'price', 'quantity']


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'total_price', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['first_name', 'email']
    inlines = [CheckoutProductsInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']

