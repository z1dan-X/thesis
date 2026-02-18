from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.Registration_page, name='registration'),
    path('login/', views.Login_page, name='login'),
    path('logout/', views.Logout_page, name='logout'),
    path('wishlist/', views.show_wishlist_page, name='wishlist')
]