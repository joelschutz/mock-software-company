from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SalesPerson(User):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sales Person'

class Client(User):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Client'

class Product(models.Model):
    name = models.CharField(verbose_name='Product name', max_length=300, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class License(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='licenses')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='licenses')
    seller = models.ForeignKey('SalesPerson', on_delete=models.SET_NULL, related_name='licenses', null=True, blank=True)
    activation_date = models.DateField(null=False, blank=False)
    valid_time = models.DurationField(null=False, blank=False)

    @property
    def expire_date(self):
        return self.activation_date + self.valid_time

    def __str__(self):
        return f'{self.product} - {self.client}'