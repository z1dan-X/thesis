from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('cart/', views.show_shopping_cart, name='cart_detail'),
    path('checkout/', views.show_checkout, name='checkout'),
]