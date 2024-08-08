from django.urls import path
from .views import *

urlpatterns = [
    path('product/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-delete'),
]
