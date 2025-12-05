from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_routes, name='get_routes'),
    path('products/', get_products, name='products'),
    
]
    