# ecommerce_api/urls.py

from django.contrib import admin
from django.urls import path, include
from products.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')), 
    path('api/', include('orders.urls')), 
    path('', homepage), 
]
