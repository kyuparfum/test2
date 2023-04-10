from django.db import models
from erp.models import ProductModel
from django.conf import settings

class QuantityModel(models.Model):#IM
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    decreased = models.IntegerField(null=False)