from django.contrib import admin
from sales.models import SalesPerson, Client, Product, License

# Register your models here.
admin.site.register(SalesPerson)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(License)