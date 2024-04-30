from django.contrib import admin

from products.models import Product

# Register your models here.
class AdminModel(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'created_at', 'updated_at', 'owner']

admin.site.register(Product, AdminModel)
