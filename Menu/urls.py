from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('anasayfa', index, name='index'),
    path('corbalar', corbalar, name='corbalar'),
    path('kebaplar', kebaplar, name='kebaplar'),
    path('pideler', pideler, name='pideler'),
    path('tatlilar', tatlilar, name='tatlilar'),
    path('icecekler', icecekler, name='icecekler'),
    path('sepet', sepet, name='sepet'),
    path('orderdetail', order, name='orderdetail'),
]
