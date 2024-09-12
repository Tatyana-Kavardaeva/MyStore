from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactPageView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, toggle_activity, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    # path('versions/', , name='version'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
]
