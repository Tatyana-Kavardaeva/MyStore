from django.urls import path
from catalog.views import home, contact


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
]
