from django.contrib import admin
from .models import ProductModel,  InventoryModel

admin.site.register(ProductModel)
admin.site.register(InventoryModel)