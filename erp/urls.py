from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/<int:id>', views.inventory_detail, name='inventory_detail'),
    path('inventory-delete/<int:id>', views.inventory_delete, name='inventory_delete'),
    path('create-product/', views.create_product, name='create-product'),
]
