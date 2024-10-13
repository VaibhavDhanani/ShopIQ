from django.contrib import admin
from Products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'company', 'quantity', 'category')
    search_fields = ('name', 'company')
    list_filter = ('category',)
