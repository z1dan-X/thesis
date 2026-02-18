from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.show_shop_page, name='shop'),
    path('product-detail/<slug:slug>/', views.show_product_detail_page, name='product_detail'),
    path('wishlist/<slug:product_slug>', views.add_or_delete_wishlist, name='wishlist-add-or-remove'),
    path('add-to-cart/<slug:product_slug>', views.add_product_to_cart, name='add-to-cart'),
    path('delete-from-cart/<slug:product_slug>', views.delete_product_from_cart, name='delete-from-cart')
]