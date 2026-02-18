from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.show_home_page, name='home'),
    path('about-us', views.show_about_us_page, name='about-us'),
]