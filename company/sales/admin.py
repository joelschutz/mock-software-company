from django.contrib import admin
from sales.models import SalesPerson, Client, Product, License

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username')
    list_display_links = ('id',)
    search_fields = ('name', 'username')
    list_per_page = 10

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id',)
    search_fields = ('name', 'price')
    list_filter = ('price',)
    list_per_page = 10

class LicenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'client', 'seller', 'valid_time', 'activated')
    list_display_links = ('id',)
    search_fields = ('product', 'client', 'seller', 'valid_time')
    list_editable = ('activated',)
    list_filter = ('product', 'client', 'seller', 'valid_time', 'activated')
    list_per_page = 10

admin.site.register(SalesPerson, PersonAdmin)
admin.site.register(Client, PersonAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(License, LicenseAdmin)