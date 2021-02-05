from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SalesPerson(User):
    name = models.CharField(max_length=200, null=False, blank=False)

class Client(User):
    name = models.CharField(max_length=200, null=False, blank=False)

class Product(models.Model):
    name = models.CharField(verbose_name='Product name', max_length=300, null=False, blank=False, unique=True)

class License(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='licenses')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='licenses')
    seller = models.ForeignKey('SalesPerson', on_delete=models.SET_NULL, related_name='licenses', null=True, blank=True)
    expire_date = models.DateField(null=False, blank=False)