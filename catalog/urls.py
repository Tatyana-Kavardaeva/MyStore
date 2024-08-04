from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, products_detail, products_list

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('products/<int:pk>/', products_detail, name='products_detail'),
    path('contact/', contact, name='contact'),
]
