from django.urls import path
from .views import *


urlpatterns = [
    path('', login_kasaadmin, name="login"),
    path('dashboard', dashboard, name="dashboard"),
    path('productlist', productlistview, name="productlist"),
    path('productadd', productadd, name="productadd"),
    path('upgradeproduct/<slug:slug>', updateproduct, name="updateproduct"),
    path('dashboard/whatsapp', whatsapp, name="whatsapp"),
]