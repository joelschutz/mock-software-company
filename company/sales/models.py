from datetime import timedelta

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
    price = models.IntegerField(verbose_name='Price per month($)', default=-1, null=False, blank=False)

    def __str__(self):
        return self.name


class License(models.Model):
    ONE_MONTH = timedelta(weeks=4)
    SIX_MONTHS = timedelta(weeks=24)
    ONE_YEAR = timedelta(weeks=48)
    TWO_YEARS = timedelta(weeks=96)
    LICENSE_DURATION_CHOICES = [
        (ONE_MONTH, '1 month'),
        (SIX_MONTHS, '6 months'),
        (ONE_YEAR, '1 year'),
        (TWO_YEARS, '2 years')
    ]
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='licenses')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='licenses')
    seller = models.ForeignKey('SalesPerson', on_delete=models.SET_NULL, related_name='licenses', null=True, blank=True)
    activation_date = models.DateField(default=None, null=True, blank=False)
    valid_time = models.DurationField(null=False, blank=False, choices=LICENSE_DURATION_CHOICES, default=ONE_MONTH)
    activated = models.BooleanField(default=False, null=False, blank=False)

    @property
    def expire_date(self):
        if self.activated:
            return self.activation_date + self.valid_time
        return None

    def __str__(self):
        return f'{self.product} - {self.client}'