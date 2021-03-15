from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    
    path('shop', views.shop, name='shop'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('shop_details', views.shop_details, name='shop_details'),
    path('shop_grid', views.shop_grid, name='shop_grid'),
]