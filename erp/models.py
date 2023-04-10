from django.db import models
from account.models import UserProfile
from django.conf import settings

# Create your models here.
class ProductModel(models.Model):#PM
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    t_sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    t_size = models.CharField(choices=t_sizes, max_length=1)
    quantity = models.IntegerField(default=0)


class InventoryModel(models.Model):#IM
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    total = models.IntegerField(null=False)